#!/usr/bin/python
# -*- coding: utf-8 -*-

#Definimos la clase Cargo
class Tipo_Cargo(object):
    __cod_TipoCargo = None
    __descripcion_Cargo = None
    __puntos_Cargo = None

    """Constructor
    * @param cod_TipoCargo, descripcion_Cargo, puntos_Cargo
    * @return no devuelve nada
    """
    def __init__(self, cod_TipoCargo, descripcion_Cargo, puntos_Cargo):
        self.__cod_TipoCargo = cod_TipoCargo
        self.__descripcion_Cargo = descripcion_Cargo
        self.__puntos_Cargo = puntos_Cargo

    """Getter cod_TipoCargo.
     * @param Ninguno.
     * @return devuelve el codigo del cargo
     */
    """
    def getCod_TipoCargo(self):
        return self.__cod_TipoCargo

    """Getter descripcion del cargo.
     * @param Ninguno.
     * @return devuelve la descripcion del cargo ocupado
     */
    """
    def getDescripcion_Cargo(self):
        return self.__descripcion_Cargo

    """Getter descripcion del cargo.
     * @param Ninguno.
     * @return devuelve los puntos del cargo
     */
    """
    def getPuntos_Cargo(self):
        return self.__puntos_Cargo

    """Setter cod_TipoCargo
     * @param cod_TipoCargo
     * @return No devuelve nada.
     */
     """ 
    def setCod_TipoCargo(self, cod_TipoCargo):
        self.__cod_TipoCargo = cod_TipoCargo

    """Setter descripcion_Cargo
     * @param descripcion_Cargo
     * @return No devuelve nada.
     */
     """
    def setDescripcion_Cargo(self, descripcion_Cargo):
        slef.__descripcion_Cargo = descripcion_Cargo

    """Setter puntos_Cargo
     * @param puntos_Cargo
     * @return No devuelve nada.
     */
     """
    def setPuntos_Cargos(self, puntos_Cargo):
        self.__puntos_Cargo = puntos_Cargo

    cod_TipoCargo = property(fget = getCod_TipoCargo, fset = setCod_TipoCargo)
    descripcion_Cargo = property(fget = getDescripcion_Cargo, fset = setDescripcion_Cargo)
    puntos_Cargo = property(fget = getPuntos_Cargo, fset = setPuntos_Cargos)
