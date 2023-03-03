from tkinter import *
from tkinter import ttk

raiz=Tk()
boton=ttk.Label(raiz, text="Botón solo texto")
boton.grid()

imagen= PhotoImage(file="imagen.png")

btnImagen=ttk.Button(raiz)
btnImagen.grid()
btnImagen['image']=imagen

btnCombinada=ttk.Button(raiz, text="Bontón combinado", compound="bottom")
btnImagen.grid()
btnImagen['image']=imagen

chkBoton=ttk.Checkbutton(raiz, text= "Opcion 1")
chkBoton.grid()

raiz.mainloop()