import sqlite3

try:
    import tkinter
except ImportError:  # Python2
    import Tkinter as tkinter

conn = sqlite3.connect('music.sqlite')

mainWindow = tkinter.TK()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1024x728')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

#  LABELS
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ARTISTS LISTBOX

artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# ALBUM LISTBOX

albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))  # tuple
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# SONGS LISTBOX

songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))  # coma because again it is tuple
songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')
