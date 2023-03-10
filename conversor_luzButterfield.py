from tkinter import *
from tkinter import ttk


class conversor: 
    def __init__(self,raiz):

        raiz.title("pies en metros")

        self.pies=StringVar()
        self.metros=StringVar()

        mainframe= ttk.Frame (raiz, padding="3   3   12  12")
        mainframe.grid(column=0, row=0, sticky=(N, W,  E,S))

        pies_entry= ttk.Entry(mainframe, width=7, textvariable=self.pies)
        pies_entry.grid(column=2, row=1,sticky=(W, E))

        ttk.Label(mainframe,textvariable=self.metros).grid(column=2,row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid( column=3,row=3,sticky=W)

        ttk.Label(mainframe,text="pies").grid(column=3,row=1, sticky=(W))
        ttk.Label(mainframe,text="p}es equivalente a:").grid(column=1,row=2, sticky=(E))

        pies_entry.focus()
        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):
        try:
            valor=float (self.pies.get())
            self.metros.set(int(0.3048 *valor*10000.0+0.5)/10000.0)
        except ValueError:
            pass

raiz=Tk()
conversor(raiz)
raiz.mainloop()