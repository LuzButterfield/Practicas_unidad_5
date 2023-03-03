from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Frames")

datos = LabelFrame(root, text="Buscador")
datos.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

Label(datos,text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="N,W")
capnombre = Entry(datos).grid(row=0, column=1, padx=10, pady=10, sticky="W,E")

Label(datos,text="A. Paterno:").grid(row=1, column=0, padx=10, pady=10, sticky="N,W")
capapat = Entry(datos).grid(row=1, column=1, padx=10, pady=10)

Label(datos,text="A. Materno:").grid(row=2, column=0, padx=10, pady=10, sticky="N,W")
capamat = Entry(datos).grid(row=2, column=1, padx=10, pady=10)

Label(datos,text="Correo:").grid(row=3, column=0, padx=10, pady=10, sticky="N,W")
capcorreo = Entry(datos).grid(row=3, column=1, padx=10, pady=10)

Label(datos,text="Movil:").grid(row=4, column=0, padx=10, pady=10, sticky="N,W")
capmovil = Entry(datos).grid(row=4, column=1, padx=10, pady=10)

aficiones = LabelFrame(root, text="Aficiones")
aficiones.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

opc1=Checkbutton(aficiones, text="Leer").grid(row=0, column=0, padx=10, pady=10)
opc2=Checkbutton(aficiones, text="Música").grid(row=0, column=1, padx=10, pady=10)
opc3=Checkbutton(aficiones, text="Videojuegos").grid(row=0, column=2, pady=10)


opciones = LabelFrame(root, text="Puesto")
opciones.grid(row=0, column=2, padx=10, pady=10)
opcion=1

r1=Radiobutton(opciones, text="Estudiante", variable=opcion, value=1).grid(row=0, column=0, padx=10, pady=10)
r2=Radiobutton(opciones, text="Empleado", variable=opcion, value=2).grid(row=1, column=0, padx=10, pady=10)
r3=Radiobutton(opciones, text="Desempleado", variable=opcion, value=3).grid(row=2, column=0, padx=10, pady=10)

guardar=Button(root,text="Guardar").grid(row=2, column=0, padx=10, pady=10)
cancelar=Button(root,text="Cancelar").grid(row=2, column=1, padx=10, pady=10, sticky="E")

estado = StringVar()
comboEstado = LabelFrame(root, text="Estados")
comboEstado.grid(row=1, column=3, padx=10, pady=10, columnspan=2)

comboEstados=ttk.Combobox(root, textvariable=estado)
comboEstados.grid(row=1, column=2, padx=10, pady=10)
comboEstados['values']= ("Aguascalientes",
                            "BC",
                            "BCS",
                            "Sonora",
                            "Sinaloa",
                            "Nayarit",
                            "Chichuahua",
                            "Coahuila",
                            "Nuevo León",
                            "Tamaulipas",
                            "San Luis Potosí",
                            "Zacatecas",
                            "Durango",
                            "Jalisco",
                            "Guanajuato",
                            "Colima",
                            "Michoacan",
                            "Guerrero",
                            "México",
                            "Queretaro",
                            "Hidalgo",
                            "Morelos",
                            "Tlaxcala",
                            "Puebla",
                            "Oaxaca",
                            "Chiapas",
                            "Tabasco",
                            "Campeche",
                            "Yucatán",
                            "Quintana Roo")




mainloop()