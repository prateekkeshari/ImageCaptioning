import os
from langchain.document_loaders import ImageCaptionLoader
from langchain.indexes import VectorstoreIndexCreator
import logging
logging.getLogger("transformers.generation_utils").setLevel(logging.ERROR)
logging.getLogger("tokenizers").setLevel(logging.ERROR)
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
def collect_image_urls():
    image_urls = []
    while len(image_urls) < 4:
        url = input(f"Enter image URL {len(image_urls) + 1} (at least 4 required): ")
        if url:
            image_urls.append(url)
        else:
            print("Please enter a valid image URL.")
    return image_urls

list_image_urls = collect_image_urls()
os.environ['OPENAI_API_KEY'] = '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'
loader = ImageCaptionLoader(path_images=list_image_urls)
list_docs = loader.load()
index = VectorstoreIndexCreator().from_loaders([loader])
while True:
    query = input("Enter your query (type 'exit' to quit): ")
    
    if query.lower() == 'exit':
        break

    result = index.query(query)
    print(result)
