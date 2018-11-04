import numpy as np
from tkinter import*
from tkinter import ttk


root = Tk()
root.title("Two set of Linear Equations")

mainframe = ttk.Frame(root, padding="55 55 55 55")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=5)
root.rowconfigure(0, weight=5)

x1 = StringVar()
y1 = StringVar()
ans1 = StringVar()
x2 = StringVar()
y2 = StringVar()
ans2 = StringVar()

# Equation1 input_boxes
x1_entry = ttk.Entry(mainframe, width=5, textvariable=x1)
x1_entry.grid(column=1, row=1, sticky=(W, E))

y1_entry = ttk.Entry(mainframe, width=5, textvariable=y1)
y1_entry.grid(column=3, row=1, sticky=(W, E))

ans1_entry = ttk.Entry(mainframe, width=5, textvariable=ans1)
ans1_entry.grid(column=6, row=1, sticky=(W, E))

# Equation2 input_boxes
x2_entry = ttk.Entry(mainframe, width=5, textvariable=x2)
x2_entry.grid(column=1, row=3, sticky=(W, E))

y2_entry = ttk.Entry(mainframe, width=5, textvariable=y2)
y2_entry.grid(column=3, row=3, sticky=(W, E))

ans2_entry = ttk.Entry(mainframe, width=5, textvariable=ans2)
ans2_entry.grid(column=6, row=3, sticky=(W, E))

# Static variables
ttk.Label(mainframe, text="x").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="y").grid(column=4, row=1, sticky=W)
ttk.Label(mainframe, text="=").grid(column=5, row=1, sticky=W)
ttk.Label(mainframe, text="x").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="y").grid(column=4, row=3, sticky=W)
ttk.Label(mainframe, text="=").grid(column=5, row=3, sticky=W)

ttk.Button(mainframe, text="Calculate").grid(column=8, row=1, sticky=W)
ttk.Button(mainframe, text="Exit", command=root.destroy).grid(column=8, row=3)

root.mainloop()
