import os
import requests
from bs4 import BeautifulSoup
import re

NUM_OF_IMAGES = 1

def download(url):
    print("Downloading Image...")
    response = requests.get(url)
    if response.status_code == 200:
        content_type = response.headers.get("content-type")
        if "image" in content_type:
            extension = content_type.split("/")[-1]
            file_name = query + "." + extension
            current_directory = os.getcwd()
            file_path = os.path.join(current_directory, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
        else:
            print("URL does not point to an image")
    else:
        print(f"Failed to download {url}")

# Scrape images
def scraper(url):
    print("Getting images from Google")
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        img_tags = soup.find_all("img")
        for idx, img in enumerate(img_tags):
            img_url = img.get("src")
            if img_url and img_url.startswith("http"):
                download(img_url)
                print(idx, img_url)
                if idx == NUM_OF_IMAGES:
                    print('IMAGES DOWNLOADED SUCCESSFULLY')
                    break
            else:
                print("Invalid URL")
    else:
        print("Failed to fetch images")

def startPro(author):
    base_url = "https://www.google.com/search"
    params = {
        "tbm": "isch",
        "q": query
    }
    query_string = "&".join([f"{key}={value}" for key, value in params.items()])
    url = f"{base_url}?{query_string}"
    print("Got query terms successfully")
    scraper(url)

# Main program
while True:
    query = str(input("Enter search query: "))
    if query.strip():
      break

startPro(query)
