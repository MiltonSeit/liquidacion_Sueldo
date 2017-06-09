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
    datos = asignar.buscarCargos()
    mostrarLabel(datos)

def mostrarRecibo(numero_Recibo, datos):
    encuentra = 'NO'
    for dato in datos:
        if dato[0]== int(numero_Recibo):
            encuentra = 'SI'

    if encuentra == 'SI':
        recibo = Recibo(numero_Recibo)
        recibo.buscarRecibo()
    else:
        tkMessageBox.showinfo("AVISO", " El Recibo'  " + numero_Recibo + " ' no se encuentra")


def mostrarLabel(datos):
    y = 150
    lblIdRecibo= Label(medio,text="Nº",background="#ec8a3a", font=("Time", 15)).place(x=10, y=110)
    lblNombre= Label(medio,text="Nombre/Apellido",background="#ec8a3a", font=("Time", 15)).place(x=65, y=110)
    lblCargo= Label(medio,text="Cargo que ocupa",background="#ec8a3a", font=("Time", 15)).place(x=270, y=110)
    lblEscuela= Label(medio,text="Escuela",background= "#ec8a3a", font=("Time", 15)).place(x=625, y=110)
    lblPeriodo= Label(medio,text="Período",background="#ec8a3a", font=("Time", 15)).place(x=900, y=110)

    global entra_recibo
    entra_recibo=StringVar()
    recibo= Entry(medio, textvariable=entra_recibo,font=("Arial", 13)).place(x=100, y=450)
    entra_recibo.set("Ingresar Nº de Recibo")

    BotonGenerarRecibo = Button(medio, text="Ver Recibo", font=("Arial", 14), relief=RIDGE, activebackground ="brown", width=19, command= lambda:mostrarRecibo(entra_recibo.get(),datos)).place(x=350,y=450)

    for dato in datos:
        if dato[5] == entra_periodo.get():
            lblIdRecibo= Label(medio,text=dato[0],background="#f0ee5f", font=("Time", 15)).place(x=10, y=y)
            lblNombre= Label(medio,text=dato[1]+" "+dato[2],background="#f0ee5f", font=("Time", 15)).place(x=65, y=y)
            lblCargo= Label(medio,text=dato[3],background="#f0ee5f", font=("Time", 15)).place(x=270, y=y)
            lblEscuela= Label(medio,text=dato[4],background="#f0ee5f", font=("Time", 15)).place(x=625, y=y)
            lblPeriodo= Label(medio,text=dato[5],background="#f0ee5f", font=("Time", 15)).place(x=900, y=y)
            #BotonRecibo = Button(medio, text="Visualizar", font=("Arial", 14), activebackground ="red", width=10, command=lambda:mostrarRecibo(dato[0])).place(x=820, y=y)
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
