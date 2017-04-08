#!/usr/bin/python
# -*- coding: utf-8 -*-

#Definimos la clase Cargo
    __cod_Cargo = None
    __descripcion_Cargo = None
    __puntos_Cargo = None

    """Constructor
    * @param cod_Cargo, descripcion_Cargo, puntos_Cargo
    * @return no devuelve nada
    """
    def __init__(self, cod_Cargo, descripcion_Cargo, puntos_Cargo):
        self.__cod_Cargo = cod_Cargo
        self.__descripcion_Cargo = descripcion_Cargo
        self.__puntos_Cargo = puntos_Cargo

    """Getter cod_Cargo.
     * @param Ninguno.
     * @return devuelve el codigo del cargo
     */
    """
    def getCod_Cargo(self):
        return self.__cod_Cargo

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

    """Setter cod_Cargo
     * @param cod_Cargo
     * @return No devuelve nada.
     */
     """
    def setCod_Cargo(self, cod_Cargo):
        self.__cod_Cargo = cod_Cargo

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

    cod_Cargo = property(fget = getCod_Cargo, fset = setCod_Cargo)
    descripcion_Cargo = property(fget = getDescripcion_Cargo, fset = setDescripcion_Cargo)
    puntos_Cargo = property(fget = getPuntos_Cargo, fset = setPuntos_Cargos) 
