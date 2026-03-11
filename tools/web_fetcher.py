import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.get_text() for p in paragraphs) 
        return text[:4000]
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None