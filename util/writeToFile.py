import os
from datetime import datetime




def writeToFile(SearchedPages):
    filename = 'searchedWords'+datetime.now().strftime("%Y%m%d-%H%M%S")+'.txt'
    fullPath = os.path.join('./FoundSentences',filename)
    File = open(fullPath, "w", encoding='utf-8')
    File.write('Found words: ')
    NoWords = []
    for i in range(len(SearchedPages)):
        if SearchedPages[i].Sentences != []:
            File.write('\n' + SearchedPages[i].Page)
            for j in range(len(SearchedPages[i].Sentences)):
                File.write('\n' + SearchedPages[i].Sentences[j])
        else:
            NoWords.append(SearchedPages[i].Page)
    if NoWords != []:
        File.write('\n No words found from following pages: ')
        for i in range(len(NoWords)):
            File.write('\n' + SearchedPages[i].Page)
    File.close()
    return filename