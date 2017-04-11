#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

from clases.docente import Docente
from datetime import datetime, date, time, timedelta
import calendar

#Funciones de los botones
"""Funcion que calcula el cod_Antiguedad"""
def antiguedad():
    fechActual = datetime.now()
    formato = "%d/%m/%Y"
    fecha_ingreso = entrada_fechaIngreso.get()
    fecha_ingreso = datetime.strptime(fecha_ingreso, formato)
    diferencia = (fechActual - fecha_ingreso)
    resultado = (diferencia/365)
    anios = resultado.days
    if anios > 24:
        return 25
    else:
        return anios

"""Funcion que calcula el cod_ObraSocial"""
def sel():
    selection = codObraSocial.get()
    return selection

def agregarDatos():
    docente = Docente(entrada_dni.get(),antiguedad(),sel(), entrada_nombre.get(), entrada_apellido.get(), entrada_direccion.get(), entrada_telefono.get(), entrada_fechaIngreso.get())
    docente.altaDocente()





#ventana principal
ventana_pcipal = Tk()
frame = Frame(ventana_pcipal)
ventana_pcipal.title("Ventana Principal")
    #ancho, alto, izquierda-derecha, arriba-abajo
ventana_pcipal.geometry("1000x610+250+100")
ventana_pcipal.maxsize(1008, 610)

#Titulo principal
variable = Label(ventana_pcipal, text="Agregar Docente", fg="BLACK", font=("Purisa", 20),background="brown",relief=SUNKEN).place(x=250, y=10)

#Ingresar el nombre
nombre = Label(ventana_pcipal, text="Nombre:",  font=("Arial", 16),relief=SUNKEN).place(x=15, y=100)
global entrada_nombre
entrada_nombre = StringVar()
campo_nombre = Entry(ventana_pcipal,highlightcolor="Red", textvariable=entrada_nombre,font=("Arial", 16),width=25).place(x=175, y=100)

#Ingresar el apellido
apellido = Label(ventana_pcipal, text="Apellido:",  font=("Arial", 16),relief=SUNKEN).place(x=15, y=150)
global entrada_apellido
entrada_apellido = StringVar()
campo_apellido = Entry(ventana_pcipal,highlightcolor="Red", textvariable=entrada_apellido,font=("Arial", 16),width=25).place(x=175, y=150)

#Ingresar el dni
dni = Label(ventana_pcipal, text="Dni:",  font=("Arial", 16),relief=SUNKEN).place(x=15, y=200)
global entrada_dni
entrada_dni = StringVar()
campo_dni = Entry(ventana_pcipal, textvariable=entrada_dni,font=("Arial", 16),width=25).place(x=175, y=200)

#Ingresar direccion
direccion = Label(ventana_pcipal, text="Direccion:",  font=("Arial", 16),relief=SUNKEN).place(x=15, y=250)
global entrada_direccion
entrada_direccion = StringVar()
campo_direccion = Entry(ventana_pcipal, textvariable=entrada_direccion,font=("Arial", 16),width=25).place(x=175, y=250)

#Ingresar telefono
telefono = Label(ventana_pcipal, text="telefono:",  font=("Arial", 16),relief=SUNKEN).place(x=15, y=300)
global entrada_telefono
entrada_telefono = StringVar()
campo_telefono = Entry(ventana_pcipal, textvariable=entrada_telefono,font=("Arial", 16),width=25).place(x=175, y=300)

#Ingresar el fechaIngreso
fechaIngreso = Label(ventana_pcipal, text="fecha Ingreso:",  font=("Arial", 16),relief=SUNKEN).place(x=15, y=350)
global entrada_fechaIngreso
entrada_fechaIngreso = StringVar()
campo_fechaIngreso = Entry(ventana_pcipal, textvariable=entrada_fechaIngreso,font=("Arial", 16),width=25).place(x=175, y=350)

#obra Social
obraSocial = Label(ventana_pcipal, text="Obra Social:",  font=("Arial", 16),relief=SUNKEN).place(x=600, y=50)
codObraSocial = IntVar()
R1 = Radiobutton(ventana_pcipal, text="Asimira", font=("Arial", 16),relief=SUNKEN, variable=codObraSocial, value=1,command=sel).place(x= 600,y=100)
R2 = Radiobutton(ventana_pcipal, text="Medisur",  font=("Arial", 16),relief=SUNKEN, variable=codObraSocial, value=2,command=sel).place(x= 600,y=150)
R3 = Radiobutton(ventana_pcipal, text="SPS Salud",  font=("Arial", 16),relief=SUNKEN, variable=codObraSocial, value=3,command=sel).place(x= 600,y=200)
R3 = Radiobutton(ventana_pcipal, text="Osecac",  font=("Arial", 16),relief=SUNKEN, variable=codObraSocial, value=4,command=sel).place(x= 600,y=250)
R3 = Radiobutton(ventana_pcipal, text="Ioscor",  font=("Arial", 16),relief=SUNKEN, variable=codObraSocial, value=5,command=sel).place(x= 600,y=300)

#Boton Agregar Docente
BtnAgregarDatos = Button(ventana_pcipal, text="Agregar Datos", font=("Purisa", 14), relief=RIDGE , activebackground ="brown", width=19, command = agregarDatos).place(x=390, y=395)

#Boton salir
BtnSalir = Button(ventana_pcipal, text="Salir", font=("Arial", 16), relief=RIDGE,  command = ventana_pcipal.destroy, width=12).place(x=430, y=520)

ventana_pcipal.mainloop()
