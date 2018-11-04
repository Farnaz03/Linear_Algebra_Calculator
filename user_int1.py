import numpy as np
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Linear Calculator")
mainframe = ttk.Frame(root, padding="55 55 55 55")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="What do you want to do?").grid(column=1, row=1)
ttk.Button(mainframe, text="Two Set Linear Equations").grid(column=1, row=2)
ttk.Button(mainframe, text="Three Set Linear Equations").grid(column=1, row=3)
ttk.Button(mainframe, text="Exit", command=root.destroy).grid(column=1, row=4)


root.mainloop()
