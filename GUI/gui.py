# TODO: Add info to install tkinter in setup.py
# python -m pip install tk

import tkinter 
from tkinter import ttk

window = tkinter.Tk()
window.title('GUI')
window.geometry('1000x450')


tab_control = ttk.Notebook(window)

#Tab1 
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Process")

tv = ttk.Treeview(tab1, columns=(1,2,3,4,5,6,7,8,9), show="headings", height="5")
tv.pack()

tv.heading(1, text="Pid")
tv.heading(2, text="Name")
tv.heading(3, text="Create time")
tv.heading(4, text="Cores")
tv.heading(5, text="CPU usage")
tv.heading(6, text="Status")
tv.heading(7, text="Nice")
tv.heading(8, text="Memory Usage")
tv.heading(9, text="Username")

tv.insert('', 'end', value=(
    "hola",
    "mundo"
))

#Tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="File Manager")

lbl1 = tkinter.Label(tab2, text= 'File Manager')
lbl1.grid(column=0, row=0)

#Complete config tabs
tab_control.pack(expand=1, fill='both') 

window.mainloop()