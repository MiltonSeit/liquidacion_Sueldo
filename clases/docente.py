#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkMessageBox
import MySQLdb
#Definimos la clase Docente
class Docente(object):
    __dni_Docente = None
    __cod_Antiguedad = None
    __cod_ObraSocial = None
    __nombre_Docente = None
    __apellido_Docente = None
    __direccion_Docente = None
    __telefono_Docente = None
    __fechaIngreso_Docente = None


    """Constructor
    * @param dni_Docente, cod_Antiguedad, cod_ObraSocial, nombre_Docente, apellido_Docente, direccion_Docente, telefono_Docente, fechaIngreso
    * @return no devuelve nada
    """
    def __init__(self, dni_Docente="", cod_Antiguedad="", cod_ObraSocial="", nombre_Docente="", apellido_Docente="", direccion_Docente="", telefono_Docente="", fechaIngreso=""):
        self.__dni_Docente = dni_Docente
        self.__cod_Antiguedad = cod_Antiguedad
        self.__cod_ObraSocial = cod_ObraSocial
        self.__nombre_Docente = nombre_Docente
        self.__apellido_Docente = apellido_Docente
        self.__direccion_Docente = direccion_Docente
        self.__telefono_Docente = telefono_Docente
        self.__fechaIngreso = fechaIngreso

    """Constructor con un solo parametro
    * @param dni_Docente
    * @return no devuelve nada

    def __init__(self, dni_Docente):
        self.__dni_Docente = dni_Docente
"""
    """Getter dni_Docente.
     * @param Ninguno.
     * @return devuelve el dni del Docente
     */
    """
    def getDni_Docente(self):
        return self.__dni_Docente

    """Getter cod_Antiguedad.
     * @param Ninguno.
     * @return devuelve el codigo de la Antiguedad
     */
    """
    def getCod_Antiguedad(self):
        return self.__cod_Antiguedad

    """ Getter cod_ObraSocial
     * @param Ninguno.
     * @return devuelve el codigo de la obra social.
     */
    """
    def getCod_ObraSocial(self):
        return self.__cod_ObraSocial

    """Getter nombre_Docente.
     * @param Ninguno.
     * @return devuelve el nombre del Docente
     */
    """
    def getNombre_Docente(self):
        return self.__nombre_Docente

    """Getter apellido_Docente.
     * @param Ninguno.
     * @return devuelve el apellido del Docente
     */
    """
    def getApellido_Docente(self):
        return self.__apellido_Docente

    """Getter direccion_Docente.
     * @param Ninguno.
     * @return devuelve la direccion del Docente
     */
    """
    def getDireccion_Docente(self):
        return self.__direccion_Docente

    """Getter telefono.
     * @param Ninguno.
     * @return devuelve el telefono del Docente
     */
    """
    def getTelefono_Docente(self):
        return self.__telefono_Docente

    """Getter fechaIngreso.
     *
     * @param Ninguno.
     * @return devuelve la fecha de ingreso del Docente
     */
    """
    def getFechaIngreso(self):
        return self.__fechaIngreso

    """Setter dni_Docente
     * @param dni_Docente.
     * @return No devuelve nada.
     */
     """
    def setDni_Docente(self, dni_Docente):
        self.__dni_Docente = dni_Docente

    """Setter cod_Antiguedad
     * @param cod_Antiguedad.
     * @return No devuelve nada.
     */
     """
    def setCod_Antiguedad(self, cod_Antiguedad):
        self.__cod_Antiguedad = cod_Antiguedad

    """Setter cod_ObraSocial
     * @param cod_ObraSocial.
     * @return No devuelve nada.
     */
     """
    def setCod_ObraSocial(self, cod_ObraSocial):
        self.__cod_ObraSocial = cod_ObraSocial

    """Setter nombre_Docente
     * @param nombre_Docente.
     * @return No devuelve nada.
     */
     """
    def setNombre_Docente(self, nombre_Docente):
        self.__nombre_Docente = nombre_Docente

    """Setter apellido_Docente
     * @param apellido_Docente.
     * @return No devuelve nada.
     */
     """
    def setApellido_Docente(self, apellido_Docente):
        self.__apellido_Docente = apellido_Docente

    """Setter direccion_Docente
     * @param direccion_Docente.
     * @return No devuelve nada.
     */
     """
    def setDireccion_Docente(self, direccion_Docente):
        self.__direccion_Docente = direccion_Docente

    """Setter telefono_Docente
     * @param telefono_Docente.
     * @return No devuelve nada.
     */
     """
    def setTelefono_Docente(self, telefono_Docente):
        self.__telefono_Docente = telefono_Docente

    """Setter fechaIngreso
     * @param fechaIngreso.
     * @return No devuelve nada.
     */
     """
    def setFechaIngreso(self, fechaIngreso):
        self.__fechaIngreso = fechaIngreso

    dni_Docente    = property(fget = getDni_Docente, fset = setDni_Docente)
    cod_Antiguedad   = property(fget = getCod_Antiguedad, fset = setCod_Antiguedad)
    cod_ObraSocial    = property(fget = getCod_ObraSocial, fset = setCod_ObraSocial)
    nombre_Docente   = property(fget = getNombre_Docente, fset = setNombre_Docente)
    apellido_Docente    = property(fget = getApellido_Docente, fset = setApellido_Docente)
    direccion_Docente    = property(fget = getDireccion_Docente, fset = setDireccion_Docente)
    telefono_Docente    = property(fget = getTelefono_Docente, fset = setTelefono_Docente)
    fechaIngreso    = property(fget = getFechaIngreso, fset = setFechaIngreso)

    """Funcion buscarDocente
     * @param ninguno.
     * @return devuelve si el docente se encuentra en la DB o no.
     */
     """
    def buscarDocente(self):
        bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
        cursor = bd.cursor()
        ent_dni = self.getDni_Docente()
        sql = "SELECT dni_Docente FROM Docente WHERE dni_Docente ='%s'" % ent_dni
        try:
       # Ejecutamos el comando
            cursor.execute(sql)
       # Obtenemos todos los registros en una lista de listas
            resultados = cursor.fetchall()

            return resultados

        except:
            print "Error: No se pudo obtener los datos del docente"
    # Nos desconectamos de la base de datos
        bd.close()

    """Funcion altaDocente
     * @param ninguno.
     * @return No devuelve nada. Agrega el docente.
     */
     """
    def altaDocente(self):
        if self.buscarDocente():
            tkMessageBox.showinfo("AVISO", " El Docente'  " + self.getNombre_Docente() + " ' Se encuentra registrado")
        else:
            conn = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Docente (dni_Docente,cod_Antiguedad, cod_ObraSocial, nombre_Docente, apellido_Docente, direccion_Docente, telefono_Docente, fechaIngreso)VALUES ('%s' , '%s', '%s', '%s', '%s', '%s', '%s', '%s') " % (self.getDni_Docente(), self.getCod_Antiguedad(), self.getCod_ObraSocial(), self.getNombre_Docente(), self.getApellido_Docente(), self.getDireccion_Docente(), self.getTelefono_Docente(), self.getFechaIngreso()))
            conn.commit()
            conn.close()
            tkMessageBox.showinfo("AVISO", " El Docente'  " + self.getNombre_Docente() + " ' fue insertado con exito")


    """Funcion mostrarDocente
     * @param ninguno.
     * @return devuelve los datos del docente.
     */
     """
    def mostrarDocente(self):
        print self.getDni_Docente(), self.getCod_Antiguedad(), self.getCod_ObraSocial(), self.getNombre_Docente(), self.getApellido_Docente(), self.getDireccion_Docente(), self.getTelefono_Docente(), self.getFechaIngreso()

    """Funcion modificarDocente
     * @param ninguno.
     * @return modificar los datos del docente.
     */
     """
    def modificarDocente(self):
        datosDocente = self.buscarDocente()
        print datosDocente
