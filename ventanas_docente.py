#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import time
from datetime import datetime, date, time, timedelta
import tkMessageBox
from clases.docente import Docente
from clases.cargo import Cargo

"""Función alta_Docente
* @param no recibe ningún parámetro
* @return cambia el estado del docente dejandolo como activo o de Alta
"""
def alta_Docente():
    docente = Docente(entra_dni.get())
    docente.altaDocente()
    BotonBaja = Button(medio, text="Baja Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)
    BotonAlta = Button(medio, text="Alta Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)

"""Función baja_Docente
* @param no recibe ningún parámetro
* @return cambia el estado del docente dejandolo como inactivo o de Baja
"""
def baja_Docente():
    docente = Docente(entra_dni.get())
    docente.bajaDocente()
    BotonAlta = Button(medio, text="Alta Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)
    BotonBaja = Button(medio, text="Baja Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)


"""Función alta_bajaDocente
* @param no recibe ningún parámetro
* @return busca el dato del docente e instancia los botones para dar de alta y/O baja respectivamente
"""
def alta_bajaDocente():
    docente = Docente()
    datos = docente.buscarDni()


    if entra_dni.get().isdigit():
        if(entra_dni.get() in datos):
            docente= Docente(entra_dni.get())
            datos = docente.buscarDocente()
            #label de los nombres
            lblNom= Label(medio,text="Nombre y Apellido: ",background="gray", font=("Time", 15)).place(x=50, y=130)
            lblDirecc= Label(medio,text="Direccion: ",background="gray", font=("Time", 15)).place(x=500, y=130)
            lblTel= Label(medio,text="Telefono: ",background="gray", font=("Time", 15)).place(x=50, y=230)
            #label de los datos
            lblNomApe= Label(medio,text=datos[2], font=("Time", 15)).place(x=245, y=130)
            lblDireccion= Label(medio,text=datos[3], font=("Time", 15)).place(x=610, y=130)
            lblTelefono= Label(medio,text=datos[4], font=("Time", 15)).place(x=155, y=230)

            #Activar el boton de docente
            if datos[5] == 'Y':
                BotonBaja = Button(medio, text="Baja Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)
                BotonAlta = Button(medio, text="Alta Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)
            elif datos[5]== 'N':
                BotonAlta = Button(medio, text="Alta Docente", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= alta_Docente).place(x=500,y=400)
                BotonBaja = Button(medio, text="Baja Docente", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command=baja_Docente).place(x=230, y=400)
        else:
            tkMessageBox.showerror("AVISO", " El DNI ' " + entra_dni.get() + "' No se encuentra registrado, pruebe con otro.")
    else:
        tkMessageBox.showerror("DNI INCORRECTO", " SIN PUNTOS, ESPACIOS Y/O LETRAS")



def actualizarDocente():
    if funcionComprobar():
        docente= Docente(entra_dni.get(), obraS(), entra_nomApe.get(), entra_dire.get(), entra_tel.get())
        docente.modificarDocente()
        entra_dni.set("")
        dni= Entry(medio, textvariable=entra_dni,  font=("Arial", 13)).place(x=240, y=30)

        entra_nomApe.set("")
        entra_dire.set("")
        entra_tel.set("")
    else:
        pass

"""Función buscarDocente
* @param no recibe ningún parámetro
* @return verifica si los datos están correctos
"""
def buscarDocente():
    docente= Docente(entra_dni.get())
    datos = docente.buscarDocente()
    entra_nomApe.set(datos[2])
    entra_dire.set(datos[3])
    entra_tel.set(datos[4])

    valor={1:'Asimira', 2:'Medisur',3:'Sps Salud',4:'Osecac',5:'Ioscor'}
    opc=valor[datos[1]]

    opciones = ['Seleccione obra Social','Asimira', 'Medisur', 'Sps Salud','Osecac','Ioscor']
    entra01 = OptionMenu (medio, respo1,*opciones, command= obraS).place(x=500,y=228)
    respo1.set(opc)
    dni= Entry(medio, textvariable=entra_dni, state="disabled", font=("Arial", 13)).place(x=240, y=30)

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

    for en in entra_nomApe.get():
        if en.isdigit():
            tkMessageBox.showerror("NOMBRE INCORRECTO", " SIN NÚMEROS           ")
            return False
        elif (en == "/") or en == "-":
            tkMessageBox.showerror("NOMBRE INCORRECTO", " SIN CARACTERES ESPECIALES")
            return False

    if entra_tel.get().isdigit():
        pass
    else:
        tkMessageBox.showerror("TELEFONO INCORRECTO", "SIN PUNTOS, GUINOES Y/O LETRAS")
        return False

    docente = Docente()
    datos = docente.buscarDni()

    if(entra_dni.get() in datos):
        tkMessageBox.showerror("AVISO", " El DNI ' " + entra_dni.get() + "' Se encuentra registrado, pruebe con otro.")
        return False
    else:
        pass

    tkMessageBox.showinfo("AVISO", " DATOS CORRECTOS")
    BotonAgrega = Button(medio, text="Guardar", state='normal', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= agregar_Docente).place(x=230, y=400)
    return True


"""Función obra social
* @param no recibe ningún parámetro
* @return devuelve el código de la obra social
"""
def obraS():
    valor={'Asimira': 1, 'Medisur': 2, 'Sps Salud': 3,'Osecac': 4,'Ioscor': 5}
    opc=valor[respo1.get()]
    return opc


"""Función agregar_Docente
* @param no recibe ningún parámetro
* @return da de alta al docente y asigna el cargo
"""
def agregar_Docente():
    docente = Docente(entra_dni.get(), obraS(), entra_nomApe.get(), entra_dire.get(), entra_tel.get())
    docente.agregarDocente()
    entra_dni.set("")
    entra_nomApe.set("")
    entra_dire.set("")
    entra_tel.set("")
    BotonAgrega = Button(medio, text="Guardar", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19, command= agregar_Docente).place(x=230, y=400)


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
	lblNomApe= Label(medio,text="Nombre y Apellido:", font=("Time", 15)).place(x=50, y=30)
	lblDni= Label(medio,text="DNI:", font=("Time", 15)).place(x=553, y=30)
	lblDirecc= Label(medio,text="Direccion:", font=("Time", 15)).place(x=500, y=130)
	lblTel= Label(medio,text="Telefono:", font=("Time", 15)).place(x=50, y=130)

	global entra_nomApe
	global entra_dni
	global entra_dire
	global entra_tel


	entra_nomApe = StringVar()
	nomApe = Entry(medio, textvariable=entra_nomApe,font=("Arial", 13)).place(x=248, y=30)

        entra_dni=StringVar()
	dni= Entry(medio, textvariable=entra_dni,font=("Arial", 13)).place(x=604, y=30)

	entra_dire=StringVar()
	direccion= Entry(medio, textvariable=entra_dire,font=("Arial", 13)).place(x=608, y=130)

	entra_tel=StringVar()
	telefono= Entry(medio, textvariable=entra_tel,font=("Arial", 13)).place(x=150, y=130)

	#Conexion
	global respo1

	respo1=StringVar(medio)
	opciones = ['Seleccione obra Social','Asimira', 'Medisur', 'Sps Salud','Osecac','Ioscor']
	entra01 = OptionMenu (medio, respo1,*opciones, command= obraS).place(x=200,y=250)
	respo1.set(opciones[5])

        #Boton de comprobar los datos
        BotonComprobar = Button(medio, text="Comprobar-Datos", font=("Arial", 14), activebackground ="red", width=14, command= funcionComprobar).place(x=670, y=250)

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
        lblDni= Label(medio,text="DNI:", font=("Time", 15)).place(x=150, y=30)
    	lblNom= Label(medio,text="Nombre y Apellido:", font=("Time", 15)).place(x=50, y=130)
    	lblApe= Label(medio,text="Dirección", font=("Time", 15)).place(x=500, y=130)
    	lblDirecc= Label(medio,text="Teléfono:", font=("Time", 15)).place(x=50, y=230)
    	lblSeparar= Label(medio,text="------------------------------------------------------------------------------------------------------------------------------------------------", font=("Time", 15)).place(x=0, y=80)

        global entra_nomApe
    	global entra_dni
    	global entra_dire
    	global entra_tel
    	global entra_fecha


    	entra_nomApe = StringVar()
    	nombre = Entry(medio, textvariable=entra_nomApe,font=("Arial", 13)).place(x=248, y=130)

    	entra_dni=StringVar()
    	dni= Entry(medio, textvariable=entra_dni,font=("Arial", 13)).place(x=240, y=30)
        entra_dni.set("DNI A BUSCAR")

    	entra_dire=StringVar()
    	direccion= Entry(medio, textvariable=entra_dire,font=("Arial", 13)).place(x=600, y=130)


    	entra_tel=StringVar()
    	telefono= Entry(medio, textvariable=entra_tel,font=("Arial", 13)).place(x=160, y=230)


    	#Conexion
    	global respo1
    	global respo2
    	global respo3

    	respo1=StringVar(medio)
    	opciones = ['Seleccione obra Social','Asimira', 'Medisur', 'Sps Salud','Osecac','Ioscor']
    	entra01 = OptionMenu (medio, respo1,*opciones, command= obraS).place(x=500,y=228)
    	respo1.set(opciones[0])

        #Boton de buscar Docente
        BotonBuscar = Button(medio, text="Buscar Docente", font=("Arial", 14), activebackground ="red", width=14, command= buscarDocente).place(x=450, y=26)

        global BotonActualiza
    	#Boton Actualizar desactivado que luego de la consulta sera activado
    	BotonActualiza = Button(medio, text="ACTUALIZAR", state='disabled', font=("Arial", 14), relief=RIDGE , activebackground ="brown", width=19).place(x=230, y=400)

    	#Boton salir cierra la ventana
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=500,y=400)

    	punto.mainloop()

"""
VENTANA DE ALBA Docente
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
