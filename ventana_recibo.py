#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from datetime import *
from clases.recibo import Recibo
import MySQLdb
import mysql.connector
import decimal
import os

"""def abrirPdf():
    titi='lasdla.pdf'
    os.system('evince '+titi)
"""

def calcularNoseQue():
    mes = date.today().month

    if int(entra_periodo.get()) > 12:
        tkMessageBox.showinfo("AVISO", " El periodo ingresado es incorrecto no existe")
    elif mes < int(entra_periodo.get()):
        tkMessageBox.showinfo("AVISO", " El periodo ingresado es incorrecto, todavia a ese mes no llegamos")
    elif mes == int(entra_periodo.get()):
        recibo = Recibo(1)
        recibo.obtenerDatosParaRecibo()
    else:
        tkMessageBox.showinfo("AVISO", " El periodo ingresado es incorrecto, ese mes ya se paso")



def guardarRecibo(cod_Asignar,sueldo_basico,montoAntiguedad,zona,asignacionJulio,presentismo,noRemunerativo,subTotal1,jubilacion,obra_Social,seguro,subTotal2,total,periodo):
    try:
        bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
        cursor = bd.cursor()
        sql="INSERT INTO Recibo(cod_Asignar, sueldoBasico, montoAnti, sumaZona, asignacion_Julio,presentismo, no_Remune, subTotal1, jubilacion, desObraSoial, seguro, subTotal2, total,fechaPeriodo) VALUES ('%s' , '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s' , '%s', '%s', '%s', '%s', '%s')" % (cod_Asignar,sueldo_basico,montoAntiguedad,zona,asignacionJulio,presentismo,noRemunerativo,subTotal1,jubilacion,obra_Social,seguro,subTotal2,total,periodo)
        cursor.execute(sql)
        bd.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    bd.close()

"""
VENTANA DE CALCULAR RECIBO
"""
def ventanaCalcular():

    	punto= Toplevel()
    	punto.title("Calcular Sueldo")
    	punto.geometry("1000x500+200+200")

        global medio
    	medio=Frame(punto, width=1000, height=650)
    	medio.pack(side=BOTTOM)

    	imagen1=PhotoImage(file="imagenes/turq2.png")
    	lblImagen= Label(medio, image= imagen1).place(x=0, y=0)

    	#etiquetas
        lblDni= Label(medio,text="Período: ",background="gray", font=("Time", 15)).place(x=150, y=30)
        lblSeparar= Label(medio,text="------------------------------------------------------------------------------------------------------------------------------------------------", font=("Time", 15)).place(x=0, y=80)

        global entra_periodo
    	entra_periodo=StringVar()
    	periodo= Entry(medio, textvariable=entra_periodo,font=("Arial", 13)).place(x=240, y=30)
        entra_periodo.set("Periodo a generar")


        #Boton de comprobar los datos
        BotonCalcular = Button(medio, text="Calcular", font=("Arial", 14), activebackground ="red", width=14, command=calcularNoseQue).place(x=450, y=26)

        #Boton salir
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=750,y=400)

    	punto.mainloop()
