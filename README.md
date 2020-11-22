# Paragraph search

Really simple webscraper, which searches for sentences inside paragraph tags, based on given keywords.

## Running the code

Currently this can be used on:
* command line with search.py (missing support for multiple keywords, needs work). Example:
`python3 search.py 'https://github.com/' 1 'code'`
* and from simple GUI, `gui.pyw`. Currently supports multiple words.
![alt text](sample.png "Gui")

Results are saved to FoundSentences as text files, and displayed in GUI if used.


## TODO
* Add scrollbar for page/result fields.
* Add statistics etc.
* Sentence saving format change?