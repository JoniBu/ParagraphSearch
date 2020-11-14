import sys
import os
from main import visitPage as vp
from util import writeToFile as wf
#from Util import printSentences as p



class SearchedPage:
    def __init__(self, Page, Sentences):
        self.Page = Page
        self.Sentences = Sentences


def ParagraphSearch(url, depth, words):
    if isinstance(words, str) == True: #convert to list if only one search word
        words = [words]
    usedUrls = {url} #add starting point
    SearchedPages = []
    foundUrls = set()
    if depth == 0:
        SearchedPages.append(SearchedPage(url, vp.findSentencesOnly(url, words)))
        return wf.writeToFile(SearchedPages) #return filename, TODO make this more sensible
    currDepth = 0
    while depth > currDepth:
        currDepth += 1
        newUrls = set()
        visit = vp.visitPage(url, words)
        SearchedPages.append(SearchedPage(url, visit[1]))
        for URL in visit[0]:
            visit = vp.visitPage(URL, words)
            if visit[1] != None: #add only if found sentences
                SearchedPages.append(SearchedPage(URL, visit[1]))
            if visit[0] == None:
                continue
            for newUrl in visit[0]: #check all found urls
                if (newUrl not in usedUrls) and (newUrl not in foundUrls): #verify page is not already in used/found
                    newUrls.add(newUrl)
            usedUrls.update(visit[0])
        if  len(newUrls) > 0:
            foundUrls.update(newUrls) #replace with only new urls
        else:
            break
    return wf.writeToFile(SearchedPages) #return filename, TODO make this more sensible