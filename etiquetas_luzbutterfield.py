from tkinter import *
from tkinter import ttk

raiz=Tk()
etqTexto=ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()

imagen= PhotoImage(file="imagen.png")

etqImagen=ttk.Label(raiz, text="Etq Combinada", compound="center")
etqImagen.grid()
etqImagen['image']=imagen


raiz.mainloop()