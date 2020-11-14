#OLD PARAGRAPH SEARCH

import sys
import os
from main import visitPage as vp
from util import writeToFile as wf
#from Util import printSentences as p



def ParagraphSearch(url, depth, words):
    if isinstance(words, str) == True: #convert to list if only one search word
        words = [words]
    usedUrls = {url} #add starting point
    foundUrls = set()
    sentences = []
    foundSentences = []
    foundUrls, sentences = vp.visitPage(url, words) #first visit
    if foundUrls is None: #check if no new urls found
        if sentences is None: #if no sentences found either
            print('No results with word(s) ', words, ' in ', url) #move to method
            return url, None
        else:
            print('Found following sentences ', words, ' in ', url) #move to method
            for sentence in sentences:
                print(sentence)
                #print loop sentences = visit[1] - create method
                return url, sentences
    else:
        foundSentences.insert(0,[url,sentences]) #add sentences, with first element as url of page
        currDepth = 0
        while depth > currDepth:
            currDepth += 1
            newUrls = set()
            for URL in foundUrls:
                visit = vp.visitPage(URL, words)
                if visit[1] != None: #add only if found sentences
                    foundSentences.insert(currDepth,[URL, visit[1]])
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
        return wf.writeToFile(foundSentences) #return filename, TODO make this more sensible