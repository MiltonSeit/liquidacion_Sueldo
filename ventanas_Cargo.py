#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from datetime import *
import time
from datetime import datetime, date, time, timedelta
from clases.recibo import Recibo
from clases.cargo import Cargo
from clases.docente import Docente
import MySQLdb
import mysql.connector
import decimal
import os

def asignacionCargo():
    fecha_ingreso = entra_fechaIngreso.get()
    #Instancia el cargo y lo asigno al docente.
    cargo = Cargo(entra_dni.get(), cargos(), escu(), fecha_ingreso)
    cargo.asignarCargo()

"""Función escuela
* @param no recibe ningún parámetro
* @return devuelve el numero de la escuela
"""
def escu():
    valor={'Isabel Estela Vera': 1, 'Agop Seferian': 2,'Bicentenario': 3,'Angel Acuna': 12,'Bernardino Rivadia': 666}
    opc2=valor[respo2.get()]
    return opc2

"""Función cargos
* @param no recibe ningún parámetro
* @return devuelve el código del cargo que tiene el Docente
"""
def cargos():
        valor={'Bibliotecarios': 1, 'Jefe Preceptores Primaria': 3, 'Jefe Coordinador': 4,'Maestro de Grado': 5,'Maestro de Grado Esc Hogar': 6,'Maestro Especial Esc Adulto': 7,'Rector Superior': 8,'Supervisor': 9}
        opc3=valor[respo3.get()]
        return opc3

def asignar_Cargo():
    docente= Docente(entra_dni.get())
    datos = docente.buscarDocente()
    #label de los nombres
    lblNom= Label(medio,text="Nombre y Apellido: ",background="gray", font=("Time", 15)).place(x=50, y=130)
    lblApe= Label(medio,text="Dirección: ",background="gray", font=("Time", 15)).place(x=500, y=130)
    lblDirecc= Label(medio,text="Teléfono: ",background="gray", font=("Time", 15)).place(x=50, y=230)

    lablFechaIngreso = Label(medio,text="Fecha Ingreso: ",background="gray", font=("Time", 15)).place(x=450, y=230)

    global entra_fechaIngreso
    entra_fechaIngreso=StringVar()
    fecha= Entry(medio, textvariable=entra_fechaIngreso,font=("Arial", 13)).place(x=610, y=230)
    entra_fechaIngreso.set("DD/MM/AAAA")

    #label de los datos
    lblNombre= Label(medio,text=datos[2], font=("Time", 15)).place(x=250, y=130)
    lblDireccion= Label(medio,text=datos[3], font=("Time", 15)).place(x=615, y=130)
    lblTelefono= Label(medio,text=datos[4], font=("Time", 15)).place(x=145, y=230)
    BotonAgrega = Button(medio, text="Guardar", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown",command=asignacionCargo, width=19).place(x=230, y=400)



def buscarDatos():
    if entra_dni.get().isdigit():
        cargo = Cargo(entra_dni.get())
        datos = cargo.buscarCargos()
        mostrarLabel(datos)
    else:
        tkMessageBox.showinfo("AVISO", " El Recibo '" + entra_dni.get() +"' no es válido(Sin Puntos Y/O Letras)")

def crearPdf(numero_Recibo, datos):
    encuentra = 'NO'
    for dato in datos:
        if dato[0]== int(numero_Recibo):
            encuentra = 'SI'

    if encuentra == 'SI':
        recibo = Recibo(numero_Recibo)
        recibo.crearPdf()
    else:
        tkMessageBox.showinfo("AVISO", " El Recibo'  " + numero_Recibo + " ' no se encuentra")

def mostrarLabel(datos):
    docente = Docente(entra_dni.get())
    if docente.buscarDocente():
        dni= Entry(medio, textvariable=entra_dni,state="disabled",font=("Arial", 13)).place(x=440, y=30)

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

        BotonGenerarRecibo = Button(medio, text="Ver Recibo", font=("Arial", 14), relief=RIDGE, activebackground ="brown", width=19, command= lambda:crearPdf(entra_recibo.get(),datos)).place(x=350,y=450)

        for dato in datos:
            if dato[4] == entra_periodo.get():
                lblIdRecibo= Label(medio,text=dato[0],background="#f0ee5f", font=("Time", 15)).place(x=10, y=y)
                lblNombre= Label(medio,text=dato[1],background="#f0ee5f", font=("Time", 15)).place(x=65, y=y)
                lblCargo= Label(medio,text=dato[2],background="#f0ee5f", font=("Time", 15)).place(x=270, y=y)
                lblEscuela= Label(medio,text=dato[3],background="#f0ee5f", font=("Time", 15)).place(x=625, y=y)
                lblPeriodo= Label(medio,text=dato[4],background="#f0ee5f", font=("Time", 15)).place(x=900, y=y)
                BotonVisualizar = Button(medio, text="Visualizar", state="disabled",font=("Arial", 14), activebackground ="red", width=14).place(x=680, y=26)
                y = y +50
    else:
        tkMessageBox.showinfo("AVISO", " El DNI'  " + entra_dni.get() + " ' No se encuentra registrado")

def limpiar():
    y = 150

    cargo = Cargo(entra_dni.get())
    datos = cargo.buscarCargos()
    dni= Entry(medio, textvariable=entra_dni,state="normal",font=("Arial", 13)).place(x=440, y=30)
    for dato in datos:
        if dato[4] == entra_periodo.get():
            lblIdRecibo= Label(medio,text="     ",background="#f0ee5f", font=("Time", 15)).place(x=10, y=y)
            lblNombre= Label(medio,text="                                ",background="#f0ee5f", font=("Time", 15)).place(x=65, y=y)
            lblCargo= Label(medio,text="                                               ",background="#f0ee5f", font=("Time", 15)).place(x=270, y=y)
            lblEscuela= Label(medio,text="                                  ",background="#f0ee5f", font=("Time", 15)).place(x=625, y=y)
            lblPeriodo= Label(medio,text="          ",background="#f0ee5f", font=("Time", 15)).place(x=900, y=y)
            BotonVisualizar = Button(medio, text="Visualizar", font=("Arial", 14), activebackground ="red", width=14,command=buscarDatos).place(x=680, y=26)
            entra_dni.set("")
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
        BotonVisualizar = Button(medio, text="Visualizar", font=("Arial", 14), activebackground ="red", width=14,command=buscarDatos).place(x=680, y=26)
        BotonLimpiar = Button(medio, text="Limpiar", font=("Arial", 14), activebackground ="red", width=10,command=limpiar).place(x=850, y=26)

        #Boton salir
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=750,y=450)

    	punto.mainloop()

