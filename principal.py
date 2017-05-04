#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import time
from datetime import datetime, date, time, timedelta
import tkMessageBox
from clases.docente import Docente
from clases.asigna import Asigna
from ventanas import *


def modificarDocente():
    docente = Docente(entra_dni.get(), obraS(), entra_nom.get(), entra_ape.get(), entra_dire.get(), entra_tel.get(), entra_fecha.get())
    docente.modificarDocente()

"""Función Alta_Docente
* @param no recibe ningún parámetro
* @return devuelve abre una nueva ventana para agregar los datos y dar de alta al Docente
"""
def Alta_Docentes():
    Alta_Docente()
    
#Crea la ventana Principal
ventana = Tk()
ventana.title("Principal")
ventana.geometry("1000x500+200+200")


#hago cabezera y cuerpo de la ventana(Tops = titulo, centro = botones)
Tops=Frame(ventana, width=1000,height=100, bg="white",relief=SUNKEN)
Tops.pack(side=TOP)

centro=Frame(ventana, width=1000, height=650)
centro.pack(side=BOTTOM)

#Titulo
lblTitu=Label(Tops, font=("Time", 20),text="SISPER Software de Gestion de RR.HH",fg="black", bg="white").place(x=250, y=30)

#imagen titulo
imagenT=PhotoImage(file="imagenes/turq2.png")
lblImagen= Label(centro, image= imagenT).place(x=0, y=0)


#Botones
btonAlta=Button(centro, text="Nuevo Docente", font=("Time", 15), width=10, command=Alta_Docentes).place(x=150, y=80)
btonBaja=Button(centro, text="Baja Docente", font=("Time", 15), width=10).place(x=425, y=80)
btonModifica=Button(centro, text="Modificar-Datos", font=("Time", 15),command=modificarDocente, width=12).place(x=700, y=80)
btonLista=Button(centro, text="Listar", font=("Time", 15), width=12).place(x=700, y=190)
btonCalcula=Button(centro, text="Calcular Sueldo", font=("Time", 15), width=12).place(x=150, y=190)
btonVisualiza=Button(centro, text="Previsualizar", font=("Time", 15), width=10).place(x=425, y=190)
btonSalir= Button(centro, text="Salir", font=("Time", 15), width=10, command=ventana.destroy).place(x=800, y=350)

ventana.mainloop()
