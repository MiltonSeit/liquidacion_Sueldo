#!/usr/bin/python
# -*- coding: utf-8 -*-

#Definimos la clase Antigüedad
class Antiguedad(object):
    __cod_Antiguedad = None
    __porc_Anti = None


    """
    * Constructor
    * @param cod_Antiguedad, porc_Anti
    * @return no devuelve nada
    """
    def __init__(self, cod_Antiguedad, porc_Anti):
        self.__cod_Antiguedad = cod_Antiguedad
        self.__porc_Anti = porc_Anti

    """
     * Getter cod_Antiguedad.
     * @param Ninguno.
     * @return devuelve el codigo de la antigüedad.
     */
    """
    def getCod_Antiguedad(self):
        return self.__cod_Antiguedad

    """
     * Getter porc_Anti
     * @param Ninguno.
     * @return devuelve el porcentaje de la Obra Social.
     */
    """
    def getPorc_Anti(self):
        return self.__porc_Anti

    """
     * Setter cod_Antiguedad
     * @param cod_Antiguedad.
     * @return No devuelve nada.
     */
     """
    def setCod_Antiguedad(self, cod_Antiguedad):
        self.__cod_Antiguedad = cod_Antiguedad

    """
     * Setter porc_Anti
     * @param porc_Anti
     * @return No devuelve nada.
     */
     """
    def setPorc_Anti(self,porc_Anti):
        self.__porc_Anti = porc_Anti


    cod_ObraSociala    = property(fget = getCod_ObraSocial, fset = setCod_ObraSocial)
    nombre_Obra = property(fget = getNombre_Obra, fset = setNombre_Obra)
    descuento_Obra = property(fget = getDescuento_Obra, fset = setDescuento_Obra)
