from flask import Flask, jsonify, request, render_template
import os
import validators
import requests
import replicate
from io import BytesIO

app = Flask(__name__)
app.static_folder = 'templates/static'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    image_url = request.form.get('image_url')
    question = request.form.get('question')

    if not validate_image_url(image_url):
        return jsonify({'error': 'Invalid image URL.'}), 400

    if not is_valid_image(image_url):
        return jsonify({'error': 'The URL does not point to a valid image.'}), 400

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Check for any request errors

        image_bytes = BytesIO(response.content)  # Read the response content into BytesIO object

        input_data = {"image": image_bytes, "question": question} if question else {"image": image_bytes}

        output = replicate.run(
            "andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
            input=input_data
        )

        return jsonify({'caption': output})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An internal server error occurred.'}), 500



def validate_image_url(image_url):
    if not validators.url(image_url):
        return False
    return True

def is_valid_image(image_url):
    response = requests.head(image_url)
    content_type = response.headers.get('content-type')
    if content_type and 'image' in content_type:
        return True
    return False

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
