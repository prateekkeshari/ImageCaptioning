from langchain.document_loaders import ImageCaptionLoader
from langchain.indexes import VectorstoreIndexCreator
from flask import Flask, jsonify, request, render_template
from http.server import BaseHTTPRequestHandler
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from io import BytesIO

app = Flask(__name__)
list_image_urls = []
index = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    global index
    if not index:
        return 'Please upload an image before generating a caption.'

    image_url = request.form.get('image_url')
    loader = ImageCaptionLoader(path_images=[image_url])
    list_docs = loader.load()
    index = VectorstoreIndexCreator().from_loaders([loader])

    result = index.query('describe this image in 3 ways. Start by saying "this getyourguide experience" and end with "Book now on https://getyourguide.com"')
    return jsonify({'caption': result})

class Handler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.app = app
        super().__init__(*args, **kwargs)

    def handle_request(self, req):
        response = self.app.full_dispatch_request()
        return Response.from_app(response, self.send_response)

    def do_GET(self):
        req = Request(self)
        res = self.handle_request(req)
        self.send_response(res.status_code)
        for k, v in res.headers:
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(res.response[0])

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length)
        req = Request(self, input_stream=BytesIO(body))
        res = self.handle_request(req)
        self.send_response(res.status_code)
        for k, v in res.headers:
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(res.response[0])

def handler(event, context):
    return run_simple('localhost', 8080, app, request_handler=Handler)
