import tkinter as tk
from utilities import utilities
# import newEventForm class
from newEventForm import newEventForm
from config.config import *
import time

class calendarPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # configure row col
        self.grid_rowconfigure(0, weight=0) # For row 0
        self.grid_rowconfigure(1, weight=2) # For row 1
        self.grid_columnconfigure(0, weight=1) # For column 0
        self.grid_columnconfigure(1, weight=1) # For column 1 
        #image declaring
        self.calendarimg = tk.PhotoImage(file = utilities.getAssetPath("assets/calenderbuttonpic.png"))
        self.neweventimg = tk.PhotoImage(file = utilities.getAssetPath("assets/neweventbuttonpic.png"))
        self.aboutusimg = tk.PhotoImage(file = utilities.getAssetPath("assets/aboutusbuttonpic.png"))
        # func def
        def openFormFrame():
            print('openFormFrame')
        def openNewEventForm():
            print('openNewEventForm')
            # for non popup window mode
            # self.newEventForm = newEventForm(self).place(
            #     in_=self, anchor="c", relx=.5, rely=.5)
            self.newEventForm = newEventForm(self).place(
                in_=self, anchor="c", relx=.5, rely=.5, relheight=1, relwidth=1)
            

        # create buttons
        self.calendarbutton = tk.Button(
            self,
            text = "Calendar",
            image = self.calendarimg,
            command=openFormFrame,
            width = 965, height = 1135, borderwidth=0,
            bg = ROOT_BG_COLOR)
        self.neweventbutton = tk.Button(
            self,
            text = "New Event",
            image = self.neweventimg,
            width = 960, height = 575, borderwidth=0,
            command=openNewEventForm,
            bg = ROOT_BG_COLOR)
        self.aboutusbutton = tk.Button(
            self,
            text = 'About Us',
            image = self.aboutusimg,
            width = 957, height = 560, borderwidth=0,
            command=openFormFrame,
            bg = ROOT_BG_COLOR)

        # positioning
        self.calendarbutton.grid(row = 0, column = 0, rowspan = 2)
        self.neweventbutton.grid(row = 0, column = 1)
        self.aboutusbutton.grid(row = 1, column = 1)
