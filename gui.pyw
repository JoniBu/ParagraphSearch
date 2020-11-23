import tkinter as tk
import re
from tkinter import messagebox
from main import ParagraphSearchRefactor as pc
import os
import time
import threading


gui = tk.Tk()
gui.title("Paragraph searcher")
gui.geometry("475x350")
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
        self.t = threading.Thread(target=updateResults, args=(url.get(), depth.get(), re.sub("[^\w]", " ",  keywords.get()).split()))
    
    def start(self):
        plsWait(self)
        self.t.start()
        del(self.t)


    # def abort(self):
    #     self.t._stop()
    #     insertResults("Search stopped.")
    #     ready()
    #     print(keywords)
    #     del(self)



def plsWait(thread):
    results.config(foreground="red")
    insertResults("Searching, please wait...")
    #clearButton.config(text="Abort \n(unadvisable)", command=lambda :Thread.abort(thread), height=2, background="light coral")
    searchButton.config(state="disabled")
    clearButton.config(state='disabled')

def ready():
    results.config(foreground="black")
    clearButton.config(text="Clear fields", command=clear, background="gray92", height=1)
    searchButton.config(state="normal")

def insertResults(text):
    results.config(state="normal")
    results.delete(1.0, "end")
    results.insert(tk.END, text)
    results.config(state="disabled")
    

def updateList(results):
    for result in results:
        resultPages.insert("end", result.Page)

def clearList():
    resultPages.delete('0','end')


def updateResults(url, depth, keywords):
    updateResults.results = pc.ParagraphSearch(url, depth, keywords, True)
    clearList()
    updateList(updateResults.results)
    insertResults("Search complete.")
    ready()

def showSentences(self):
    idx = int(''.join(map(str, resultPages.curselection()))) 
    for sentence in updateResults.results[idx].Sentences:
        insertResults(sentence)

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

#page selection
resultPages = tk.Listbox(gui, width = 28, height= 14, selectmode="SINGLE")
resultPages.grid(row=4, column=0, columnspan=2, sticky="W")
resultPages.bind('<<ListboxSelect>>',showSentences)

#text area
results = tk.Text(gui, width=35, height=14, state="disabled")
results.grid(row=4,column=1, columnspan = 2,sticky="E")



gui.mainloop()

