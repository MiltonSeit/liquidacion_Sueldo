#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import MySQLdb
import tkMessageBox
import mysql.connector

class Asigna(object):

	__cod_asigna = None
	__dni_Docente = None
	__cod_Cargo = None
	__cod_Escuela = None
	__fechaIngreso = None


	"""Constructor
	* @param cod_Cargo, descripcion_Cargo, puntos_Cargo, fechaIngreso
	* @return no devuelve nada
	"""
	def __init__(self, dni_Docente, cod_Cargo="", cod_Escuela="", fechaIngreso=""):
		self.__dni_Docente = dni_Docente
		self.__cod_Cargo = cod_Cargo
		self.__cod_Escuela = cod_Escuela
		self.__fechaIngreso


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


	"""Setter fechaIngreso
	* @param fechaIngreso
	* @no devuelve nada.
	*/
	"""
	def _setfechaIngreso(self, fechaIngreso):
		self.__fechaIngreso = fechaIngreso


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

	"""Getter fechaIngreso.
 	* @param Ninguno.
 	* @return devuelve la fecha de ingreso del cargo del docente
 	*/
	"""
	def getFechaIngreso(self):
		return self.__fechaIngreso

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
		tkMessageBox.showinfo("AVISO", " El Cargo de '  " + self.getDni_Docente() + " ' fue insertado con exito")

	"""Funcion buscarCargos
	* @param ninguno
	* @return devuelve los datos de los docentes con sus cargos
	*/
	"""
	def buscarCargos(self):
		try:
			bd = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo")
			cursor = bd.cursor()
			dnis = int(self.getDni_Docente())
			sql="SELECT DISTINCT r.numero_Recibo, d.nombre_Docente, d.apellido_Docente, c.descripcion_Cargo, e.nombre_Escuela,r.fechaPeriodo from Docente d INNER JOIN Asignar a on d.dni_Docente = a.dni_Docente INNER JOIN Cargo c on c.cod_Cargo = a.cod_Cargo INNER JOIN Escuela e on e.numero_Escuela = a.numero_Escuela INNER JOIN Recibo r on r.cod_Asignar = a.cod_Asignar where a.dni_Docente = %s;" % self.getDni_Docente()
			cursor.execute(sql)
			resultados = cursor.fetchall()
			lista = []
			for registro in resultados:
				idRecibo = registro[0]
				nombreDocente = registro[1]
				apellidoDocente = registro[2]
				descripcionCargo = registro[3]
				nombreEscuela = registro[4]
				fechaPeriodo = registro[5]
				elementos = [idRecibo,nombreDocente, apellidoDocente, descripcionCargo, nombreEscuela, fechaPeriodo]
				lista.append(elementos)
			return lista
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
		bd.close()

	def mostrarCargo(self,idRecibo,nombreDocente, apellidoDocente, descripcionCargo, nombreEscuela, fechaPeriodo):
		lista = [idRecibo,nombreDocente, apellidoDocente, descripcionCargo, nombreEscuela, fechaPeriodo]
		return lista
