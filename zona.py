#!/usr/bin/python
# -*- coding: utf-8 -*-


#Definimos la clase Docente
class Zona(object):
    __cod_Zona = None
    __descripcion_Zona = None
    __porcentaje_Zona

    """Instanciador"""
    def __init__(self, cod_Zona, descripcion_Zona, porcentaje_Zona):
        self.__cod_Zona = cod_Zona
        self.__descripcion_Zona = descripcion_Zona
        self.__porcentaje_Zona

    def getCod_Zona(self):
        return self.__cod_Zona

    def getDescripcion_Zona(self):
        return self.__descripcion_Zona

    def getPorcentaje_Zona(self):
        return self.__porcentaje_Zona

    def setCod_Zona(self, cod_Zona):
        self.__cod_Zona = cod_Zona

    def setDescripcion_Zona(self,descripcion_Zona):
        self.__descripcion_Zona = des

    def setPorcentaje_Zona(self, porcentaje_Zona):
        self.__porcentaje_Zona = porcentaje_Zona

    cod_zona    = property(fget = getCod_Zona, fset = setCod_Zona)
    descripcion_Zona = property(fget = getDescripcion_Zona, fset = setDescripcion_Zona)
    porcentaje_Zona = property(fget = getPorcentaje_Zona, fset = setPorcentaje_Zona)

    
