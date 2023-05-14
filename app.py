from langchain.document_loaders import ImageCaptionLoader
from langchain.indexes import VectorstoreIndexCreator
from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)
list_image_urls = []
index = None

os.environ['TOKENIZERS_PARALLELISM'] = 'false'

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

    result = index.query('describe this image in 3 ways.')
    return jsonify({'caption': result})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
