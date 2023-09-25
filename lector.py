#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:18:39 2023

@author: zekibestia
"""

import csv
from AlfabetoN import alfabeto

alfa = alfabeto()
alfabeto = ['a', 'b', 'c', 'd']
datos = []

with open('datos2.csv', newline='') as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for fila in lector:
        if len(fila) >= 4:
            fila_dict = {
                'Nombre': fila[0],
                'Pal1': fila[1],
                'Pal2': fila[2],
                'Pal3': fila[3]
            }
            datos.append(fila_dict)


# Crear un archivo CSV para escribir los resultados
nombre_archivo = "resultados2.csv"

with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    
    # Escribe los encabezados en el archivo CSV
    escritor.writerow(['Nombre', 'Resultado Pal1', 'Resultado Pal2', 'Resultado Pal3'])
    
    # Escribe los nombres y resultados en el archivo CSV
    for fila_dict in datos:
        nombre = fila_dict['Nombre']
        palabra1 = fila_dict['Pal1']
        palabra2 = fila_dict['Pal2']
        palabra3 = fila_dict['Pal3']

        num1 = alfa.asignarN(alfabeto, palabra1)
        num2 = alfa.asignarN(alfabeto, palabra2)
        num3 = alfa.asignarN(alfabeto, palabra3)
        escritor.writerow([nombre, num1, num2, num3])

print(f'Se ha creado el archivo CSV "{nombre_archivo}" con los nombres y los resultados.')
