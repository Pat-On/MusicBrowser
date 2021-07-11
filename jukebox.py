import sqlite3
try:
    import _tkinter
except ImportError: #Python2
    import Tkinter as tkinter

conn = sqlite3.connect('music.sqlite')