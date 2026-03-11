import requests
from bs4 import BeautifulSoup

MGT_PAGES = [
    'https://mgt.ai'
    'https://mgt.ai/insights'
    'https://mgt.ai/markets',
    'https://mgt.ai/partners'
    'https://mgt.ai/approach'
]

def fetch_mgt_content():
    contents = []
    for url in MGT_PAGES:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join(p.get_text() for p in paragraphs)
            contents.append(text[:4000])
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
    return contents