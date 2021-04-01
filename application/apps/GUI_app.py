from tkinter import *
from tkinter import ttk
import os


class App:

    def aplication(self):

        # ventana principal
        ventana = Tk()
        ventana.title("An App")
        ventana.configure(bg='#252526')
        ventana.resizable(False, False)
        #self.img = PhotoImage(file='icon.png')
        #self.ventana.Tk.call('wm', 'iconphoto', ventana._w, img)

        # canvas
        canvas = Canvas(ventana)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = ttk.Scrollbar(
            ventana, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set,
                         bg='#252526', relief='flat')
        canvas.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox('all')))

        # label titulo
        titulo = Label(canvas, text="PID:")
        titulo.grid(row=0, column=0, padx=30, pady=30)
        titulo.config(bg='#333333', fg='#5cb1e7', highlightbackground='#5cb1e7',
                      relief='flat', font='Courier 18 bold')

        # pid de la aplicacion
        numero_pid = Label(canvas, text=os.getpid())
        numero_pid.grid(row=1, column=0, padx=30, pady=30)
        numero_pid.config(bg='#333333', fg='#5cb1e7',
                          highlightbackground='#5cb1e7', relief='flat', font='Courier 18 bold')

        #ventana.iconbitmap('logoapp.ico')
        ventana.mainloop()


if __name__ == "__main__":
    App().aplication()
