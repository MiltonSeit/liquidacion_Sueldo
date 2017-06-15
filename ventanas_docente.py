#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import time
from datetime import datetime, date, time, timedelta
import tkMessageBox
from clases.docente import Docente
from clases.asigna import Asigna

def alta_Docente():
    docente = Docente(entra_dni.get())
    docente.altaDocente()
    BotonBaja = Button(medio, text="Baja Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)
    BotonAlta = Button(medio, text="Alta Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)

def baja_Docente():
    docente = Docente(entra_dni.get())
    docente.bajaDocente()
    BotonAlta = Button(medio, text="Alta Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)
    BotonBaja = Button(medio, text="Baja Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)


def asignacionCargo():
    #Instancia el cargo y lo asigno al docente.
    asigna = Asigna(entra_dni.get(), cargos(), escu())
    asigna.asignarCargo()


def asignar_Cargo():
    docente= Docente(entra_dni.get())
    datos = docente.buscarDocente()
    #label de los nombres
    lblNom= Label(medio,text="Nombre: ",background="gray", font=("Time", 15)).place(x=50, y=130)
    lblApe= Label(medio,text="Apellido: ",background="gray", font=("Time", 15)).place(x=500, y=130)
    lblDirecc= Label(medio,text="Direccion: ",background="gray", font=("Time", 15)).place(x=50, y=230)
    lblTel= Label(medio,text="Telefono: ",background="gray", font=("Time", 15)).place(x=500, y=230)
    lblFech= Label(medio,text="Fecha-Ingreso: ",background="gray", font=("Time", 15)).place(x=50, y=330)
    #label de los datos
    lblNombre= Label(medio,text=datos[2], font=("Time", 15)).place(x=140, y=130)
    lblApellido= Label(medio,text=datos[3], font=("Time", 15)).place(x=600, y=130)
    lblDireccion= Label(medio,text=datos[4], font=("Time", 15)).place(x=160, y=230)
    lblTelefono= Label(medio,text=datos[5], font=("Time", 15)).place(x=600, y=230)
    lblFecha= Label(medio,text=datos[6], font=("Time", 15)).place(x=200, y=330)
    BotonAgrega = Button(medio, text="Guardar", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown",command=asignacionCargo, width=19).place(x=230, y=400)

"""Función buscarDocente
* @param no recibe ningún parámetro
* @return busca el dato del docente e instancia los botones para dar de alta y/O baja respectivamente
"""
def alta_bajaDocente():
    if entra_dni.get().isdigit():
        docente= Docente(entra_dni.get())
        datos = docente.buscarDocente()
        #label de los nombres
        lblNom= Label(medio,text="Nombre: ",background="gray", font=("Time", 15)).place(x=50, y=130)
        lblApe= Label(medio,text="Apellido: ",background="gray", font=("Time", 15)).place(x=500, y=130)
        lblDirecc= Label(medio,text="Direccion: ",background="gray", font=("Time", 15)).place(x=50, y=230)
        lblTel= Label(medio,text="Telefono: ",background="gray", font=("Time", 15)).place(x=500, y=230)
        lblFech= Label(medio,text="Fecha-Ingreso: ",background="gray", font=("Time", 15)).place(x=50, y=330)
        #label de los datos
        lblNombre= Label(medio,text=datos[2], font=("Time", 15)).place(x=140, y=130)
        lblApellido= Label(medio,text=datos[3], font=("Time", 15)).place(x=600, y=130)
        lblDirecciom= Label(medio,text=datos[4], font=("Time", 15)).place(x=160, y=230)
        blTelefono= Label(medio,text=datos[5], font=("Time", 15)).place(x=600, y=230)
        lblFecha= Label(medio,text=datos[6], font=("Time", 15)).place(x=200, y=330)

        #Activar el boton de docente
        if datos[7] == 'Y':
            BotonBaja = Button(medio, text="Baja Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)
            BotonAlta = Button(medio, text="Alta Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)
        elif datos[7]== 'N':
            BotonAlta = Button(medio, text="Alta Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)
            BotonBaja = Button(medio, text="Baja Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)
    else:
        tkMessageBox.showerror("DNI INCORRECTO", " SIN PUNTOS, ESPACIOS Y/O LETRAS")



def actualizarDocente():
    docente= Docente(entra_dni.get(),antiguedad(), obraS(), entra_nom.get(),entra_ape.get(), entra_dire.get(), entra_tel.get(), entra_fecha.get())
    docente.modificarDocente()
    entra_dni.set("")
    entra_nom.set("")
    entra_ape.set("")
    entra_dire.set("")
    entra_tel.set("")
    entra_fecha.set("")

"""Función buscarDocente
* @param no recibe ningún parámetro
* @return verifica si los datos están correctos
"""
def buscarDocente():
    docente= Docente(entra_dni.get())
    datos = docente.buscarDocente()
    entra_nom.set(datos[2])
    entra_ape.set(datos[3])
    entra_dire.set(datos[4])
    entra_tel.set(datos[5])
    entra_fecha.set(datos[6])
    valor={1:'Asimira', 2:'Medisur',3:'Sps Salud',4:'Osecac',5:'Ioscor'}
    opc=valor[datos[1]]
    lblObraSocial= Label(medio,text=opc, font=("Time", 15)).place(x=550, y=328)
    BotonAgrega = Button(medio, text="ACTUALIZAR", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= actualizarDocente).place(x=230, y=400)

"""Función Comprobar
* @param no recibe ningún parámetro
* @return verifica si los datos están correctos
"""
def funcionComprobar(*args):
    if entra_dni.get().isdigit():
        pass
    else:
        tkMessageBox.showerror("DNI INCORRECTO", " SIN PUNTOS, ESPACIOS Y/O LETRAS")
        return False

    for en in entra_nom.get():
        if en.isdigit():
            tkMessageBox.showerror("NOMBRE INCORRECTO", " SIN NÚMEROS           ")
            return False
        elif (en == "/") or en == "-":
            tkMessageBox.showerror("NOMBRE INCORRECTO", " SIN CARACTERES ESPECIALES")
            return False

    for en in entra_ape.get():
        if en.isdigit():
            tkMessageBox.showerror("APELLIDO INCORRECTO", "SIN NUMEROS       ")
            return False
        elif (en == "/") or en == "-":
            tkMessageBox.showerror("APELLIDO INCORRECTO", "SIN CARACTERES ESPECIALES")
            return False
    if entra_tel.get().isdigit():
        pass
    else:
        tkMessageBox.showerror("TELEFONO INCORRECTO", "SIN PUNTOS, GUINOES Y/O LETRAS")
        return False
    docente = Docente(entra_dni.get(), antiguedad(), obraS(), entra_nom.get(), entra_ape.get(), entra_dire.get(), entra_tel.get(), entra_fecha.get())

    if docente.buscarDocente():
        tkMessageBox.showerror("AVISO", " El DNI ' " + entra_dni.get() + "' Se encuentra registrado, pruebe con otro.")
        return False

    tkMessageBox.showinfo("AVISO", " DATOS CORRECTOS")
    BotonAgrega = Button(medio, text="Guardar", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= agregar_Docente).place(x=230, y=400)
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
    docente = Docente(entra_dni.get(), antiguedad(), obraS(), entra_nom.get(), entra_ape.get(), entra_dire.get(), entra_tel.get(), entra_fecha.get())
    docente.agregarDocente()
    entra_dni.set("")
    entra_nom.set("")
    entra_ape.set("")
    entra_dire.set("")
    entra_tel.set("")
    entra_fecha.set("")

"""
VENTANA AGREGAR DOCENTE
"""
def Agregar_Docente():

	punto= Toplevel()
	punto.title("Agregar-Docente")
	punto.geometry("1000x500+200+200")

        global medio
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
        entra_fecha.set("DD/MM/AAAA")

	#Conexion
	global respo1
	global respo2
	global respo3

	respo1=StringVar(medio)
	opciones = ['Seleccione obra Social','Asimira', 'Medisur', 'Sps Salud','Osecac','Ioscor']
	entra01 = OptionMenu (medio, respo1,*opciones, command= obraS).place(x=200,y=300)
	respo1.set(opciones[0])

        #Boton de comprobar los datos
        BotonComprobar = Button(medio, text="Comprobar-Datos", font=("Arial", 14), activebackground ="red", width=14, command= funcionComprobar).place(x=790, y=80)

        global BotonAgrega
	#Boton Agregar persona
	BotonAgrega = Button(medio, text="Guardar", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= agregar_Docente).place(x=230, y=400)

	#Boton salir
	BotonSalir = Button(medio, text="Salir", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=500,y=400)

	punto.mainloop()

"""
VENTANA DE MODIFICAR DOCENTE
"""
def Modificar_Docente():

    	punto= Toplevel()
    	punto.title("MODIFICAR - DOCENTE")
    	punto.geometry("1000x500+200+200")

        global medio
    	medio=Frame(punto, width=1000, height=650)
    	medio.pack(side=BOTTOM)

    	imagen1=PhotoImage(file="imagenes/turq2.png")
    	lblImagen= Label(medio, image= imagen1).place(x=0, y=0)

    	#etiquetas
        lblDni= Label(medio,text="DNI", font=("Time", 15)).place(x=150, y=30)
    	lblNom= Label(medio,text="Nombre", font=("Time", 15)).place(x=50, y=130)
    	lblApe= Label(medio,text="Apellido", font=("Time", 15)).place(x=500, y=130)
    	lblDirecc= Label(medio,text="Direccion", font=("Time", 15)).place(x=50, y=230)
    	lblTel= Label(medio,text="Telefono", font=("Time", 15)).place(x=500, y=230)
    	lblFech= Label(medio,text="Fecha-Ingreso", font=("Time", 15)).place(x=50, y=330)
        lblSeparar= Label(medio,text="------------------------------------------------------------------------------------------------------------------------------------------------", font=("Time", 15)).place(x=0, y=80)
    	global entra_nom
    	global entra_dni
    	global entra_ape
    	global entra_dire
    	global entra_tel
    	global entra_fecha


    	entra_nom = StringVar()
    	nombre = Entry(medio, textvariable=entra_nom,font=("Arial", 13)).place(x=140, y=130)


    	entra_ape= StringVar()
    	apellido= Entry(medio, textvariable=entra_ape,font=("Arial", 13)).place(x=600, y=130)


    	entra_dni=StringVar()
    	dni= Entry(medio, textvariable=entra_dni,font=("Arial", 13)).place(x=240, y=30)
        entra_dni.set("DNI A BUSCAR")

    	entra_dire=StringVar()
    	direccion= Entry(medio, textvariable=entra_dire,font=("Arial", 13)).place(x=160, y=230)


    	entra_tel=StringVar()
    	telefono= Entry(medio, textvariable=entra_tel,font=("Arial", 13)).place(x=600, y=230)


    	entra_fecha=StringVar()
    	fecha= Entry(medio, textvariable=entra_fecha,font=("Arial", 13)).place(x=200, y=330)

    	#Conexion
    	global respo1
    	global respo2
    	global respo3

    	respo1=StringVar(medio)
    	opciones = ['Seleccione obra Social','Asimira', 'Medisur', 'Sps Salud','Osecac','Ioscor']
    	entra01 = OptionMenu (medio, respo1,*opciones, command= obraS).place(x=700,y=328)
    	respo1.set(opciones[0])

        #Boton modificar cargo
        BotonModificarCargo = Button(medio, text="Modificar Cargo", font=("Arial", 14), activebackground ="red", width=14, command= buscarDocente).place(x=450, y=26)

        #Boton de comprobar los datos
        BotonComprobar = Button(medio, text="Buscar Docente", font=("Arial", 14), activebackground ="red", width=14, command= buscarDocente).place(x=450, y=26)

        global BotonAgrega
    	#Boton Agregar persona
    	BotonAgrega = Button(medio, text="ACTUALIZAR", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= agregar_Docente).place(x=230, y=400)

    	#Boton salir
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=500,y=400)

    	punto.mainloop()

"""
VENTANA DE MODIFICAR DOCENTE
"""
def AlBa_Docente():
        #Crea la variable para la ventana
    	punto= Toplevel()
    	punto.title("DAR DE ALTA/BAJA AL DOCENTE")
    	punto.geometry("1000x500+200+200")

        global medio
    	medio=Frame(punto, width=1000, height=650)
    	medio.pack(side=BOTTOM)

        #Imagen para fondo
    	imagen1=PhotoImage(file="imagenes/turq2.png")
    	lblImagen= Label(medio, image= imagen1).place(x=0, y=0)

    	#Label DNI y separador
        lblDni= Label(medio,text="DNI: ",background="gray", font=("Time", 15)).place(x=150, y=30)
        lblSeparar= Label(medio,text="------------------------------------------------------------------------------------------------------------------------------------------------", font=("Time", 15)).place(x=0, y=80)

        #Input para entrada de DNI
        global entra_dni
    	entra_dni=StringVar()
    	dni= Entry(medio, textvariable=entra_dni,font=("Arial", 13)).place(x=240, y=30)
        entra_dni.set("DNI A BUSCAR")


        #Boton de buscar los datos
        BotonBuscar = Button(medio, text="Buscar Docente", font=("Arial", 14), activebackground ="red", width=14, command= alta_bajaDocente).place(x=450, y=26)

        global BotonBaja
    	#Boton Baja
    	BotonBaja = Button(medio, text="Baja Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19,).place(x=230, y=400)

        global BotonAlta
        #Boton Alta
    	BotonAlta = Button(medio, text="Alta Docente", state='disabled',font=("Arial", 14), relief=RIDGE, activebackground ="brown",  width=19).place(x=500,y=400)

    	#Boton Salir
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=750,y=400)

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
        global respo1
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
