# Paragraph search

Really simple webscraper, which searches for sentences inside paragraph tags, based on given keywords.

## Running the code

Currently this can be used on:
* command line with search.py (missing support for multiple keywords, needs work). Example:
`python3 search.py https://github.com/ 1 code`
* and from simple GUi, `gui.pyw`. Currently supports multiple words.
![alt text](sample.png "Gui")



## TODO
* Filter out pages where nothing was found - probably needs sorting
* Make search incasesensitive
* fix stopping abort (terminating thread)
* add scrollbar https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget
* add statistics etc.
* Sentence formatting, remove excess spaces etc.