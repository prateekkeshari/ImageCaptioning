# Image Captioning

This code performs image captioning using Langchain, a Python package for natural language processing and machine learning. The code uses an image caption loader to load captions for a set of images, and then creates a vectorstore index to enable fast querying of captions based on user input. The loader utilizes the pre-trained [Salesforce BLIP image captioning model.](https://huggingface.co/Salesforce/blip-image-captioning-base)

## Requirements

- Python 3.x
- Flask
- Langchain package
- OpenAI API key

## Setup

1. Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/image-captioning-webapp.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Obtain an OpenAI API key and store it in a `.env` file in the root directory of the project, like this:

```bash
OPENAI_API_KEY=<your-api-key>
```

4. Run the Flask web app:

run this if you want to just use the model without detailed descriptions
```bash
python imagemodel.py
```
or run this f you want to just use the model _with_ detailed descriptions
```bash
python imageopenai.py
```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8080`.
2. Enter an image URL and click the "Generate" button to receive an image caption.

## Notes

- The code sets the `TOKENIZERS_PARALLELISM` environment variable to 'false' to avoid deadlocks related to tokenizers parallelism.
- The code uses the OpenAI API to generate captions for the images. You will need a valid OpenAI API key to use this feature.
- The code uses a vectorstore index to enable fast querying of captions based on user input. The index is created using the Langchain package and is stored in memory for the duration of the program.
