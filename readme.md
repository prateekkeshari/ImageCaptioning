# Image Captioning using Langchain

This code performs image captioning using Langchain, a Python package for natural language processing and machine learning. The code uses an image caption loader to load captions for a set of images, and then creates a vectorstore index to enable fast querying of captions based on user input.

## Requirements

-  Python 3.x
-  Langchain package (`pip install langchain`)
-  OpenAI API key

## Setup

1. Clone the repository to your local machine.
2. Install the Langchain package by running the command `pip install langchain` in your terminal.
3. Obtain an OpenAI API key and store it in a `.env` file in the root directory of the project, like this:

   ```
   OPENAI_API_KEY=<your-api-key>
   ```

4. Run the script `captions.py` using the command `python captions.py`.

## Usage

1. When prompted, enter the URLs of at least 4 images for which you want to generate captions.
2. Once the images are loaded, enter a query to search for captions that match your query. You can type "exit" to quit the program.

## Notes

-  The code sets the logging level to ignore warnings, so you may see some warning messages when running the code. These warnings can be safely ignored.
-  The code uses the OpenAI API to generate captions for the images. You will need a valid OpenAI API key to use this feature.
-  The code uses a vectorstore index to enable fast querying of captions based on user input. The index is created using the Langchain package and is stored in memory for the duration of the program.