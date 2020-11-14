import requests
from urllib.parse import urlparse

def findSentences(lxml, words):
    sentences = []
    for word in words:
        for tag in lxml.descendants:
            if tag.name == 'p' and tag.string and word in tag.string:
                sentences.append(tag.string)
    return sentences

    
def findLinks(currentUrl,lxml):
    links = set()
    for link in lxml.find_all('a', href=True): #potentially swap to select
        if is_absolute(link['href']):
            links.add(link['href'])
        else:
            links.add(requests.compat.urljoin(currentUrl, link['href']))
    return links

def is_absolute(url):
    return bool(urlparse(url).netloc)