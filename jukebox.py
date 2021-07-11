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


# e.target in JS
def get_albums(event):
    lb = event.widget
    index = lb.curselection()[0]
    artist_name = lb.get(index),  # this coma at the end is going to change it to tuple

    # get the artist ID from the database row
    artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
    alist = []
    for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist=? ORDER BY albums.name", artist_id):
        alist.append(row[0])
    albumLV.set(tuple(alist))


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

# population of the first Listbox
for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    # print(artist)
    artistList.insert(tkinter.END, artist[0])

# We can bind our function to virual events what may happen on the listbox
artistList.bind('<<ListboxSelect>>', get_albums)  # case sensitive if ListBox... it not working

# ALBUM LISTBOX
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))  # tuple
albumList = Scrollbox(mainWindow, listvariable=albumLV)  # is variable is going to change it is going to be notify
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# SONGS LISTBOX

songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))  # coma because again it is tuple
songList = Scrollbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# MAIN LOOP
# testList = range(0, 100)
# albumLV.set(tuple(testList))
mainWindow.mainloop()
print("closing db connection")
conn.close()
