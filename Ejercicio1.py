import tkinter
from tkinter import ttk

window = tkinter.Tk()

def seleccionar(event):
    monitor.config(text="{}".format(seleccionado.get()))

label1 = tkinter.Label(window, text="Seleccione una de las opciones: ", bg="gray", fg="white")
label1.grid(column=0, row=0)


seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="OPCION 1", value='0', variable=seleccionado, command=seleccionar)
r1.grid(column=0, row=1)
r2 = ttk.Radiobutton(window, text="OPCION 2", value='1', variable=seleccionado, command=seleccionar)
r2.grid(column=0, row=2)
r3 = ttk.Radiobutton(window, text="OPCION 3", value='2', variable=seleccionado, command=seleccionar)
r3.grid(column=0, row=3)

monitor = tkinter.Label(window)
monitor.grid(column=0, row=4)

def reiniciar(event):
    seleccionado.set(None)
    monitor.config()

button1 = ttk.Button(window, text="Reiniciar")
button1.grid(column=0, row=5)
button1.bind('<Button-1>', reiniciar)

window.mainloop()