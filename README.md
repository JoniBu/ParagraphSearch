# Paragraph search

Really simple webscraper, which searches for sentences inside paragraph tags, based on given keywords.

## Running the code

Currently this can be used on:
* command line with search.py (missing support for multiple keywords, needs work). Example:
`python3 search.py 'https://github.com/' 1 'code'`
* and from simple GUI, `gui.pyw`. Currently supports multiple words.
![alt text](sample.png "Gui")

Results are saved to FoundSentences (as text files, xlsx would probably be better format), and displayed in GUI if used.



## TODO
* Make search incasesensitive
* fix stopping abort (terminating thread)
* add scrollbar https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget
* add statistics etc.
* Sentence formatting, remove excess spaces etc.