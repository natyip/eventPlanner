import tkinter as tk
from tkinter import ttk
from config.config import *
# from utilities import utilities


HEADER_FRAME_HEIGHT=150
BODY_FRAME_HEIGHT=600

class newEventForm(tk.Frame):
    def prevPage(self):
        self.destroy()

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # for non popup window mode
        # self.configure(height=500, width=600, background='blue')
        self.configure(background=ROOT_BG_COLOR)

        # def prevPage():
        #     self.destroy()

        header = tk.Frame(
            self, 
            height=HEADER_FRAME_HEIGHT,
            bg=ROOT_BG_COLOR,
            highlightbackground='red', 
            highlightcolor='red', 
            highlightthickness=2)
        header.pack(side='top', fill='x')
        # disable inner elements changing size of the frame
        header.configure(height=header["height"],width=header["width"])
        header.pack_propagate(0)
        title =  tk.Label(
            header,
            text='CREATE NEW EVENT',
            bg=ROOT_BG_COLOR,
            fg='black',
            font=("Arial", 58))
        title.pack(side='bottom')
        backBtn = tk.Button(
            header,
            text='BACK',
            bg=ROOT_BG_COLOR,
            fg='blue',
            font=("Arial", 42),
            command=self.prevPage)
        backBtn.place(anchor='nw', x=20, y=20)

        body = tk.Frame(
            self, 
            height=BODY_FRAME_HEIGHT,
            bg=ROOT_BG_COLOR,
            highlightbackground='blue', 
            highlightcolor='blue', 
            highlightthickness=2)

        body.pack(side='top', pady=(10,0))
        body.configure(width=800)
        body.grid_propagate(0)
        # disable inner elements changing size of the frame
        # body.configure(height=body["height"],width=body["width"])
        # configure row col
        body.grid_columnconfigure(0, weight=1) # For column 0
        body.grid_columnconfigure(1, weight=1) # For column 1 
        body.grid_columnconfigure(2, weight=1) # For column 2
        body.grid_columnconfigure(3, weight=1) # For column 3 
        # ROW 0
        nameLable = tk.Label(body, text="Event Name: ",
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22))
        nameEntry = tk.Entry(body,
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        nameLable.grid(row=0,column=0, sticky='w', pady=5)
        nameEntry.grid(row=0,column=1, columnspan=3, sticky='we', pady=5)
        # ROW 1
        isMulitDay = tk.Checkbutton(body,
            text="Multi-day event",
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22))
        isMulitDay.grid(row=1, column=1, columnspan=3, sticky='w', pady=5)
        # ROW 2
        date1Lable = tk.Label(body, text="Start Date: ",
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22))
        date1Entry = tk.Entry(body,
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        date2Lable = tk.Label(body, text="End Date: ",
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22))
        date2Entry = tk.Entry(body,
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        date1Lable.grid(row=2,column=0, sticky='w', pady=5)
        date1Entry.grid(row=2,column=1, sticky='we', pady=5)
        date2Lable.grid(row=2,column=2, sticky='w', pady=5)
        date2Entry.grid(row=2,column=3, sticky='we', pady=5)
        # ROW 3
        descLable = tk.Label(body, text="Description: ",
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22))
        descEntry = tk.Entry(body,
            bg=ROOT_BG_COLOR,
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        descLable.grid(row=3,column=0, sticky='w', pady=5)
        descEntry.grid(row=3,column=1, columnspan=3, sticky='we', pady=5)

        
        # save button
        saveBtn = tk.Button(
            self,
            text='SAVE',
            bg=ROOT_BG_COLOR,
            fg='orange',
            font=("Arial", 42),
            command=self.prevPage)
        saveBtn.place(relx=1,rely=1, x=-30, y=-20, anchor='se')