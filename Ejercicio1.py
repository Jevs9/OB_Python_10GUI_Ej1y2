import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)

label1 = tkinter.Label(window, text="Seleccione una de las opciones: ", bg="gray", fg="white")
label1.grid(column=0, row=0)

seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="OPCION 1", value='0', variable=seleccionado)
r2 = ttk.Radiobutton(window, text="OPCION 2", value='1', variable=seleccionado)
r3 = ttk.Radiobutton(window, text="OPCION 3", value='2', variable=seleccionado)

r1.grid(column=0,row=1)
r2.grid(column = 0, row=2)
r3.grid(column=0, row=3)

def reiniciar(event):
    seleccionado.set(None)

button1 = ttk.Button(window, text="Reiniciar")
button1.grid(column=0, row=4)
button1.bind('<Button-1>', reiniciar)

window.mainloop()