import os
from datetime import datetime




def writeToFile(sentences):
    filename = 'searchedWords'+datetime.now().strftime("%Y%m%d-%H%M%S")+'.txt'
    fullPath = os.path.join('./FoundSentences',filename)
    File = open(fullPath, "w", encoding='utf-8')
    File.write('Found words: ')
    NoSentences = []
    for i in range(len(sentences)):
        if not sentences[i][1]: #TODO, as none found, add "header" and save all links where no founds
            #File.write('\nNo words found from this link.\n')
            NoSentences.append(sentences[i][0])
        else:
            File.write('\n' + sentences[i][0])
            for sentence in sentences[i][1]:
                File.write('\n' + sentence + '\n')
    File.write('\nNo words found from following pages:\n')
    for page in NoSentences:
        File.write(page + '\n')
    File.close()
    return filename