import requests
import os
from duckduckgo_search import DDGS

def search_sources(topic):

    urls = [
    ]

    with DDGS() as ddgs:
        for r in ddgs.text(topic, max_results=5):
            urls.append(r['href'])

    return urls