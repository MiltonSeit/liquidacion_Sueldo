#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkMessageBox
import MySQLdb
import mysql.connector
from fpdf import FPDF
import decimal
from datetime import *
import os, sys
from clase.asigna import Asigna

#Definimos la clase Recibo
class Recibo(object):
    __numero_Recibo = None

    """Constructor
    * @param numero_Recibo,fechaPeriodo
    * @return no devuelve nada
    """
    def __init__(self, numero_Recibo="", fechaPeriodo=""):
        self.__numero_Recibo = numero_Recibo

    """Getter numero_Recibo.
     * @param Ninguno.
     * @return devuelve el numero del recibo
     */
    """
    def getNumero_Recibo(self):
        return self.__numero_Recibo

"""Setter numero_Recibo.
     * @param numero_Recibo.
     * @return no devuelve nada.
     */
    """
    def setNumero_Recibo(self, numero_Recibo):
        self.__numero_Recibo = numero_Recibo

    numero_Recibo = property(fget= getNumero_Recibo,fset=setNumero_Recibo)

    def sueldo_Basico(self,puntos):
        sueldoBasico = round((3.437393 * puntos),2)
        return sueldoBasico

    def monto_Anti(self, anios, sueldoB):
        porcentaje= [0,0.10,0.15,0.15,0.15,0.30,0.30,0.40,0.40,0.40,0.50,0.50,0.60,0.60,0.60,0.70,0.70,0.80,0.80,0.80,1,1,1.10,1.10,1.20]
        monto_Anti = round((porcentaje[anios] * sueldoB),2)
        return monto_Anti

    def suma_Zona(self, sueldoB, porcentajeZona):
        sumaZona = round((sueldoB * porcentajeZona),2)
        return sumaZona

    def presentismo(self, sueldoB,montoAnti):
        presentissmo = round(((sueldoB * montoAnti)* 0.75)*0.08 ,2)
        return presentissmo

    def subTotal1(self, sueldoB, montoAnti, sumaZona, presentismo):
        subtotal1 = round((sueldoB + montoAnti + sumaZona + presentismo),2)
        return subtotal1

    def jubilacion(self, subtotal1):
        montoJubilacion = round((subtotal1 * 0.20),2)
        return montoJubilacion

    def obraSocial(self, subtotal1, descuento_Obra):
        descuentoObra = round((subtotal1 *  descuento_Obra),2)
        return descuentoObra

    def seguro(self):
        return 300

    def subTotal2(self, jubilacion, descuento_Obra, seguro):
        subtotal2 = round((jubilacion + descuento_Obra + seguro),2)
        return subtotal1

    def total(self, subtotal1, subtotal2):
        montoTotal = round((subtotal1 + subtoral2),2)
        return

    def calcularPeriodo(self):
        mes = str(datetime.today().month)
        anio = str(datetime.today().year)
        return (mes + anio)

    def calcularRecibo(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
            cursor = bd.cursor()
            sql="SELECT distinct a.cod_Asignar, c.puntos_Cargos, zon.porcentaje_Zona ,obra.descuento_Obra FROM Docente d INNER JOIN Asignar a on d.dni_Docente = a.dni_Docente INNER JOIN ObraSocial obra on obra.cod_ObraSocial = d.cod_ObraSocial INNER JOIN Cargo c on c.cod_Cargo = a.cod_Cargo INNER JOIN Escuela esc on esc.numero_Escuela = a.numero_Escuela  INNER JOIN Zona zon on zon.cod_Zona = esc.cod_Zona;"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for registro in resultados:
                sueldoBasico = self.sueldo_Basico(registro[1])
                asigna = Asigna(registro[0])
                montoAntiguedad = self.monto_Anti(asigna.antiguedad(), sueldoBasico)
                sumaZona = self.suma_Zona(sueldoBasico, registro[2])
                present = self.presentismo(sueldoBasico, montoAntiguedad)
                suBTotal1 = self.subTotal1(sueldoBasico, montoAntiguedad, sumaZona, present)
                jubi = self.jubilacion(suBTotal1)
                obraS = self.ObraSocial(suBTotal1, registro[3])
                suBTotal2 = self.subTotal2(jubi, obraS, self.seguro())
                tot = self.total(suBTotal1, suBTotal2)
                sql="INSERT INTO Recibo(cod_Asignar, sueldoBasico, montoAnti, sumaZona,presentismo, subTotal1, jubilacion, desObraSoial, seguro, subTotal2, total,fechaPeriodo) VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s' , '%s', '%s', '%s', '%s', '%s')" % (registro[0], sueldoBasico, montoAntiguedad, sumaZona, present, suBTotal1, jubi, obraS, self.seguro(), suBTotal2, tot, self.calcularPeriodo())
                cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()
