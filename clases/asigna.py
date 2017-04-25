#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import MySQLdb
import tkMessageBox

class Asigna(object):

	__cod_asigna = None
	__dni_Docente = None
	__cod_Cargo = None
	__cod_Escuela = None



	def __init__(self, dni_Docente, cod_Cargo, cod_Escuela):

		self.__dni_Docente = dni_Docente
		self.__cod_Cargo = cod_Cargo
		self.__cod_Escuela = cod_Escuela



	def __setDni_Docente(self, dni_Docente):
		self.__dni_Docente = dni_Docente

	def __setCod_Cargo(self, cod_Cargo):
		self.__cod_Cargo = cod_Cargo

	def __setCod_Escuela(self, cod_Escuela):
		self.__cod_Escuela = cod_Escuela



	def getDni_Docente(self):
		return self.__dni_Docente

	def getCod_Cargo(self):
		return self.__cod_Cargo

	def getCod_Escuela(self):
		return self.__cod_Escuela



	def asignarCargo(self):
		base  = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
		cursor = base.cursor()
		cursor.execute("INSERT INTO Asignar(dni_Docente, cod_Cargo,numero_Escuela)VALUES ('%s','%s','%s')" %(self.getDni_Docente(), self.getCod_Cargo(),self.getCod_Escuela()))
		base.commit()
		base.close()
