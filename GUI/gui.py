import tkinter 
from tkinter import ttk

from GUI.main import Client

window = tkinter.Tk()
window.title('GUI')
window.geometry('1000x450')


tab_control = ttk.Notebook(window)

client = Client()
client.connect()

#Tab1 
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Process")



tv = ttk.Treeview(tab1, columns=(1,2,3,4,5,6,7,8,9), show="headings", height="8")
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

for process in client.status():
    tv.insert('', 'end', value=process)

def cambiarPrioridadProceso():
    if len(namePid.get()) > 0 and len(namePriority.get()) > 0:
        if int(namePriority.get()):
            client.setPriority(int(namePriority.get()), int(namePid.get()))

labelNamePid = ttk.Label(tab1, text = "Pid:")
labelNamePid.pack()

namePid = tkinter.StringVar()
namePidEntered = ttk.Entry(tab1, width = 15, textvariable = namePid)
namePidEntered.pack()

labelNamePriority = ttk.Label(tab1, text = "Priority (1 - 19):")
labelNamePriority.pack()

namePriority = tkinter.StringVar()
namePriorityEntered = ttk.Entry(tab1, width = 15, textvariable = namePriority)
namePriorityEntered.pack()

button7 = tkinter.Button(tab1, text="Cambiar prioridad proceso", command = cambiarPrioridadProceso)
button7.pack()

def terminarProceso():
    client.terminateProcess(int(namePid.get()))

button8 = tkinter.Button(tab1, text="Terminar proceso", command = terminarProceso)
button8.pack()

def actualizarTabla():
    for i in tv.get_children():
        tv.delete(i)

    for process in client.status():
        tv.insert('', 'end', value=process)

button9 = tkinter.Button(tab1, text="Actualizar tablas", command = actualizarTabla)
button9.pack()

def halt():
    client.halt()

button10 = tkinter.Button(tab1, text="Matar procesos", command = halt)
button10.pack()

def launch():
    client.launch()

button11 = tkinter.Button(tab1, text="Iniciar procesos", command = launch)
button11.pack()

#Tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="File Manager")


# Change FIle name
# =================
def changeFileName():
    if len(nameFileName.get()) > 0:
        client.setFileName(nameFileName.get())
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
        client.createDir(nameCreateDirectory.get())
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
        client.deleteDir(nameDeleteDirectory.get())
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
def readLogFile():
    logs = client.readLogFile()
    for log in logs:
        logsArea.insert(tkinter.END, log)

def stopProcess():
    client.stopProcess()


button4 = tkinter.Button(tab2, text="List logs", command = readLogFile)
button4.grid(column=3, row=0, padx=10, pady=8)

button6 = tkinter.Button(tab2, text="Stop process", command = stopProcess)
button6.grid(column=3, row=2, padx=10, pady=8)

logsArea = tkinter.Text(tab2, height=15, width=50)
logsArea.grid(column=0, row=5, columnspan=2, rowspan=2, padx=10, pady=10)


#Complete config tabs
tab_control.pack(expand=1, fill='both') 

window.mainloop()