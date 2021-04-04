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


# Change FIle name
# =================
def changeFileName():
    if len(nameFileName.get()) > 0:
        labelFileName.configure(text= 'New File Name: \n' + nameFileName.get())
 
labelFileName = ttk.Label(tab2, text = "File Name: Logs-1.log")
labelFileName.grid(column = 0, row = 0, pady=8)
 
nameFileName = tkinter.StringVar()
nameFileNameEntered = ttk.Entry(tab2, width = 15, textvariable = nameFileName)
nameFileNameEntered.grid(column = 0, row = 1)

button1 = tkinter.Button(tab2, text="Change File Name", command = changeFileName)
button1.grid(column=0, row=2, padx=8, pady=8)


# Create Directory
# =================
def createDirectory():
    if len(nameCreateDirectory.get()) > 0:
        labelCreateDirectory.configure(text= 'Directory ' + nameCreateDirectory.get() + '\n created')
 
labelCreateDirectory = ttk.Label(tab2, text = "Create new directory")
labelCreateDirectory.grid(column = 1, row = 0, pady=8)
 
nameCreateDirectory = tkinter.StringVar()
nameCreateDirectoryEntered = ttk.Entry(tab2, width = 15, textvariable = nameCreateDirectory)
nameCreateDirectoryEntered.grid(column = 1, row = 1)

button2 = tkinter.Button(tab2, text="Create directory", command = createDirectory)
button2.grid(column=1, row=2, padx=10, pady=8)

# Delete Directory
# =================
def deleteDirectory():
    if len(nameDeleteDirectory.get()) > 0:
        labelDeleteDirectory.configure(text= 'Directory ' + nameDeleteDirectory.get() + '\n deleted')
 
labelDeleteDirectory = ttk.Label(tab2, text = "Delete directory")
labelDeleteDirectory.grid(column = 2, row = 0, pady=8)
 
nameDeleteDirectory = tkinter.StringVar()
nameDeleteDirectoryEntered = ttk.Entry(tab2, width = 15, textvariable = nameDeleteDirectory)
nameDeleteDirectoryEntered.grid(column = 2, row = 1)

button3 = tkinter.Button(tab2, text="Delete directory", command = deleteDirectory)
button3.grid(column=2, row=2, padx=10, pady=8)

# LS 
# =================
def ListLogs():
    logsArea1.insert(tkinter.END, 'List logs \n')

def ListLogsDirectory():
    logsArea2.insert(tkinter.END, 'List logs Directory \n')


button4 = tkinter.Button(tab2, text="List logs", command = ListLogs)
button4.grid(column=3, row=0, padx=10, pady=8)

button5 = tkinter.Button(tab2, text="List directory", command = ListLogsDirectory)
button5.grid(column=3, row=1, padx=10, pady=8)

logsArea1 = tkinter.Text(tab2, height=15, width=50)
logsArea1.grid(column=0, row=5, columnspan=2, rowspan=2, padx=10, pady=10)

logsArea2 = tkinter.Text(tab2, height=15, width=50)
logsArea2.grid(column=2, row=5, columnspan=2, rowspan=2, padx=10, pady=10)


#Complete config tabs
tab_control.pack(expand=1, fill='both') 

window.mainloop()