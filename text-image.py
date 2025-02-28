import requests
from PIL import Image
from io import BytesIO
from duckduckgo_search import DDGS

def fetch_image(query):
    with DDGS() as ddgs:
        search_results = list(ddgs.images(query, max_results=1))
    if search_results:
        return search_results[0]['image']  # Extract direct image URL
    return None

def show_image(url):
    if not url:
        print("No valid image URL found.")
        return
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if request is successful
        img = Image.open(BytesIO(response.content))
        img.show()
    except Exception as e:
        print("Error loading image: {e}")

# User input
text_query = input("Enter the image description: ")
image_url = fetch_image(text_query)

if image_url:
    print("Image URL: {image_url}")
    show_image(image_url)
else:
    print("No image found.")
