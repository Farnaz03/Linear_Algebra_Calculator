import numpy as np
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Linear Calculator")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="What do you want to do?").grid(column=1, row=1)
ttk.Button(mainframe, text="Three Set Linear Equations").grid(column=1, row=3)
ttk.Button(mainframe, text="Exit", command=root.destroy).grid(column=1, row=4)


def callback(x, x_2, y, y_2, x_dep, y_dep):
    root2 = Tk()
    root2.title("Two Set Linear Equations")

    mainframe2 = ttk.Frame(root, padding="3 3 12 12")
    mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Takes in input and outputs given response
    a = np.array([[x, y], [x_2, y_2]])  # Takes in x and y coefficients
    b = np.array([x_dep, y_dep])  # Takes in x and y dependents

    j = np.linalg.solve(a, b)  # Solves the Equation

    value_x = int(j[0])
    value_y = int(j[1])

    # Static variables
    ttk.Label(mainframe, text="x").grid(column=2, row=1, sticky=W)
    ttk.Label(mainframe, text="y").grid(column=4, row=1, sticky=W)
    ttk.Label(mainframe, text="=").grid(column=5, row=1, sticky=W)
    ttk.Label(mainframe, text="x").grid(column=2, row=2, sticky=W)
    ttk.Label(mainframe, text="y").grid(column=4, row=2, sticky=W)
    ttk.Label(mainframe, text="=").grid(column=5, row=2, sticky=W)

    # print("Your x value is:", value_x)
    # print("Your y value is:", value_y)
    ttk.Button(mainframe, text="Two Set Linear Equations", command=callback(x, x_2, y, y_2, x_dep, y_dep)).grid(column=1, row=2)

    return value_x, value_y


def second_set(x, x_2, x_3, y, y_2, y_3, z, z_2, z_3, x_dep, y_dep, z_dep):
    a = np.array([[x, y, z], [x_2, y_2, z_2], [x_3, y_3, z_3]])
    b = np.array([x_dep, y_dep, z_dep])

    j = np.linalg.solve(a, b)  # Solves the Equation

    value_x = int(j[0])
    value_y = int(j[1])
    value_z = int(j[2])

    # print("Your x value is:", value_x)
    # print("Your y value is:", value_y)
    # print("Your z value is:", value_z)

    return value_x, value_y, value_z


root.mainloop()
