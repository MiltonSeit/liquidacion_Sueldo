#!/usr/bin/python
# -*- coding: utf-8 -*-

#Definimos la clase Obra_Social
class Obra_Social(object):
    __cod_ObraSocial = None
    __nombre_Obra = None
    __descuento_Obra = None

    """
    * Constructor
    * @param cod_ObraSocial, nombre_Obra, descuento_Obra
    * @return no devuelve nada
    """
    def __init__(self, cod_ObraSocial, nombre_Obra, descuento_Obra):
        self.__cod_ObraSocial = cod_ObraSocial
        self.__nombre_Obra = nombre_Obra
        self.__descuento_Obra = descuento_Obra

    """
     * Getter cod_ObraSocial.
     * @param Ninguno.
     * @return devuelve el codigo de la obra social
     */
    """
    def getCod_ObraSocial(self):
        return self.__cod_ObraSocial

    """
     * Getter nombre_Obra.
     * @param Ninguno.
     * @return devuelve el nombre de la obra social
     */
    """
    def getNombre_Obra(self):
        return self.__nombre_Obra

    """
     * Getter descuento Obra
     * @param Ninguno.
     * @return devuelve el descuento de la obra social
     */
    """
    def getDescuento_Obra(self):
        return self.__descuento_Obra


    """
     * Setter cod_ObraSocial
     * @param cod_ObraSocial.
     * @return No devuelve nada.
     */
     """
    def setCod_ObraSocial(self, cod_ObraSocial):
        self.__cod_ObraSocial = cod_ObraSocial

    """
     * Setter nombre_Obra
     * @param nombre_Obra.
     * @return No devuelve nada.
     */
     """
    def setNombre_Obra(self,nombre_Obra):
        self.__nombre_Obra = nombre_Obra

    """
     * Setter descuento_Obra
     * @param descuento_Obra.
     * @return No devuelve nada.
     */
     """
    def setDescuento_Obra(self, descuento_Obra):
        self.__descuento_Obra = descuento_Obra

    cod_ObraSocial    = property(fget = getCod_ObraSocial, fset = setCod_ObraSocial)
    nombre_Obra = property(fget = getNombre_Obra, fset = setNombre_Obra)
    descuento_Obra = property(fget = getDescuento_Obra, fset = setDescuento_Obra)
