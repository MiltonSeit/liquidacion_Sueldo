ALTER TABLE ObraSocial   CHANGE descuento_Obra descuento_Obra real(2,2);
ALTER TABLE Antiguedad   CHANGE porc_Anti porc_Anti real(4,3);
ALTER TABLE Cargo CHANGE descripcion_Cargo descripcion_Cargo varchar(40);


UPDATE ObraSocial
SET descuento_Obra = 0.05
WHERE cod_ObraSocial = 5;

-- ***************************************************************************************************

											-- Tabla Zona
-- Valor 1:
INSERT INTO Zona(cod_Zona,descripcion_Zona)
VALUES (1,'Escuelas Urbanas',1.20);

-- Valor 2:
INSERT INTO Zona(cod_Zona,descripcion_Zona,porcentaje_Zona)
VALUES (2,'Escuelas alejadas del radio Urbano',1.50);

-- Valor 3:
INSERT INTO Zona(cod_Zona,descripcion_Zona,porcentaje_Zona)
VALUES (3,'Escuelas de ubicación Desfavorable',1.80);

-- Valor 4:
INSERT INTO Zona(cod_Zona,descripcion_Zona,porcentaje_Zona)
VALUES (4,'Escuelas de ubic. Muy Desfavorab',2.50);

-- Valor 5:--
INSERT INTO Zona(cod_Zona,descripcion_Zona,porcentaje_Zona)
VALUES (5,'Escuelas de ubicación Inhóspitas',3.0);

SELECT * FROM Zona;
-- ***************************************************************************************************

											-- Tabla Obra Social
-- Valor Obra Social 1 
INSERT INTO ObraSocial(cod_ObraSocial, nombre_Obra, descuento_Obra)
VALUES(1,'Asimira',0.06);

-- Valor Obra Social 2 --
INSERT INTO ObraSocial(cod_ObraSocial, nombre_Obra, descuento_Obra)
VALUES(2,'Medisur',0.10);

-- Valor Obra Social 3
INSERT INTO ObraSocial(cod_ObraSocial, nombre_Obra, descuento_Obra)
VALUES(3,'Sps Salud',0.11);

-- Valor Obra Social 4
INSERT INTO ObraSocial(cod_ObraSocial, nombre_Obra, descuento_Obra)
VALUES(4,'Osecac',0.03);

-- Valor Obra Social 5
INSERT INTO ObraSocial(cod_ObraSocial, nombre_Obra, descuento_Obra)
VALUES(5,'Ioscor',0.05);

SELECT *
FROM ObraSocial;

-- ***************************************************************************************************

											-- Tabla Antiguedad

-- Valor Antiguedad 0 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(1,0);

-- Valor Antiguedad 1 Año1
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(2,0.10);

-- Valor Antiguedad 2 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(3,0.15);

-- Valor Antiguedad 3 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(4,0.15);

-- Valor Antiguedad 4 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(5,0.15);

-- Valor Antiguedad 5 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(6,0.30);

-- Valor Antiguedad 6 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(7,0.30);

-- Valor Antiguedad 7 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(8,0.40);

-- Valor Antiguedad 8 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(9,0.40);

-- Valor Antiguedad 9 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(10,0.40);

-- Valor Antiguedad 10 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(11,0.50);
 
-- Valor Antiguedad 11 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(12 , 0.50);

-- Valor Antiguedad 12 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(13,0.60);

-- Valor Antiguedad 13 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(14,0.60);

-- Valor Antiguedad 14 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(15,0.60);

-- Valor Antiguedad 15 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(16,0.70);

-- Valor Antiguedad 16 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(17,0.70);

-- Valor Antiguedad 17 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(18,0.80);

-- Valor Antiguedad 18 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(19, 0.80);

-- Valor Antiguedad 19 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(20,0.80);

-- Valor Antiguedad 20 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(21,1.00);

-- Valor Antiguedad 21 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(22,1.00);

-- Valor Antiguedad 22 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(23, 1.10);

-- Valor Antiguedad 23 Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(24,1.10);

-- Valor Antiguedad 24 o MAS Años
INSERT INTO Antiguedad(cod_Antiguedad,porc_Anti)
VALUES(25,1.20);

SELECT *
FROM Antiguedad;

-- ***************************************************************************************************
											-- Tabla Cargos

-- Valor Cargo 1:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Asistente Social',1467);

-- Valor Cargo 2:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Bibliotecario',1257);
 
-- Valor Cargo 3:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Director General',5409);

-- Valor Cargo 4:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Jefe de Preceptores de Primaria',1556);

-- Valor Cargo 5:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Jefe Coordinador',1945);

-- Valor Cargo 6:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Maestro de Grado',1297);

-- Valor Cargo 7:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Maestra Grado Esc Hogar',2268);

-- Valor Cargo 8:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Maestro Especial Esc Adulto',2270);

-- Valor Cargo 9:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Rector Superior',2723);

-- Valor Cargo 10:
INSERT INTO Cargo(descripcion_Cargo,puntos_Cargo)
VALUES('Supervisor',4532);

SELECT *
FROM Cargo;
-- - ***********************************************************************************************************

											-- Tabla Escuelas

-- Escuela 1
INSERT INTO Escuela (cod_Escuela,cod_Zona,numero_Escuela,nombre_Escuela,direccion_Escuela,telefono_Escuela)
VALUES(1,1,7,'Isabel Estela Vera','3 De Abril 1236','3794438363');

-- Escuela 2
INSERT INTO Escuela (cod_Escuela,cod_Zona,numero_Escuela,nombre_Escuela,direccion_Escuela,telefono_Escuela)
VALUES(2,2,36,'Agop Seferian','Cordoba 1254','3794436543');

-- Escuela 3
INSERT INTO Escuela (cod_Escuela,cod_Zona,numero_Escuela,nombre_Escuela,direccion_Escuela,telefono_Escuela)
VALUES(3,3,25,'Bicenteario','Av Bicentenario','3794439874');

-- Escuela 4
INSERT INTO Escuela (cod_Escuela,cod_Zona,numero_Escuela,nombre_Escuela,direccion_Escuela,telefono_Escuela)
VALUES(4,4,197,'Angel Acuña','Santa Cruz 654','3794421365');

-- Escuela 5
INSERT INTO Escuela (cod_Escuela,cod_Zona,numero_Escuela,nombre_Escuela,direccion_Escuela,telefono_Escuela)
VALUES(5,5,654,'Bernardino Rivadia','Paraje Gauchito Gil','3794436514');

SELECT *
FROM Escuela;

-- -************************************************************************************************************************************                                            