#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Creamos una tupla con el orden de las letras
letras = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
#También podríamos haber creado una cadena "string" ya que podemos tratarla como una tupla.
#letras = 'TRWAGMYFPDXBNJZSQVHLCKE'

# Solicitamos el número de DNI
dni = int(input('Dame el numero de tu DNI:'))
# Comprobamos que la longitud del DNI sea de 8 dígitos
longitud = len(str(dni))
if  longitud <= 8 :
	# Sacamos el resto de la división
	resto = dni % 23
	# Imprimimos el resultado
	print('La letra de tu DNI es la' , (letras[resto]))
	print('Tu DNI completo es: ' , str(dni) + '-' + (letras[resto]))
	input('Pulsa enter para salir.')
else:
	print('El DNI introducido tiene una longitud de más de 8 números.\nIntroduce un DNI correcto.')