"""
VENTANA DE Asignar cargos
"""
def Asignar_Cargos():

    	punto= Toplevel()
    	punto.title("ASIGNAR CARGOS AL DOCENTE")
    	punto.geometry("1000x500+200+200")

        global medio
    	medio=Frame(punto, width=1000, height=650)
    	medio.pack(side=BOTTOM)

    	imagen1=PhotoImage(file="imagenes/turq2.png")
    	lblImagen= Label(medio, image= imagen1).place(x=0, y=0)

    	#etiquetas
        lblDni= Label(medio,text="DNI: ",background="gray", font=("Time", 15)).place(x=150, y=30)
        lblSeparar= Label(medio,text="------------------------------------------------------------------------------------------------------------------------------------------------", font=("Time", 15)).place(x=0, y=80)

        global entra_dni
    	entra_dni=StringVar()
    	dni= Entry(medio, textvariable=entra_dni,font=("Arial", 13)).place(x=240, y=30)
        entra_dni.set("DNI A BUSCAR")



        #Boton de comprobar los datos
        BotonBuscar = Button(medio, text="Buscar Docente", font=("Arial", 14), activebackground ="red", width=14, command= asignar_Cargo).place(x=450, y=26)

        	#Conexion
        global respo2
        global respo3

        respo2=StringVar(medio)
        opciones = ['Seleccione Escuela','Isabel Estela Vera', 'Agop Seferian','Bicentenario','Angel Acuna','Bernardino Rivadia']
        entra02 = OptionMenu (medio, respo2,*opciones,command= escu).place(x=400,y=300)
        respo2.set(opciones[0])

        respo3=StringVar(medio)
        opciones = ['Seleccione Cargo','Bibliotecarios', 'Jefe Preceptores Primaria', 'Jefe Coordinador','Maestro de Grado','Maestro de Grado Esc Hogar','Maestro Especial Esc Adulto','Rector Superior','Supervisor']
        entra03 = OptionMenu (medio, respo3,*opciones,command= cargos).place(x=600,y=300)
        respo3.set(opciones[0])

        global BotonAgrega
    	#Boton Agregar cargo
    	BotonAgrega = Button(medio, text="Guardar", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19).place(x=230, y=400)

    	#Boton salir
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=500,y=400)

    	punto.mainloop()
