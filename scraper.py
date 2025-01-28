import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    # Example: Extracting all paragraphs
    paragraphs = soup.find_all('p')
    return [p.get_text() for p in paragraphs]
