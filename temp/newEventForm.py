import tkinter as tk
# from utilities import utilities

class newEventForm(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(
                height=600,
                width=1000, background='blue')

        # self.grid_rowconfigure(0, weight=0) # For row 0
        # self.grid_rowconfigure(1, weight=2) # For row 1
        # self.grid_columnconfigure(0, weight=1) # For column 0
        # self.grid_columnconfigure(1, weight=1) # For column 1 
        # #image declaring
        # self.calendarimg = tk.PhotoImage(file = utilities.getAssetPath("assets/calenderbuttonpic.png"))
        # self.neweventimg = tk.PhotoImage(file = utilities.getAssetPath("assets/neweventbuttonpic.png"))
        # self.aboutusimg = tk.PhotoImage(file = utilities.getAssetPath("assets/aboutusbuttonpic.png"))

        # def openFormFrame():
        #     print('openFormFrame')


        # self.calendarbutton = tk.Button(
        #     self,
        #     text = "Calendar",
        #     image = self.calendarimg,
        #     # command=openWindow,
        #     command=openFormFrame,
        #     width = 965, height = 1135, borderwidth=0,
        #     bg = 'white')
        # self.calendarbutton.grid(row = 0, column = 0, rowspan = 2)

        # self.neweventbutton = tk.Button(self, text = "New Event", width = 960, height = 575, borderwidth=0, image = self.neweventimg, bg = 'white')
        # self.neweventbutton.grid(row = 0, column = 1)

        # self.aboutusbutton = tk.Button(self, text = 'About Us', width = 957, height = 560, borderwidth=0, image = self.aboutusimg, bg = 'white')
        # self.aboutusbutton.grid(row = 1, column = 1)
