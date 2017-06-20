#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkMessageBox
import MySQLdb
import mysql.connector
from fpdf import FPDF
import decimal
from datetime import *
import os, sys
from cargo import Cargo

#Definimos la clase Recibo
class Recibo(object):
    __numero_Recibo = None

    """Constructor
    * @param numero_Recibo,fechaPeriodo
    * @return no devuelve nada
    """
    def __init__(self, numero_Recibo=""):
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

    """Función sueldo_Basico.
     * @param puntos.
     * @return calcula y devuelve el sueldo Básico del Docente.
     */
    """
    def sueldo_Basico(self,puntos):
        sueldoBasico = round((3.437393 * puntos),2)
        return sueldoBasico

    """Función monto_Anti.
     * @param los años y sueldo Básico.
     * @return calcula y devuelve el monto de la antigüedad.
     */
    """
    def monto_Anti(self, anios, sueldoB):
        if anios > 25:
            monto_Anti = round((1.20 * sueldoB),2)
        else:
            porcentaje= [0,0.10,0.15,0.15,0.15,0.30,0.30,0.40,0.40,0.40,0.50,0.50,0.60,0.60,0.60,0.70,0.70,0.80,0.80,0.80,1,1,1.10,1.10,1.20]
            monto_Anti = round((porcentaje[anios] * sueldoB),2)
        return monto_Anti

    """Función suma_Zona.
     * @param sueldo básico y el porcentaje de la zona.
     * @return calcula y devuelve la suma de la zona donde trabaja el doncente.
     */
    """
    def suma_Zona(self, sueldoB, porcentajeZona):
        sumaZona = round((sueldoB * porcentajeZona),2)
        return sumaZona

    """ Función presentismo.
     * @param sueldo Básico y el monto de la antiguedad.
     * @return calcula y devuelve la suma del presentismo.
     */
    """
    def presentismo(self, sueldoB,montoAnti):
        presentissmo = round(((sueldoB + montoAnti)* 0.75)*0.08 ,2)
        return presentissmo

    """ Función SubTotal1.
     * @param sueldo básico, monto Antiguedad, suma de la zona y presentismo.
     * @return calcular y devolver las ganancias del docente.
     */
    """
    def subTotal1(self, sueldoB, montoAnti, sumaZona, presentismo):
        subtotal1 = round((sueldoB + montoAnti + sumaZona + presentismo),2)
        return subtotal1

    """Función Jubilacion.
     * @param subTotal1.
     * @return calcula y devuelve el descuento de la jubilación.
     */
    """
    def jubilacion(self, subtotal1):
        montoJubilacion = round((subtotal1 * 0.20),2)
        return montoJubilacion

    """ Funcion Obra Social.
     * @param subtotal1 y descuento de la obra social.
     * @return calcula y devuelve el monto de la obra social..
     */
    """
    def obraSocial(self, subtotal1, descuento_Obra):
        descuentoObra = round((subtotal1 *  descuento_Obra),2)
        return descuentoObra

    """Funcion seguro.
     * @param .
     * @return devuelve el monto del seguro de vida.
     */
    """
    def seguro(self):
        return 300

    """Funcion subtotal2.
     * @param jubilacion, descuento de la obra social y seguro.
     * @return calcula y devuelve los descuentos hacia el docentes.
     */
    """
    def subTotal2(self, jubilacion, descuento_Obra, seguro):
        subtotal2 = round((jubilacion + descuento_Obra + seguro),2)
        return subtotal2

    """Funcion total.
     * @param subtotal1  subTotal2.
     * @return calcula y devuelve el monto final a cobrar por parte del docente.
     */
    """
    def total(self, subtotal1, subtotal2):
        montoTotal = round((subtotal1 - subtotal2),2)
        return montoTotal

    """Funcion calcularPeriodo.
     * @param ninguno.
     * @return calcula y devuelve el periodo del recibo a generar.
     */
    """
    def calcularPeriodo(self):
        mes = str(datetime.today().month)
        anio = str(datetime.today().year)
        return (mes + anio)


    """Funcion buscarPeriodo
     * @param ninguno.
     * @return devuelve el periodo del recibo.
     */
     """
    def buscarPeriodo(self):
        periodo = []
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
            cursor = bd.cursor()
            sql = "SELECT fechaPeriodo FROM Recibo;"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for registro in resultados:
                periodo.append(str(registro[0]))
            return periodo
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    """ calcularRecibo.
     * @param ninguno.
     * @return calcula y guarda el recibo.
     */
    """
    def calcularRecibo(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
            cursor = bd.cursor()
            sql="SELECT c.cod_Cargo, tp.puntos_Cargos, zon.porcentaje_Zona, obra.descuento_Obra, c.fechaIngreso  FROM Docente d INNER JOIN Cargo c on d.dni_Docente = c.dni_Docente INNER JOIN ObraSocial obra on obra.cod_ObraSocial = d.cod_ObraSocial INNER JOIN Tipo_Cargo tp on tp.cod_tipoCargo = c.cod_Cargo INNER JOIN Escuela esc on esc.numero_Escuela = c.numero_Escuela INNER JOIN Zona zon on zon.cod_Zona = esc.cod_Zona where d.activo='Y';"
            cursor.execute(sql)
            resultados = cursor.fetchall()

            for registro in resultados:
                sueldoBasico = self.sueldo_Basico(registro[1])
                cargo = Cargo(registro[0])
                montoAntiguedad = self.monto_Anti(cargo.antiguedad(registro[4]), sueldoBasico)
                sumaZona = self.suma_Zona(sueldoBasico, registro[2])
                present = self.presentismo(sueldoBasico, montoAntiguedad)
                suBTotal1 = self.subTotal1(sueldoBasico, montoAntiguedad, sumaZona, present)
                jubi = self.jubilacion(suBTotal1)
                obraS = self.obraSocial(suBTotal1, registro[3])
                suBTotal2 = self.subTotal2(jubi, obraS, self.seguro())
                tot = self.total(suBTotal1, suBTotal2)
                fechaPeriodo= self.calcularPeriodo()
                sql="INSERT INTO Recibo(cod_Cargo, sueldoBasico, montoAnti, sumaZona,presentismo, subTotal1, jubilacion, desObraSoial, seguro, subTotal2, total,fechaPeriodo) VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s' , '%s', '%s', '%s', '%s', '%s')" % (registro[0], sueldoBasico, montoAntiguedad, sumaZona, present, suBTotal1, jubi, obraS, self.seguro(), suBTotal2, tot, self.calcularPeriodo())
                cursor.execute(sql)
                bd.commit()
            tkMessageBox.showinfo("AVISO", " Los Recibos fueron insertados con exito")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    """Función crearPdf.
     * @param ninguno.
     * @return crea el pdf con el cargo del docente y lo abre.
     */
    """
    def crearPdf(self):
      periodo = "recibos"
      try:
          bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
          cursor = bd.cursor()
          sql = "SELECT DISTINCT e.nombre_Escuela,d.nomApe_Docente, d.dni_Docente, tp.descripcion_Cargo, r.numero_Recibo, r.sueldoBasico, r.montoAnti, r.sumaZona, r.presentismo, r.subTotal1, r.jubilacion,r.desObraSoial, r.seguro, r.subTotal2, r.Total, r.fechaPeriodo, c.fechaIngreso FROM Docente d INNER JOIN Cargo c on d.dni_Docente = c.dni_Docente INNER JOIN Tipo_Cargo tp on tp.cod_tipoCargo = c.cod_tipoCargo INNER JOIN Escuela e on e.numero_Escuela = c.numero_Escuela INNER JOIN Recibo r on r.cod_Cargo = c.cod_Cargo WHERE r.numero_Recibo ='%s'" % self.getNumero_Recibo()
          cursor.execute(sql)
          resultados = cursor.fetchall()
          for registro in resultados:
              escuela = str(registro[0])
              nomApe = str(registro[1])
              dni = str(registro[2])
              cargo = str(registro[3])
              numero_recibo = str(registro[4])
              sueldoBasico = str(registro[5])
              monto_Anti = str(registro[6])
              suma_Zona = str(registro[7])
              presentismo = str(registro[8])
              subTotal1 = str(registro[9])
              jubilacion = str(registro[10])
              desObraSocial = str(registro[11])
              seguro = str(registro[12])
              subTotal2 = str(registro[13])
              total = str(registro[14])
              fechaPeriodo = str(registro[15])
              ingreso = str(registro[16])
      except mysql.connector.Error as err:
          print("Something went wrong: {}".format(err))
      bd.close()
      pdf = FPDF()
      pdf.add_page()
      pdf.image('factura.jpg',5,2,200,290)
      pdf.set_font('Arial', 'B', 10)
      pdf.text(96, 72  , escuela)
      pdf.text(161, 72 , fechaPeriodo)
      pdf.text(28, 89 , nomApe)
      pdf.text(69, 89 , dni)
      pdf.text(96, 89 , cargo)
      pdf.text(161, 89 , numero_recibo)
      pdf.text(74, 115 , "$ "+sueldoBasico)
      pdf.text(74, 120 , "$ "+monto_Anti)
      pdf.text(74, 125 , "$ "+suma_Zona)
      pdf.text(74, 130 , "$ "+presentismo)
      pdf.text(74, 140,  "$ "+subTotal1)
      pdf.text(155, 116, "$ "+jubilacion)
      pdf.text(155, 121, "$ "+desObraSocial)
      pdf.text(155, 126, "$ "+seguro)
      pdf.text(150, 141, "$ "+subTotal2)
      pdf.text(145, 216, "$ "+total)
      pdf.text(29, 231 , ingreso)
      nombre = str(self.getNumero_Recibo())
      ext = '.pdf'
      salida = nombre+ext
      pdf.output(periodo+"/"+salida, 'F')
      abrir='recibos/'+str(self.getNumero_Recibo())+'.pdf'
      os.system('evince '+abrir)
