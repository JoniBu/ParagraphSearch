import os
import sys
from . import crawl
import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def visitPage(currentUrl, words):
    try:
        res = requests.get(currentUrl, headers=headers)
        if res.raise_for_status():
            return None, None
    except:
        return None, None
    lxml = bs4.BeautifulSoup(res.text, 'lxml')
    foundUrls = set(crawl.findLinks(currentUrl,lxml))
    if foundUrls is None:
        return None, crawl.findSentences(lxml, words)
    else:
        return foundUrls, crawl.findSentences(lxml, words)

