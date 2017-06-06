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
        obtenerDatosParaRecibo()
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

def calcularRecibo(cod_Asignar, sueldo_basico,porcAnti,porcZona,descObra):
    #BENEFICIOS
    montoAntiguedad = sueldo_basico * decimal.Decimal(porcAnti)
    zona = sueldo_basico * decimal.Decimal(porcZona)
    asignacionJulio = 1852
    presentismo = (((sueldo_basico + montoAntiguedad) * decimal.Decimal(0.75))*decimal.Decimal(0.08))
    noRemunerativo = 1000
    subTotal1 = (sueldo_basico + montoAntiguedad + zona + asignacionJulio + presentismo + noRemunerativo)

    mes = str(datetime.today().month)
    anio = str(datetime.today().year)
    periodo = mes + anio
    #DESCUENTOS
    jubilacion = subTotal1 * decimal.Decimal(0.20)
    obra_Social = subTotal1 * decimal.Decimal(descObra)
    seguro = 300
    subTotal2 = (jubilacion + obra_Social + seguro)

    #TOTAL
    total = subTotal1 - subTotal2
    guardarRecibo(cod_Asignar,round(sueldo_basico,2), round(montoAntiguedad,2), round(zona,2),round(asignacionJulio,2), round(presentismo,2), round(noRemunerativo,2), round(subTotal1,2), round(jubilacion,2), round(obra_Social,2), round(seguro,2), round(subTotal2,2), round(total,2), periodo)

def obtenerDatosParaRecibo():
    try:
        bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
        cursor = bd.cursor()
        sql="SELECT distinct a.cod_Asignar, (3.437393 * c.puntos_Cargos), ant.porc_Anti, zon.porcentaje_Zona ,obra.descuento_Obra FROM Docente d INNER JOIN Asignar a on d.dni_Docente = a.dni_Docente INNER JOIN ObraSocial obra on obra.cod_ObraSocial = d.cod_ObraSocial INNER JOIN Cargo c on c.cod_Cargo = a.cod_Cargo INNER JOIN Antiguedad ant on ant.cod_Antiguedad = d.cod_Antiguedad INNER JOIN Escuela esc on esc.numero_Escuela = a.numero_Escuela  INNER JOIN Zona zon on zon.cod_Zona = esc.cod_Zona;"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for registro in resultados:
            cod_Asignar = registro[0]
            sueldo_basico = registro[1]
            porcAnti = registro[2]
            porcZona = registro[3]
            descObra = registro[4]
            calcularRecibo(cod_Asignar,sueldo_basico,porcAnti,porcZona,descObra)
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
