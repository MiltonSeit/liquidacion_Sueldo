#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from datetime import *
from clases.recibo import Recibo
from clases.asigna import Asigna
import MySQLdb
import mysql.connector
import decimal
import os

def buscarDatos():
    asignar = Asigna(entra_dni.get())
    asignar.buscarCargos()

def mostrarRecibo(numero):
    print numero

def mostrarLabel():
    y = 110
    for i in range(1,7):
        lblNombre= Label(medio,text="Milton Seitzinger ",background="gray", font=("Time", 15)).place(x=10, y=y)
        lblCargo= Label(medio,text="Jefe de preceptores de primaria ",background="gray", font=("Time", 15)).place(x=195, y=y)
        lblEscuela= Label(medio,text="Isabel Estela Vera ",background="gray", font=("Time", 15)).place(x=530, y=y)
        lblPeriodo= Label(medio,text="6/2017 ",background="gray", font=("Time", 15)).place(x=725, y=y)
        BotonRecibo = Button(medio, text="Visualizar", font=("Arial", 14), activebackground ="red", width=10, command=lambda:mostrarRecibo(i)).place(x=820, y=y)

        y = y +50

"""
VENTANA DE PREVISUALIZAR CARGO
"""
def ventanaPrevisualizar():

    	punto= Toplevel()
    	punto.title("Previsualizar Cargo")
    	punto.geometry("1000x500+200+200")

        global medio
    	medio=Frame(punto, width=1000, height=650)
    	medio.pack(side=BOTTOM)

    	imagen1=PhotoImage(file="imagenes/turq2.png")
    	lblImagen= Label(medio, image= imagen1).place(x=0, y=0)

    	#etiquetas
        lblDni= Label(medio,text="PERIODO: ",background="gray", font=("Time", 15)).place(x=30, y=30)
        lblDni= Label(medio,text="DNI: ",background="gray", font=("Time", 15)).place(x=380, y=30)
        lblSeparar= Label(medio,text="------------------------------------------------------------------------------------------------------------------------------------------------", font=("Time", 15)).place(x=0, y=80)

        global entra_periodo
    	entra_periodo=StringVar()
    	periodo= Entry(medio, textvariable=entra_periodo,font=("Arial", 13)).place(x=140, y=30)
        entra_periodo.set(str(datetime.today().month) +str(datetime.today().year))

        global entra_dni
    	entra_dni=StringVar()

    	dni= Entry(medio, textvariable=entra_dni,font=("Arial", 13)).place(x=440, y=30)
        entra_dni.set("DNI A INGRESAR")


        #Boton de comprobar los datos
        BotonVisualizar = Button(medio, text="Visualizar", font=("Arial", 14), activebackground ="red", width=14,command=buscarDatos).place(x=750, y=26)

        #Boton salir
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=750,y=450)

    	punto.mainloop()
