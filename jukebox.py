import sqlite3

try:
    import tkinter
except ImportError:  # Python2
    import Tkinter as tkinter
# sql connection
conn = sqlite3.connect('music.sqlite')

# subclasses base on the Listbox with added already scrollbar !INHERITANCE
class Scrollbox(tkinter.Listbox):
    # init method
    def __init__(self, window, **kwargs):
        # kinter.Listbox.__init__(self, window, **kwargs) # Python 2 version
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, comman=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan, **kwargs) #python2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, **kwargs)  # calling supper method
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


mainWindow = tkinter.Tk()
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

artistList = Scrollbox(mainWindow, background="lightblue")  # it can pass additional because of **kwargs
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# we are telling it to use yview opposite is xview
# artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
# artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
# artistList['yscrollcommand'] = artistScroll.set  # it will notify list box that to set method if anything
# is going to happen what should change the scroll like arrows  -> way of implement it in any widget what support it!

# ALBUM LISTBOX

albumLV = tkinter.Variable(mainWindow)
# tkinter variable in python are tracked so if anything is going to change the python is going to be notify
albumLV.set(("Choose an artist",))  # tuple
# albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)  # is variable is going to change it is going to be notify
albumList = Scrollbox(mainWindow, listvariable=albumLV)  # is variable is going to change it is going to be notify
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
# albumScroll.grid(row=1, column=1, sticky='nse', rowspan=2)
# albumList['yscrollcommand'] = albumScroll.set

# SONGS LISTBOX

songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))  # coma because again it is tuple
# songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList = Scrollbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# MAIN LOOP
testList = range(0, 100)
albumLV.set(tuple(testList))
# albumLV.set((1, 2, 3, 4, 5)) # You have to use set You can not assign them straight forward
mainWindow.mainloop()
print("closing db connection")
conn.close()
