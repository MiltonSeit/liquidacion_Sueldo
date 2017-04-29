#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import time
from datetime import datetime, date, time, timedelta
import tkMessageBox
from clases.docente import Docente
from clases.asigna import Asigna




"""Función Comprobar
* @param no recibe ningún parámetro
* @return verifica si los datos están correctos
"""
def funcionComprobar():
    if entra_dni.get().isdigit():
        pass
    else:
        tkMessageBox.showerror("AVISO", " DNI INCORRECTO: SIN PUNTOS Y/O LETRAS")
        return False

    for en in entra_nom.get():
        if en.isdigit():
            tkMessageBox.showerror("AVISO", " NOMBRE INCORRECTO: SIN NÚMEROS")
            return False
        elif (en == "/") or(en == " ") or en == "-":
            tkMessageBox.showerror("AVISO", " NOMBRE INCORRECTO: SIN CARACTERES ESPECIALES")
            return False

    for en in entra_ape.get():
        if en.isdigit():
            tkMessageBox.showerror("AVISO", " APELIIDO INCORRECTO: SIN NUMEROS")
            return False
        elif (en == "/") or(en == " ") or en == "-":
            tkMessageBox.showerror("AVISO", " APELIIDO INCORRECTO: SIN CARACTERES ESPECIALES")
            return False
    if entra_tel.get().isdigit():
        pass
    else:
        tkMessageBox.showerror("AVISO", " TELEFONO INCORRECTO: SIN PUNTOS Y/O LETRAS")
        return False

    return True

"""Función antiguedad
* @param no recibe ningún parámetro
* @return devuelve la cantidad de años que ejerce como Docente
"""
def antiguedad():
    fechActual = datetime.now()
    formato = "%d/%m/%Y"
    fecha_ingreso = entra_fecha.get()
    fecha_ingreso = datetime.strptime(fecha_ingreso, formato)
    diferencia = (fechActual - fecha_ingreso)
    resultado = (diferencia/365)
    anios = resultado.days
    if anios > 24:
        return 25
    else:
        return anios

"""Función obra social
* @param no recibe ningún parámetro
* @return devuelve el código de la obra social
"""
def obraS():
    valor={'Asimira': 1, 'Medisur': 2, 'Sps Salud': 3,'Osecac': 4,'Ioscor': 5}
    opc=valor[respo1.get()]
    return opc

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

"""Función agregar_Docente
* @param no recibe ningún parámetro
* @return da de alta al docente y asigna el cargo
"""
def agregar_Docente():
    if funcionComprobar():
        #Instancia el Docente y da de alta.
        docente = Docente(entra_dni.get(), antiguedad(), obraS(), entra_nom.get(), entra_ape.get(), entra_dire.get(), entra_tel.get(), entra_fecha.get())
        docente.altaDocente()

        #Instancia el cargo y lo da de alta.
        asigna = Asigna(entra_dni.get(), cargos(), escu())
        asigna.asignarCargo()

    else:
        tkMessageBox.showwarning ("AVISO", " CORREGIR LOS DATOS ERRONEOS")

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


#funciones

"""Función Alta_Docente
* @param no recibe ningún parámetro
* @return devuelve abre una nueva ventana para agregar los datos y dar de alta al Docente
"""
def Alta_Docente():

	punto= Toplevel(ventana)
	punto.title("Alta-Docente")
	punto.geometry("1000x500+200+200")
    

	medio=Frame(punto, width=1000, height=650)
	medio.pack(side=BOTTOM)

	imagen1=PhotoImage(file="imagenes/turq2.png")
	lblImagen= Label(medio, image= imagen1).place(x=0, y=0)

	#etiquetas
	lblNom= Label(medio,text="Nombre", font=("Time", 15)).place(x=50, y=30)
	lblApe= Label(medio,text="Apellido", font=("Time", 15)).place(x=500, y=30)
	lblDni= Label(medio,text="DNI", font=("Time", 15)).place(x=50, y=130)
	lblDirecc= Label(medio,text="Direccion", font=("Time", 15)).place(x=500, y=130)
	lblTel= Label(medio,text="Telefono", font=("Time", 15)).place(x=50, y=230)
	lblFech= Label(medio,text="Fecha-Ingreso", font=("Time", 15)).place(x=500, y=230)

	global entra_nom
	global entra_dni
	global entra_ape
	global entra_dire
	global entra_tel
	global entra_fecha

	entra_nom = StringVar()
	nombre = Entry(medio, textvariable=entra_nom,font=("Arial", 13)).place(x=140, y=30)

	entra_ape= StringVar()
	apellido= Entry(medio, textvariable=entra_ape,font=("Arial", 13)).place(x=600, y=30)

	entra_dni=StringVar()
	dni= Entry(medio, textvariable=entra_dni,font=("Arial", 13)).place(x=140, y=130)

	entra_dire=StringVar()
	direccion= Entry(medio, textvariable=entra_dire,font=("Arial", 13)).place(x=600, y=130)

	entra_tel=StringVar()
	telefono= Entry(medio, textvariable=entra_tel,font=("Arial", 13)).place(x=160, y=230)

	entra_fecha=StringVar()
	fecha= Entry(medio, textvariable=entra_fecha,font=("Arial", 13)).place(x=650, y=230)

	#Conexion
	global respo1
	global respo2
	global respo3

	respo1=StringVar(medio)
	opciones = ['Seleccione obra Social','Asimira', 'Medisur', 'Sps Salud','Osecac','Ioscor']
	entra01 = OptionMenu (medio, respo1,*opciones, command= obraS).place(x=200,y=300)
	respo1.set(opciones[0])

	respo2=StringVar(medio)
	opciones = ['Seleccione Escuela','Isabel Estela Vera', 'Agop Seferian','Bicentenario','Angel Acuna','Bernardino Rivadia']
	entra02 = OptionMenu (medio, respo2,*opciones,command= escu).place(x=400,y=300)
	respo2.set(opciones[0])

	respo3=StringVar(medio)
	opciones = ['Seleccione Cargo','Bibliotecarios', 'Jefe Preceptores Primaria', 'Jefe Coordinador','Maestro de Grado','Maestro de Grado Esc Hogar','Maestro Especial Esc Adulto','Rector Superior','Supervisor']
	entra03 = OptionMenu (medio, respo3,*opciones,command= cargos).place(x=600,y=300)
	respo3.set(opciones[0])

	#Boton Agregar persona
	BotonAgrega = Button(medio, text="Guardar", font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= agregar_Docente).place(x=230, y=400)

	#Boton salir
	BotonSalir = Button(medio, text="Salir", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=500,y=400)

	punto.mainloop()

#Botones
btonAlta=Button(centro, text="Alta Docente", font=("Time", 15), width=10, command=Alta_Docente).place(x=150, y=80)
btonBaja=Button(centro, text="Baja Docente", font=("Time", 15), width=10).place(x=425, y=80)
btonModifica=Button(centro, text="Modificar-Datos", font=("Time", 15), width=12).place(x=700, y=80)
btonLista=Button(centro, text="Listar", font=("Time", 15), width=12).place(x=700, y=190)
btonCalcula=Button(centro, text="Calcular Sueldo", font=("Time", 15), width=12).place(x=150, y=190)
btonVisualiza=Button(centro, text="Previsualizar", font=("Time", 15), width=10).place(x=425, y=190)
btonSalir= Button(centro, text="Salir", font=("Time", 15), width=10, command=ventana.destroy).place(x=800, y=350)

ventana.mainloop()
