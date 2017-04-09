#!/usr/bin/python
# -*- coding: utf-8 -*-

#Definimos la clase Escuela
class Escuela(object):
    __cod_Escuela = None
    __cod_Zona = None
    __numero_Escuela = None
    __nombre_Escuela = None
    __direccion_Escuela = None
    __telefono_Escuela = None

    """Constructor
    * @param cod_Escuela, cod_Zona, numero_Escuela, nombre_Escuela, direccion_Escuela,, telefono_Escuela
    * @return no devuelve nada
    """
    def __init__(self, cod_Escuela, cod_Zona, numero_Escuela, nombre_Escuela, direccion_Escuela, telefono_Escuela):
        self.__cod_Escuela = cod_Escuela
        self.__cod_Zona = cod_Zona
        self.__numero_Escuela = numero_Escuela
        self.__nombre_Escuela = nombre_Escuela
        self.__direccion_Escuela = direccion_Escuela
        self.__telefono_Escuela = telefono_Escuela

    """Getter cod_Escuela.
     * @param Ninguno.
     * @return devuelve el copdigo de la escuela
     */
    """
    def getCod_Escuela(selg):
        return self.__cod_Escuela

    """Getter cod_zona.
     * @param Ninguno.
     * @return devuelve el codigo de la zona de la escuela
     */
    """
    def getCod_Zona(self):
        return self.__cod_Zona

    """Getter numero_Escuela.
     * @param Ninguno.
     * @return devuelve el numero de la escuela.
     */
    """
    def getNumero_Escuela(self):
        return self.__numero_Escuela

    """Getter nombre_Escuela.
     * @param Ninguno.
     * @return devuelve el nombre de la escuela
     */
    """
    def getNombre_Escuela(self):
        return self.__nombre_Escuela

    """Getter direccion_Escuela.
     * @param Ninguno.
     * @return devuelve la direccion de la escuela
     */
    """
    def getDireccion_Escuela(self):
        return self.__direccion_Escuela

    """Getter telefono_Escuela.
     * @param Ninguno.
     * @return devuelve el telefono de la escuela
     */
    """
    def getTelefono_Escuela(self):
        return self.__telefono_Escuela

    """Setter cod_Escuela
     * @param cod_Escuela.
     * @return No devuelve nada.
     */
    """
    def setCod_Escuela(self, cod_Escuela):
        self.__cod_Escuela = cod_Escuela

    """Setter cod_Zona
     * @param cod_Zona.
     * @return No devuelve nada.
     */
    """
    def setCod_Zona(self, cod_Zona):
        self.__cod_Zona = cod_Zona

    """Setter numero_Escuela
    * @param numero_Escuela.
    * @return No devuelve nada.
    */
    """
    def setNumero_Escuela(self, numero_Escuela):
        self.__numero_Escuela = numero_Escuela

    """Setter nombre_Escuela
     * @param nombre_Escuela.
     * @return No devuelve nada.
     */
    """
    def setNombre_Escuela(self, nombre_Escuela):
        self.__nombre_Escuela = nombre_Escuela


    """Setter direccion_Escuela
     * @param direccion_Escuela.
     * @return No devuelve nada.
     */
    """
    def setDireccion_Escuela(self, direccion_Escuela):
        self.__direccion_Escuela = direccion_Escuela

    """Setter telefono_Escuela
     * @param telefono_Escuela.
     * @return No devuelve nada.
     */
    """
    def setTelefono_Escuela(self, telefono_Escuela):
        self.__telefono_Escuela = telefono_Escuela

    cod_Escuela = property(fget = getCod_Escuela, fset = setCod_Escuela)
    cod_Zona = property (fget = cod_Zona, fset = setCod_Zona)
    numero_Escuela = property (fget = getNumero_Escuela, fset =setNumero_Escuela)
    nombre_Escuela = property (fget = getNombre_Escuela, fset = nombre_Escuela)
    direccion_Escuela = property (fget = getDireccion_Escuela, fset =setDireccion_Escuela)
    telefono_Escuela = property (fget = getTelefono_Escuela, fset = telefono_Escuela)
