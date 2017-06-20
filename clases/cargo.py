#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import tkMessageBox
import mysql.connector
from datetime import *

class Cargo(object):
	__cod_Cargo = None
	__dni_Docente = None
	__cod_Escuela = None
	__fechaIngreso = None


	"""Constructor
	* @param cod_Cargo, descripcion_Cargo, puntos_Cargo, fechaIngreso
	* @return no devuelve nada
	"""
	def __init__(self, dni_Docente="", cod_Cargo="", cod_Escuela="", fechaIngreso=""):
		self.__dni_Docente = dni_Docente
		self.__cod_Cargo = cod_Cargo
		self.__cod_Escuela = cod_Escuela
		self.__fechaIngreso = fechaIngreso

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

	"""Función antiguedad
	* @param no recibe ningún parámetro
	* @return devuelve la cantidad de años que ejerce como Docente
	"""
	def antiguedad(self, fecha_ingreso):
		fechActual = datetime.now()
		formato = "%d/%m/%Y"
		fecha_ingreso = datetime.strptime(fecha_ingreso, formato)
		diferencia = (fechActual - fecha_ingreso)
		resultado = (diferencia/365)
		anios = resultado.days
		if anios > 24:
			return 25
		else:
			return anios

	"""Funcion asignarCargo
     * @param ninguno
     * @return No devuelve nada. Asigna el cargo al docente
     */
     """
	def asignarCargo(self):
		base  = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
		cursor = base.cursor()
		cursor.execute("INSERT INTO Cargo(dni_Docente, cod_tipoCargo,numero_Escuela, fechaIngreso)VALUES ('%s','%s','%s','%s')" %(self.getDni_Docente(), self.getCod_Cargo(),self.getCod_Escuela(),self.getFechaIngreso()))
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
			sql="SELECT DISTINCT r.numero_Recibo, d.nomApe_Docente, tp.descripcion_Cargo, e.nombre_Escuela,r.fechaPeriodo from Docente d INNER JOIN Cargo c on d.dni_Docente = c.dni_Docente INNER JOIN Tipo_Cargo tp on tp.cod_tipoCargo = c.cod_tipoCargo INNER JOIN Escuela e on e.numero_Escuela = c.numero_Escuela INNER JOIN Recibo r on r.cod_Cargo = c.cod_Cargo where c.dni_Docente = %s;" % self.getDni_Docente()
			cursor.execute(sql)
			resultados = cursor.fetchall()
			lista = []
			for registro in resultados:
				idRecibo = registro[0]
				nomApeDocente = registro[1]
				descripcionCargo = registro[2]
				nombreEscuela = registro[3]
				fechaPeriodo = registro[4]
				elementos = [idRecibo,nomApeDocente, descripcionCargo, nombreEscuela, fechaPeriodo]
				lista.append(elementos)
			return lista
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
		bd.close()

	def listarCargo(self):
		base = MySQLdb.connect("localhost","root","gogole","Recibo_Sueldo" )
		cursor = base.cursor()
		sql= ("SELECT d.dni_Docente, d.nomApe_Docente , d.direccion_Docente , e.nombre_Escuela , c.descripcion_Cargo FROM Cargo a INNER JOIN Docente d on d.dni_Docente = a.dni_Docente INNER JOIN Escuela e on e.numero_Escuela = a.numero_Escuela INNER JOIN Tipo_Cargo c on c.cod_tipoCargo = a.cod_Cargo where d.activo like 'Y'")
		cursor.execute(sql)
		resul = cursor.fetchall()
		base.close()
		return resul
