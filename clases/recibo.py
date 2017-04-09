#!/usr/bin/python
# -*- coding: utf-8 -*-

#Definimos la clase Recibo
class Recibo(object):
    __numero_Recibo = None
    __dni_Docente = None
    __cod_Cargo = None
    __cod_Zona = None
    __cod_Escuela = None
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
    def __init__(self, numero_Recibo, dni_Docente, cod_Cargo, cod_Zona, cod_Escuela, sueldo_Basico, monto_Anti, suma_Zona, asignacion_Julio, presentismo, no_Remune, subTotal1, jubilacion, desObraSocial, seguro, subTotal2, total, fechaCobro, fechaPeriodo):
        self.__numero_Recibo = numero_Recibo
        self.__dni_Docente = dni_Docente
        self.__cod_Cargo = cod_Cargo
        self.__cod_Zona = cod_Zona
        self.__cod_Escuela = cod_Escuela
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

    """Getter dni_Docente.
     * @param Ninguno.
     * @return devuelve el dni del docente
     */
    """
    def getDni_Docente(self):
        return self.__dni_Docente

    """Getter cod_Cargo.
     * @param Ninguno.
     * @return devuelve el codigo de cargo del docente.
     */
    """
    def getCod_Cargo(self):
        return self.__cod_Cargo

    """Getter cod_Zona.
     * @param Ninguno.
     * @return devuelve el codigo de la zona en la que se encuentra el cliente.
     */
    """
    def getCod_Zona(self):
        return self.__cod_Zona

    """Getter cod_Escuela.
     * @param Ninguno.
     * @return devuelve el codigo de la escuela en la que trabaja el cliente.
     */
    """
    def getCod_Escuela(self):
        return self.__cod_Escuela

    """Getter sueldo_Basico.
     * @param Ninguno.
     * @return devuelve el sueldo básico del cliente.
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
        return suma_Zona

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

    """Setter dni_Docente.
     * @param dni_Docente.
     * @return no devuelve nada.
     */
    """
    def setDni_Docente(self, dni_Docente):
        self.__dni_Docente = dni_Docente

    """Setter cod_Cargo.
     * @param cod_Cargo.
     * @return no devuelve nada.
     */
    """
    def setCod_Cargo(self, cod_Cargo):
        self.__cod_Cargo = cod_Cargo

    """Setter cod_Zona.
     * @param cod_Zona.
     * @return no devuelve nada.
     */
    """
    def setCod_Zona(self, cod_Zona):
        self.__cod_Zona = cod_Zona

    """Setter cod_Escuela.
     * @param cod_Escuela.
     * @return no devuelve nada.
     */
    """
    def setCod_Escuela(self, cod_Escuela):
        self.__cod_Escuela = cod_Escuela

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
