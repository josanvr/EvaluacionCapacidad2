"""
Created on Mon May 30 14:07:59 2022
@author: Andres Vera
"""

import gestion_archivos

def menu():
    print("******MENU PRINCIPAL*******")
    print("1. Crear Archivo")
    print("2. Agregar Contenido")
    print("3. Mostrar contenido del Archivo")
    print("4. Eliminar Archivo")
    print("5. Salir")
    
def crear():
    print("--Crear Archivo--")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.crear_archivo(archivo, contenido)
    