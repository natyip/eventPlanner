# Use Tkinter for python 2, tkinter for python 3
import calendar
import tkinter as tk
from config.config import *
# import calendarPage class
from calendarPage import calendarPage


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        print(self,'\n', parent,'\n', *args,'\n', **kwargs)
        self.calendarPage = calendarPage(self).pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    # setup and configure root
    root = tk.Tk()
    root.title(ROOT_TITLE)
    root.attributes('-fullscreen', True) if ROOT_FULLSCREEN else root.geometry(ROOT_WINDOW_SIZE)
    # create main frame
    name = 'wanlin'
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
