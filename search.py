import sys
import os
import ParagraphSearch as pc



if len(sys.argv) <= 3:
	print('Too few arguments. At least site, depth and one or more keywords needed.')
if len(sys.argv) >= 5:
    print('Too many arguments.')
else:
    website = sys.argv[1]
    depth = int(sys.argv[2])
    keywords = sys.argv[3]
    pc.ParagraphSearch(website, depth, keywords)
