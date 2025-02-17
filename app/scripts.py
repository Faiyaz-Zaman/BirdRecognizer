import os
import requests
from duckduckgo_search import DDGS

def download_images(query, num_images=15, save_folder="bird_images"):
    bird_folder = os.path.join(save_folder, query.replace(" ", "_"))
    os.makedirs(bird_folder, exist_ok=True)
    
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=num_images)
    
    for i, result in enumerate(results):
        image_url = result["image"]
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            with open(f"{bird_folder}/{query.replace(' ', '_')}_{i}.jpg", "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {query} - {image_url}")
        except Exception as e:
            print(f"Failed to download {query} - {image_url}: {e}")

# List of bird names
bird_names = [
"Sparrows",
"Pigeons"
"Crows",
"Parrots",
"Eagles",
"Owls",
"Kingfishers",
"Peacocks",
"Ducks",
"Woodpeckers",
"Seagulls",
"Flamingos",
"Hummingbirds",
"Pelicans",
"Hawks",
"Penguins",
"Storks",
"Hornbills",
"Swallows",
"Robins"
]

# Download images for each bird
for bird in bird_names:
    download_images(bird, num_images=15)
