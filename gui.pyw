import tkinter as tk
import re
from tkinter import messagebox
import ParagraphSearch as pc
import os
import time
import threading



#TODO fix stopping abort/thread stop
#TODO add scrollbar https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget
#TODO fix multiple keywords
#TODO split search keywords to two columns, one for pages one for found paragraphs


gui = tk.Tk()
gui.title("Paragraph searcher")
gui.geometry("500x345")
gui.resizable(width=False, height=False)
fontsize = "none 11"


#parameters
url = tk.StringVar(gui)
keywords = tk.StringVar(gui)
depthOptions = [0,1,2,3,4,5]
depth = tk.IntVar(gui)
depth.set(depthOptions[1])


#Django validation regex // https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
urlValidityRegex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

class Thread:
    def __init__(self):
        self.t = threading.Thread(target=updateResults, args=(url.get(), depth.get(), [words for segments in keywords.get() for words in segments.split()]))
    
    def start(self):
        plsWait(self)
        self.t.start()
        del(self.t)


    def abort(self):
        self.t._stop() # not actually stopped..
        insertResults("Search stopped.")
        ready()
        del(self)



def plsWait(thread):
    results.config(foreground="red")
    insertResults("Searching, please wait...")
    clearButton.config(text="Abort \n(unadvisable)", command=lambda :Thread.abort(thread), height=2, background="light coral")
    searchButton.config(state="disabled")

def ready():
    results.config(foreground="black")
    clearButton.config(text="Clear fields", command=clear, background="gray92", height=1)
    searchButton.config(state="normal")

def insertResults(text):
    results.config(state="normal")
    results.delete(1.0, "end")
    results.insert(tk.END, text)
    results.config(state="disabled")

def readFile(fullPath):
    while not os.path.exists(fullPath):
            time.sleep(1)
    with open(fullPath, 'r', encoding='utf-8') as f:
        ready()
        insertResults(f.read())

def updateResults(url, depth, keywords):
    filename = pc.ParagraphSearch(url, depth, keywords)
    fullPath = os.path.join('./FoundSentences',filename)
    readFile(fullPath)



def search():
    pUrl = url.get()
    pKeywords = keywords.get()
    if pUrl == "" or pKeywords == '':
        messagebox.showinfo("Error", "Missing parameters.")
    elif re.match(urlValidityRegex, pUrl) is None:
        messagebox.showinfo("Error", "Invalid url. Please enter full URL.")
    else:
        #thread = threading.Thread(target=updateResults, args=(url.get(), depth.get(), keywords.get()))
        thread = Thread()
        thread.start()


def clear():
    urlEntry.delete(0,"end")
    keywordEntry.delete(0, "end")
    results.delete(1.0, "end")


#URL
tk.Label(gui, text="Start URL" , fg="black", font=fontsize).grid(row=0, column=0, sticky="W")
urlEntry = tk.Entry(gui, width=61, bg="white", textvariable=url)
urlEntry.grid(row=0, column=1, sticky="W")

#keywords
tk.Label(gui, text="Keywords", fg="black", font=fontsize).grid(row=1, column=0, sticky="W")
keywordEntry = tk.Entry(gui, width=61, bg="white", textvariable=keywords)
keywordEntry.grid(row=1, column=1, sticky="W")

#depth
tk.Label(gui, text="Search depth", fg="black", font=fontsize).grid(row=2, column=0, sticky="W")
depthMenu = tk.OptionMenu(gui, depth, *depthOptions)
depthMenu.grid(row=2, column=1, sticky="W")

#button
clearButton = tk.Button(gui, text="Clear fields", command=clear)
clearButton.grid(row=3, column=0, sticky="W", pady=5, padx=16)
searchButton = tk.Button(gui, text="Search", command=search)
searchButton.grid(row=3, column=1, sticky="E", pady=5, padx=16)

#text area
results = tk.Text(gui, width=62, height=14, state="disabled")
results.grid(row=4,column=0, columnspan = 2,sticky="W")



gui.mainloop()

