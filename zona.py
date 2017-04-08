#!/usr/bin/python
# -*- coding: utf-8 -*-

#Definimos la clase Zona
class Zona(object):
    __cod_Zona = None
    __descripcion_Zona = None
    __porcentaje_Zona = None

    """
    * Constructor
    * @param cod_Zonal,descripcion_Zona, porcentaje_Zona
    * @return no devuelve nada
    """
    def __init__(self, cod_Zona, descripcion_Zona, porcentaje_Zona):
        self.__cod_Zona = cod_Zona
        self.__descripcion_Zona = descripcion_Zona
        self.__porcentaje_Zona = porcentaje_Zona

    """
     * Getter cod_Zona.
     * @param Ninguno.
     * @return devuelve el codigo de la Zona
     */
    """
    def getCod_Zona(self):
        return self.__cod_Zona

    """
     * Getter descripcion_Zona.
     * @param Ninguno.
     * @return devuelve la descripcion de la zona(favorable, desfavorable).
     */
    """
    def getDescripcion_Zona(self):
        return self.__descripcion_Zona

    """
     * Getter porcentaje_Zona.
     * @param Ninguno.
     * @return devuelve el porcentaje de la zona de acuerdo a la zona.
     */
    """
    def getPorcentaje_Zona(self):
        return self.__porcentaje_Zona

    """
     * Setter cod_Zona
     * @param cod_Zona.
     * @return No devuelve nada.
     */
     """
    def setCod_Zona(self, cod_Zona):
        self.__cod_Zona = cod_Zona

    """
     * Setter descripcion_Zona
     * @param descripcion_Zona.
     * @return No devuelve nada.
     */
     """
    def setDescripcion_Zona(self,descripcion_Zona):
        self.__descripcion_Zona = descripcion_Zona

    """
     * Setter porcentaje_Zona
     * @param porcentaje_Zona.
     * @return No devuelve nada.
     */
     """
    def setPorcentaje_Zona(self, porcentaje_Zona):
        self.__porcentaje_Zona = porcentaje_Zona

    cod_zona    = property(fget = getCod_Zona, fset = setCod_Zona)
    descripcion_Zona = property(fget = getDescripcion_Zona, fset = setDescripcion_Zona)
    porcentaje_Zona = property(fget = getPorcentaje_Zona, fset = setPorcentaje_Zona)
