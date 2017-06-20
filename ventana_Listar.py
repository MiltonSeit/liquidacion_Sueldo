#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from fpdf import FPDF
import mysql.connector
import MySQLdb
from clases.cargo import *
import os, sys


def ListaDocen():
	x = 1
	cargo = Cargo()
	cargos = cargo.listarCargo()

	for resul in cargos:
		tipo1 = resul[0]
		tipo2 = resul[1]
		tipo3 = resul[2]
		tipo4 = resul[3]
		tipo5 = resul[4]
		#inserto en ListBox las variables separadas por el ancho de la columna
		lstLista.insert(x,'{:^15}{:^20}{:^39}{:^30}{:^62}'.format(tipo1,tipo2,tipo3,tipo4,tipo5))
		x =(x+1)

def ganeraPdf():
	cargo = Cargo()
	resultado = cargo.listarCargo()

	#creo pdf
	pdf=FPDF()
	pdf.set_title('Lista Docentes')
	pdf.alias_nb_pages()
	pdf.add_page()
	pdf.set_auto_page_break(True, margin = 0.0)
	pdf.set_font('Arial','B',9)
	pdf.footer()
	x="        |       "
	titulo1=('{:^20}{:^28}{:^30}{:^38}{:^42}'.format('Dni', 'Nombre', 'Direccion', 'Escuela', 'Cargo'))
	pdf.cell(0,10, titulo1,1,1)
	for regis in resultado:
		pdf.multi_cell(0,20,str(regis[0])+x+regis[1]+x+regis[2]+x+regis[3]+x+regis[4],1,'L',False)

	pdf.output('Lista-Docentes.pdf')
	os.system('evince '+'Lista-Docentes.pdf')


def colocar_scrollbar(listbox,scrollbar):
	scrollbar.config(command=listbox.yview)
	listbox.config(yscrollcommand=scrollbar.set)
	scrollbar.pack(side=RIGHT, fill=Y)
	listbox.pack(side=LEFT, fill=Y)


def ventanaListar():
	global lstLista
	punto2 = Toplevel()
	punto2.title("Listar")
	punto2.geometry("1366x768+200+200")

	medio2=Frame(punto2, width=1366, height=768)
	medio2.pack(side=BOTTOM)
	imagen1=PhotoImage(file="imagenes/turq2.png")
	lblImagen= Label(medio2, image= imagen1).place(x=0, y=0)
	lblBusc= Label(medio2,text="Muestra los datos de todos los Docentes", font=("Time", 15)).place(x=450, y=10)

	#encabezado dentro del ListBox
	titulo=('{:^22}{:^28}{:^30}{:^38}{:^72}'.format('Dni', 'Nombre', 'Direccion', 'Escuela', 'Cargo'))

	scroll1=Scrollbar(punto2)
	lstLista= Listbox(punto2, width = 100, height= 21, font=("Time", 15))
	colocar_scrollbar(lstLista,scroll1)
	lstLista.place(x= 30, y= 100)
	lstLista.insert(0, titulo)

	BotonMues = Button(medio2, text="Listar", font=("Arial", 14), relief=RIDGE, command= ListaDocen, width=19).place(x=100,y=50)
	BotonGenera = Button(medio2, text="Genera PDF", font=("Arial", 14), relief=RIDGE, command = ganeraPdf, width=19).place(x=800,y=680)
	BotonSalir = Button(medio2, text="Salir", font=("Arial", 14), relief=RIDGE, command = punto2.destroy, width=19).place(x=400,y=680)
	punto2.mainloop()
