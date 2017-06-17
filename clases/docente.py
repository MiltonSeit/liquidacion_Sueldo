#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkMessageBox
import MySQLdb
import mysql.connector

#Definimos la clase Docente
class Docente(object):
    __dni_Docente = None
    __codigo_ObraSocial = None
    __nomApe_Docente = None
    __direccion_Docente = None
    __telefono_Docente = None


    """Constructor
    * @param dni_Docente, codigo_ObraSocial, nomApe_Docente, direccion_Docente, telefono_Docente,
    * @return no devuelve nada
    """
    def __init__(self, dni_Docente="",codigo_ObraSocial="", nomApe_Docente="",direccion_Docente="", telefono_Docente=""):
        self.__dni_Docente = dni_Docente
        self.__codigo_ObraSocial = codigo_ObraSocial
        self.__nomApe_Docente = nomApe_Docente
        self.__direccion_Docente = direccion_Docente
        self.__telefono_Docente = telefono_Docente

    """Getter dni_Docente.
     * @param Ninguno.
     * @return devuelve el dni del Docente
     */
    """
    def getDni_Docente(self):
        return self.__dni_Docente

    """ Getter codigo_ObraSocial
     * @param Ninguno.
     * @return devuelve el nombre de la obra social.
     */
    """
    def getCodigo_ObraSocial(self):
        return self.__codigo_ObraSocial

    """Getter nomApe_Docente.
     * @param Ninguno.
     * @return devuelve el nomApe del Docente
     */
    """
    def getNomApe_Docente(self):
        return self.__nomApe_Docente

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

    """Setter dni_Docente
     * @param dni_Docente.
     * @return No devuelve nada.
     */
     """
    def setDni_Docente(self, dni_Docente):
        self.__dni_Docente = dni_Docente

    """Setter codigo_ObraSocial
     * @param codigo_ObraSocial.
     * @return No devuelve nada.
     */
     """
    def setCodigo_ObraSocial(self, codigo_ObraSocial):
        self.__codigo_ObraSocial = codigo_ObraSocial

    """Setter nomApe_Docente
     * @param nomApe_Docente.
     * @return No devuelve nada.
     */
     """
    def setNomApe_Docente(self, nomApe_Docente):
        self.__nomApe_Docente = nomApe_Docente

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

    dni_Docente    = property(fget = getDni_Docente, fset = setDni_Docente)
    codigo_ObraSocial    = property(fget = getCodigo_ObraSocial, fset = setCodigo_ObraSocial)
    nomApe_Docente   = property(fget = getNomApe_Docente, fset = setNomApe_Docente)
    direccion_Docente    = property(fget = getDireccion_Docente, fset = setDireccion_Docente)
    telefono_Docente    = property(fget = getTelefono_Docente, fset = setTelefono_Docente)

    """Funcion buscarDocente
     * @param ninguno.
     * @return devuelve si el docente se encuentra en la DB o no.
     */
     """
    def buscarDocente(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
            cursor = bd.cursor()
            sql = "SELECT * FROM Docente WHERE dni_Docente ='%s'" % self.getDni_Docente()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for registro in resultados:
                dni = registro[0]
                obraSocial = registro[1]
                nomApe = registro[2]
                direccion = registro[3]
                telefono = registro[4]
                activo= registro[5]
            lista = [dni, obraSocial, nomApe, direccion, telefono,activo]
            return lista
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    """Funcion agregarDocente
     * @param ninguno.
     * @return No devuelve nada. Agrega el docente a la BASE DE DATOS.
     */
     """
    def agregarDocente(self):
        try:
            conn = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Docente (dni_Docente, cod_ObraSocial, nomApe_Docente, direccion_Docente, telefono_Docente,activo)VALUES ('%s' , '%s', '%s', '%s', '%s', '%s') " % (self.getDni_Docente(), self.getCodigo_ObraSocial(), self.getNomApe_Docente(), self.getDireccion_Docente(), self.getTelefono_Docente(),'Y'))
            conn.commit()
            conn.close()
            tkMessageBox.showinfo("AVISO", " El Docente '" + self.getDni_Docente() +"' fue insertado con exito")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    """Funcion modificarDocente
     * @param ninguno.
     * @return modificar los datos del docente.
     */
     """
    def modificarDocente(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
            cursor = bd.cursor()
            ent_dni = self.getDni_Docente()
            cursor.execute ("UPDATE Docente SET dni_Docente='%s',cod_Antiguedad='%s', cod_ObraSocial='%s', nombre_Docente='%s', apellido_Docente='%s', direccion_Docente='%s', telefono_Docente='%s', fechaIngreso='%s' WHERE dni_Docente='%s' " % (self.getDni_Docente(), self.getCod_Antiguedad(), self.getCod_ObraSocial(), self.getNombre_Docente(), self.getApellido_Docente(), self.getDireccion_Docente(),self.getTelefono_Docente(), self.getFechaIngreso(),self.getDni_Docente()))
            bd.commit()
            tkMessageBox.showinfo("AVISO", " El Docente '" + self.getNombre_Docente() +"' se ha modificado con exito")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    """Funcion bajaDocente
     * @param ninguno.
     * @return da de baja al docente que se encuentra activo..
     */
     """
    def bajaDocente(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
            cursor = bd.cursor()
            cursor.execute ("UPDATE Docente SET activo='%s' WHERE dni_Docente='%s' " % ('N',self.getDni_Docente()))
            bd.commit()
            tkMessageBox.showinfo("AVISO", " El Docente '" + self.getDni_Docente() +"' se ha dado de baja con éxito")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()

    """Función altaDocente
    * @param no recibe ninguno.
    * @return da de alta el usuario que estaba dado de baja.
    """
    def altaDocente(self):
        try:
            bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
            cursor = bd.cursor()
            cursor.execute("UPDATE Docente SET activo='%s' WHERE dni_Docente='%s'" % ('Y',self.getDni_Docente()))
            bd.commit()
            tkMessageBox.showinfo("AVISO", " El Docente '" + self.getDni_Docente() +"' se ha dado de alta con éxito")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        bd.close()
