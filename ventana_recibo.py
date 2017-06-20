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

def calcularecibo():
    #Pregunta si el periodo ingresado es un número, si lo es entra en el if sino muestra ell mensaje que no lo es
    if entra_periodo.get().isdigit():
        mes = date.today().month
        anio = date.today().year

        #Genera el período actual.
        periodo = (str(entra_periodo.get())+str(anio))

        #Verificar si esta en el período actual.
        if int(entra_periodo.get()) > 12:
            tkMessageBox.showinfo("AVISO", " El periodo ingresado es incorrecto no existe")
        elif mes < int(entra_periodo.get()):
            tkMessageBox.showinfo("AVISO", " El periodo ingresado es incorrecto, todavia a ese mes no llegamos")
        elif mes == int(entra_periodo.get()):
            recibo = Recibo()
            existe = recibo.buscarPeriodo()
            #Verifica que ya no haya sido generado este período, sino lo está lo genera.
            if(periodo in existe):
                tkMessageBox.showerror("AVISO", " Este Periodo ya fue generado")
            else:
                recibo.calcularRecibo()
        else:
            tkMessageBox.showinfo("AVISO", " El periodo ingresado es incorrecto, ese mes ya se paso")
    else:
        tkMessageBox.showerror("DNI INCORRECTO", " SIN PUNTOS, ESPACIOS Y/O LETRAS")


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

        lblaclaracion= Label(medio,text="Solamente debe ingresarse el número del mes: 'Por ejemplo para Mayo = 5' ",background="gray", font=("Time", 15)).place(x=150, y=230)

        #Boton de comprobar los datos
        BotonCalcular = Button(medio, text="Calcular", font=("Arial", 14), activebackground ="red", width=14, command=calcularecibo).place(x=450, y=26)

        #Boton salir
    	BotonSalir = Button(medio, text="SALIR", font=("Arial", 14), relief=RIDGE, activebackground ="brown", command = punto.destroy, width=19).place(x=750,y=400)

    	punto.mainloop()
