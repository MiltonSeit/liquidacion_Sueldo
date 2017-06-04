#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkMessageBox
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
        self.__subTotal2 = setSubTotal2

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

    def mostrarRecibo(self):
        print self.getNumero_Recibo()," ",self.getCod_Asignar(), " ", self.getSueldo_Basico(), " ", self.getMonto_Anti()," ", self.getSuma_Zona(), " ", self.getAsignacion_Julio()," ",
        self.getPresentismo()," ", self.getNo_Remunerativo()," ", self.getSubTotal1()," ", self.getJubilacion()," ", self.getDesObraSocial()," ", self.getSeguro()," ", self.getSubTotal2()," ", self.getTotal()," fechaC ", self.getFechaCobro()," fechaPer", self.getFechaPeriodo()

    def crearFichero(self):
        registro = open("registroRecibo.csv",'a')
        registro.write(str(self.getNumero_Recibo()))
        registro.write(",")
        registro.write(str(self.getCod_Asignar()))
        registro.write(",")
        registro.write(str(self.getSueldo_Basico()))
        registro.write(",")
        registro.write(str(self.getMonto_Anti()))
        registro.write(",")
        registro.write(str(self.getSuma_Zona()))
        registro.write(",")
        registro.write(str(self.getAsignacion_Julio()))
        registro.write(",")
        registro.write(str(self.getPresentismo()))
        registro.write(",")
        registro.write(str(self.getNo_Remunerativo()))
        registro.write(",")
        registro.write(str(self.getSubTotal1()))
        registro.write(",")
        registro.write(str(self.getJubilacion()))
        registro.write(",")
        registro.write(str(self.getDesObraSocial()))
        registro.write(",")
        registro.write(str(self.getSeguro()))
        registro.write(",")
        registro.write(str(self.getSubTotal2()))
        registro.write(",")
        registro.write(str(self.getTotal()))
        registro.write(",")
        registro.write(str(self.getFechaCobro()))
        registro.write(",")
        registro.write(str(self.getFechaPeriodo()))
        registro.write(",")
        registro.write("\n")
        registro.close()
