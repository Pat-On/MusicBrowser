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


class DataListBox(Scrollbox):
    """ DOC STRING SHOULD BE ADDED HERE ESPECIALLY IF CLASS IS REUSED :> """

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # Scrollbox.__init__(self, window, **kwargs) # python 2
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()  # we are using here cursor not connection
        self.table = table
        self.field = field

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self, link_value=None):
        if link_value:
            # populating by specific id
            sql = self.sql_select + " WHERE " + "artist" + "=?" + self.sql_sort
            print(sql)  # TODO: delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)  # TODO del
            self.cursor.execute(self.sql_select + self.sql_sort)

        #  clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

    # e.target in JS
    def on_select(self, event):
        print(self is event.widget)  # TODO - DELETE
        # lb = event.widget
        index = self.curselection()[0]
        value = self.get(index),  # this coma at the end is going to change it to tuple

        # !IMPORTANT He said very clearly that using the function as a method class is very good (obvious) but You have
        # to be very careful to not use global values, because then your classes are not going to work in different
        # programs and this is not going to be something what you are going to notice instantly
        # example conn
        # link_id = conn.execute(self.sql_select + "WHERE " + self.field + "=?", value).fetchone()[0]

        # get the artist ID from the database row
        link_id = self.cursor.execute(self.sql_select + "WHERE " + self.field + "=?", value).fetchone()[0]
        # unpacking - ...fetchone()[0]
        albumList.requery(link_id)

        # old solution
        # artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
        # alist = []
        # for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist=?
        # ORDER BY albums.name", artist_id):
        #     alist.append(row[0])
        # albumLV.set(tuple(alist))
        # songLV.set(("Choose an album",))


def get_songs(event):
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    # get the artist ID from the db row
    album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
    alist = []
    for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
        alist.append(x[0])
    songLV.set(tuple(alist))


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
artistList = DataListBox(mainWindow, conn, 'artists', 'name',
                         background="lightblue")  # it can pass additional because of **kwargs
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# population of the first Listbox
# for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
#     # print(artist)
#     artistList.insert(tkinter.END, artist[0])

artistList.requery()

# We can bind our function to virual events what may happen on the listbox
artistList.bind('<<ListboxSelect>>', get_albums)  # case sensitive if ListBox... it not working

# ALBUM LISTBOX
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))  # tuple

albumList = DataListBox(mainWindow, conn, "albums", "name",
                        sort_order=("name",))  # is variable is going to change it is going to be notify
albumList.requery(12)

albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

albumList.bind('<<ListboxSelect>>', get_songs)

# SONGS LISTBOX

songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))  # coma because again it is tuple
songList = DataListBox(mainWindow, conn, "songs", "title", sort_order=("track", "title"))
songList.requery()
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# MAIN LOOP
# testList = range(0, 100)
# albumLV.set(tuple(testList))
mainWindow.mainloop()
print("closing db connection")
conn.close()
