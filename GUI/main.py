# TODO: Add info to install tkinter in setup.py
# python -m pip install tk

import tkinter 
from tkinter import ttk

window = tkinter.Tk()
window.title('GUI')
window.geometry('500x350')


tab_control = ttk.Notebook(window)

#Tab1 
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Process")

lbl1 = tkinter.Label(tab1, text= 'Process')

lbl1.grid(column=0, row=0)

#Tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="File Manager")

lbl1 = tkinter.Label(tab2, text= 'File Manager')
lbl1.grid(column=0, row=0)

#Complete config tabs
tab_control.pack(expand=1, fill='both') 

window.mainloop()