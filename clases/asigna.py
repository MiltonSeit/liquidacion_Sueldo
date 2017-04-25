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


    """Constructor
    * @param cod_Cargo, descripcion_Cargo, puntos_Cargo
    * @return no devuelve nada
    """
	def __init__(self, dni_Docente, cod_Cargo, cod_Escuela):

		self.__dni_Docente = dni_Docente
		self.__cod_Cargo = cod_Cargo
		self.__cod_Escuela = cod_Escuela


	"""Setter dni_Docente
     * @param dni_Docente
     * @return No devuelve nada.
     */
     """
	def __setDni_Docente(self, dni_Docente):
		self.__dni_Docente = dni_Docente

	"""Setter cod_Cargo
     * @param cod_Cargo
     * @return No devuelve nada.
     */
     """
	def __setCod_Cargo(self, cod_Cargo):
		self.__cod_Cargo = cod_Cargo

	"""Setter cod_Escuela
     * @param cod_Escuela
     * @return No devuelve nada.
     */
     """
	def __setCod_Escuela(self, cod_Escuela):
		self.__cod_Escuela = cod_Escuela


	"""Getter dni_Docente.
 	* @param Ninguno.
 	* @return devuelve el dni del docente
 	*/
	"""
	def getDni_Docente(self):
		return self.__dni_Docente

	"""Getter cod_Cargo.
 	* @param Ninguno.
 	* @return devuelve el codigo del cargo
 	*/
	"""
	def getCod_Cargo(self):
		return self.__cod_Cargo

	"""Getter cod_Escuela.
 	* @param Ninguno.
 	* @return devuelve el numero de la escuela
 	*/
	"""
	def getCod_Escuela(self):
		return self.__cod_Escuela


	"""Funcion asignarCargo
     * @param ninguno
     * @return No devuelve nada. Asigna el cargo al docente
     */
     """
	def asignarCargo(self):
		base  = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
		cursor = base.cursor()
		cursor.execute("INSERT INTO Asignar(dni_Docente, cod_Cargo,numero_Escuela)VALUES ('%s','%s','%s')" %(self.getDni_Docente(), self.getCod_Cargo(),self.getCod_Escuela()))
		base.commit()
		base.close()
