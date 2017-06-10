#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkMessageBox
import MySQLdb
import mysql.connector
from fpdf import FPDF
import decimal
from datetime import *
#Definimos la clase Recibo
class Recibo(object):
    __numero_Recibo = None
    __cod_Asignar = None
    __sueldo_Basico = None
    __monto_Anti = None
    __suma_Zona = None
    __asignacion_Julio = None
    __presentismo = None
    __no_Remune = None
    __subTotal1 = None
    __jubilacion = None
    __desObraSocial = None
    __seguro = None
    __subTotal2 = None
    __total = None
    __fechaCobro = None
    __fechaPeriodo = None

    """Constructor
    * @param numero_Recibo, dni_Docente, cod_Cargo, cod_Zona, cod_Escuela, sueldo_Basico, monto_Anti, suma_Zona, asignacion_Julio, presentismo, no_Remune, subTotal1, jubilacion, desObraSocial, seguro, subTotal2, total, fechaCobro, fechaPeriodo
    * @return no devuelve nada
    """
    def __init__(self, numero_Recibo="", cod_Asignar="", sueldo_Basico="", monto_Anti="", suma_Zona="", asignacion_Julio="", presentismo="", no_Remune="", subTotal1="", jubilacion="", desObraSocial="", seguro="", subTotal2="", total="", fechaCobro="", fechaPeriodo=""):
        self.__numero_Recibo = numero_Recibo
        self.__cod_Asignar = cod_Asignar
        self.__sueldo_Basico = sueldo_Basico
        self.__monto_Anti = monto_Anti
        self.__suma_Zona = suma_Zona
        self.__asignacion_Julio = asignacion_Julio
        self.__presentismo = presentismo
        self.__no_Remune = no_Remune
        self.__subTotal1 = subTotal1
        self.__jubilacion = jubilacion
        self.__desObraSocial = desObraSocial
        self.__seguro = seguro
        self.__subTotal2 = subTotal2
        self.__total = total
        self.__fechaCobro = fechaCobro
        self.__fechaPeriodo = fechaPeriodo

    """Getter numero_Recibo.
     * @param Ninguno.
     * @return devuelve el numero del recibo
     */
    """
    def getNumero_Recibo(self):
        return self.__numero_Recibo

    """Getter cod_Asignar.
     * @param Ninguno.
     * @return devuelve el codigo de asignación.
     */
    """
    def getCod_Asignar(self):
        return self.__cod_Asignar

    """Getter sueldo_Basico.
     * @param Ninguno.
     * @return devuelve el sueldo básico del docente.
     */
    """
    def getSueldo_Basico(self):
        return self.__sueldo_Basico

    """Getter monto_Anti.
     * @param Ninguno.
     * @return devuelve el total del monto de antigüedad.
     */
    """
    def getMonto_Anti(self):
        return self.__monto_Anti

    """Getter suma_Zona.
     * @param Ninguno.
     * @return devuelve la suma de la zona.
     */
    """
    def getSuma_Zona(self):
        return self.__suma_Zona

    """Getter asignacion_Julio.
     * @param Ninguno.
     * @return devuelve la asignación de julio.
     */
    """
    def getAsignacion_Julio(self):
        return self.__asignacion_Julio

    """Getter presentismo.
     * @param Ninguno.
     * @return devuelve el presentismo total del docente.
     */
    """
    def getPresentismo(self):
        return self.__presentismo

    """Getter no_Remune.
     * @param Ninguno.
     * @return devuelve  lo remunerativo.
     */
    """
    def getNo_Remunerativo(self):
        return self.__no_Remune

    """Getter subTotal1.
     * @param Ninguno.
     * @return devuelve el total1 que son los beneficios del docentes.
     */
    """
    def getSubTotal1(self):
        return self.__subTotal1

    """Getter jubilacion.
     * @param Ninguno.
     * @return devuelve la jubilación descontada hacia el docente.
     */
    """
    def getJubilacion(self):
        return self.__jubilacion

    """Getter desObraSocial.
     * @param Ninguno.
     * @return devuelve el descuento de la obra social.
     */
    """
    def getDesObraSocial(self):
        return self.__desObraSocial

    """Getter seguro.
     * @param Ninguno.
     * @return devuelve el descuento del seguro
     */
    """
    def getSeguro(self):
        return self.__seguro

    """Getter subTotal2.
     * @param Ninguno.
     * @return devuelve el total2(son los descuentos)
     */
    """
    def getSubTotal2(self):
        return self.__subTotal2

    """Getter total.
     * @param Ninguno.
     * @return devuelve el total del codente con los descuentos.
     */
    """
    def getTotal(self):
        return self.__total

    """Getter fechaCobro.
     * @param Ninguno.
     * @return devuelve la fecha de cobro del docente.
     */
    """
    def getFechaCobro(self):
        return self.__fechaCobro

    """Getter fechaPeriodo.
     * @param Ninguno.
     * @return devuelve el periodo que va cobrar.
     */
    """
    def getFechaPeriodo(self):
        return self.__fechaPeriodo

    """Setter numero_Recibo.
     * @param numero_Recibo.
     * @return no devuelve nada.
     */
    """
    def setNumero_Recibo(self, numero_Recibo):
        self.__numero_Recibo = numero_Recibo

    """Setter cod_Asignar.
     * @param cod_Asignar.
     * @return no devuelve nada.
     */
    """
    def setCod_Asignar(self, cod_Asignar):
        self.__cod_Asignar = cod_Asignar

    """Setter sueldo_Basico.
     * @param sueldo_Basico.
     * @return no devuelve nada.
     */
    """
    def setSueldo_Basico(self, sueldo_Basico):
        self.__sueldo_Basico = sueldo_Basico

    """Setter monto_Anti.
     * @param monto_Anti.
     * @return no devuelve nada.
     */
    """
    def setMonto_Anti(self, monto_Anti):
        self.__monto_Anti = monto_Anti

    """Setter suma_Zona.
     * @param suma_Zona.
     * @return no devuelve nada.
     */
    """
    def setSuma_Zona(self, suma_Zona):
        self.__suma_Zona = suma_Zona

    """Setter asignacion_Julio.
     * @param asignacion_Julio.
     * @return no devuelve nada.
     */
    """
    def setAsignacion_Julio(self, asignacion_Julio):
        self.__asignacion_Julio = asignacion_Julio

    """Setter presentismo.
     * @param presentismo.
     * @return no devuelve nada.
     */
    """
    def setPresentismo(self, presentismo):
        self.__presentismo = presentismo

    """Setter no_Remune.
     * @param no_Remune.
     * @return no devuelve nada.
     */
    """
    def setNo_Remune(self, no_Remune):
        self.__no_Remune = no_Remune

    """Setter subTotal1.
     * @param subTotal1.
     * @return no devuelve nada.
     */
    """
    def setSubTotal1(self, subTotal1):
        self.__subTotal1 = subTotal1

    """Setter jubilacion.
     * @param jubilacion.
     * @return no devuelve nada.
     */
    """
    def setJubilacion(self, jubilacion):
        self.__jubilacion = jubilacion

    """Setter desObraSocial.
     * @param desObraSocial.
     * @return no devuelve nada.
     */
    """
    def setDesObraSocial(self, desObraSocial):
        self.__desObraSocial = desObraSocial

    """Setter seguro.
     * @param seguro.
     * @return no devuelve nada.
     */
    """
    def setSeguro(self, seguro):
        self.__seguro = seguro

    """Setter subTotal2.
     * @param subTotal2.
     * @return no devuelve nada.
     */
    """
    def setSubTotal2(self, subTotal2):
        self.__subTotal2 = subTotal2

    """Setter total.
     * @param total.
     * @return no devuelve nada.
     */
    """
    def setTotal(self, total):
        self.__total = total

    """Setter fechaCobro.
     * @param fechaCobro.
     * @return no devuelve nada.
     */
    """
    def setFechaCobro(self, fechaCobro):
        self.__fechaCobro = fechaCobro

    """Setter fechaPeriodo.
     * @param fechaPeriodo.
     * @return no devuelve nada.
     */
    """
    def setFechaPeriodo(self, fechaPeriodo):
        self.__fechaPeriodo = fechaPeriodo

    numero_Recibo = property(fget= getNumero_Recibo,fset=setNumero_Recibo)
    cod_Asignar = property(fget=getCod_Asignar,fset=setCod_Asignar)
    sueldo_Basico = property(fget=getSueldo_Basico,fset=setSueldo_Basico)
    monto_Anti = property(fget=getMonto_Anti,fset=setMonto_Anti)
    suma_Zona = property(fget=getSuma_Zona,fset=getSuma_Zona)
    asignacion_Julio = property(fget=getAsignacion_Julio,fset=setAsignacion_Julio)
    presentismo = property(fget=getPresentismo,fset=setPresentismo)
    no_Remune = property(fget=getNo_Remunerativo,fset=setNo_Remune)
    subTotal1 = property(fget=getSubTotal1,fset=setSubTotal1)
    jubilacion = property(fget=getJubilacion,fset=setJubilacion)
    desObraSocial = property(fget=getDesObraSocial,fset=setDesObraSocial)
    seguro = property(fget=getSeguro,fset=setSeguro)
    subTotal2 = property(fget=getSubTotal2,fset=setSubTotal2)
    total = property(fget=getTotal,fset=setTotal)
    fechaCobro = property(fget=getFechaCobro,fset=setFechaCobro)
    fechaPeriodo = property(fget=getFechaPeriodo,fset=setFechaPeriodo)

    def buscarRecibo(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
            cursor = bd.cursor()
            sql = "SELECT * FROM Recibo WHERE numero_Recibo ='%s'" % self.getNumero_Recibo()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for registro in resultados:
                self.setNumero_Recibo(registro[0])
                self.setCod_Asignar(registro[1])
                self.setSueldo_Basico(registro[2])
                self.setMonto_Anti(registro[3])
                self.setSuma_Zona(registro[4])
                self.setAsignacion_Julio(registro[5])
                self.setPresentismo(registro[6])
                self.setNo_Remune(registro[7])
                self.setSubTotal1(registro[8])
                self.setJubilacion(registro[9])
                self.setDesObraSocial(registro[10])
                self.setSeguro(registro[11])
                self.setSubTotal2(registro[12])
                self.setTotal(registro[13])
                self.setFechaCobro(registro[14])
                self.setFechaPeriodo(registro[15])
            self.crearPdf()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    def mostrarRecibo(self):
        print "Codigo Asignar: ",self.getCod_Asignar()
        print "Sueldo Basico: ", self.getSueldo_Basico()
        print "Monto Antiguedad ", self.getMonto_Anti()
        print "Suma Zona: ", self.getSuma_Zona()
        print "Asignacion Julio: ", self.getAsignacion_Julio()
        print "Presentismo: ",self.getPresentismo()
        print "NO remunerativo: ", self.getNo_Remunerativo()
        print "SubTotal1: ", self.getSubTotal1()
        print "Jubilacion:  ", self.getJubilacion()
        print "Desc Obra Social: ", self.getDesObraSocial()
        print "Seguro:  ", self.getSeguro()
        print "SubTotal2: ", self.getSubTotal2()
        print "Total: ", self.getTotal()
        print "Fecha Periodo: ",self.getFechaPeriodo()


    def guardarRecibo(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
            cursor = bd.cursor()
            sql="INSERT INTO Recibo(cod_Asignar, sueldoBasico, montoAnti, sumaZona, asignacion_Julio,presentismo, no_Remune, subTotal1, jubilacion, desObraSoial, seguro, subTotal2, total,fechaPeriodo) VALUES ('%s' , '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s' , '%s', '%s', '%s', '%s', '%s')" % (self.getCod_Asignar(),self.getSueldo_Basico(),self.getMonto_Anti(),self.getSuma_Zona(),self.getAsignacion_Julio(),
            self.getPresentismo(),self.getNo_Remunerativo(),self.getSubTotal1(),self.getJubilacion(),self.getDesObraSocial(),self.getSeguro(),self.getSubTotal2(),self.getTotal(),self.getFechaPeriodo())
            cursor.execute(sql)
            bd.commit()
            self.crearPdf()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    def obtenerDatosParaRecibo(self):
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
                self.calcularRecibo(cod_Asignar,sueldo_basico,porcAnti,porcZona,descObra)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    def calcularRecibo(self, cod_Asignar, sueldo_basico,porcAnti,porcZona,descObra):
        #BENEFICIOS
        self.setCod_Asignar(cod_Asignar)
        self.setSueldo_Basico(sueldo_basico)
        self.setMonto_Anti (self.getSueldo_Basico() * decimal.Decimal(porcAnti))
        self.setSuma_Zona(self.getSueldo_Basico() * decimal.Decimal(porcZona))
        self.setAsignacion_Julio(1852)
        self.setPresentismo(((self.getSueldo_Basico() + self.getMonto_Anti()) * decimal.Decimal(0.75))*decimal.Decimal(0.08))
        self.setNo_Remune(1000)
        self.setSubTotal1(self.getSueldo_Basico() + self.getMonto_Anti() + self.getSuma_Zona() + self.getAsignacion_Julio() + self.getPresentismo() + self.getNo_Remunerativo())

        mes = str(datetime.today().month)
        anio = str(datetime.today().year)
        self.setFechaPeriodo(mes+anio)

        #DESCUENTOS
        self.setJubilacion(self.getSubTotal1() * decimal.Decimal(0.20))
        self.setDesObraSocial(self.getSubTotal1() * decimal.Decimal(descObra))
        self.setSeguro(300)
        self.setSubTotal2(self.getJubilacion() + self.getDesObraSocial() + self.getSeguro())

        #TOTAL
        self.setTotal(self.getSubTotal1() - self.getSubTotal2())
        self.guardarRecibo()

    def crearPdf(self):
        try:
            escuela = " "
            apellido =" "
            nombre = " "
            dni = " "
            cargo = " "
            ingreso = " "
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
            cursor = bd.cursor()
            sql = "SELECT DISTINCT e.nombre_Escuela,d.apellido_Docente, d.nombre_Docente,d.dni_Docente, c.descripcion_Cargo,d.fechaIngreso FROM Docente d INNER JOIN Asignar a on d.dni_Docente = a.dni_Docente INNER JOIN Cargo c on c.cod_Cargo = a.cod_Cargo INNER JOIN Escuela e on e.numero_Escuela = a.numero_Escuela INNER JOIN Recibo r on r.cod_Asignar = a.cod_Asignar  WHERE numero_Recibo ='%s'" % self.getNumero_Recibo()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for registro in resultados:
                escuela = registro[0]
                apellido = registro[1]
                nombre = registro[2]
                dni = registro[3]
                cargo = registro[4]
                ingreso = registro[5]
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()
        pdf = FPDF()
        pdf.add_page()
        pdf.image('factura.jpg',5,2,200,290)
        pdf.set_font('Arial', 'B', 10)
        pdf.text(96, 72  , escuela)
        pdf.text(161, 72 , str(self.getFechaPeriodo()))
        pdf.text(28, 89 , apellido +" "+ nombre)
        pdf.text(69, 89 , dni)
        pdf.text(96, 89 , cargo)
        pdf.text(161, 89 , str(self.getNumero_Recibo()))
        pdf.text(74, 115 , str(self.getSueldo_Basico()))
        pdf.text(74, 120 , str(self.getMonto_Anti()))
        pdf.text(74, 125 , str(self.getSuma_Zona()))
        pdf.text(74, 130 , str(self.getPresentismo()))
        pdf.text(74, 140,  str(self.getSubTotal1()))
        pdf.text(155, 116, str(self.getJubilacion()))
        pdf.text(155, 121, str(self.getDesObraSocial()))
        pdf.text(155, 126, str(self.getSeguro()) )
        pdf.text(150, 141, str(self.getSubTotal2()))
        pdf.text(145, 216, str(self.getTotal()))
        pdf.text(29, 231 , ingreso)
        nombre = str(self.getNumero_Recibo())
        ext = '.pdf'
        total = nombre+ext
        pdf.output(total, 'F')
