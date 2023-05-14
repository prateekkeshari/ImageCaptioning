from flask import Flask, render_template, request, jsonify

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

if __name__ == '__main__':
    import os
    from langchain.document_loaders import ImageCaptionLoader
    from langchain.indexes import VectorstoreIndexCreator

    os.environ['OPENAI_API_KEY'] = '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'

    app.run(debug=True)
