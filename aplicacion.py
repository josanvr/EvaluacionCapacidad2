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
    
def agregar():
    print("--Agregar datos a un archivo--")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)

def listar():
    print("--Mostrar contenido de un archivo--")
    archivo = input("Archivo: ")
    print(gestion_archivos.leer_archivo(archivo)+"\n")

def eliminar():
    print("--Eliminar Archivo--")
    archivo = input("Archivo: ")
    gestion_archivos.eliminar_archivo(archivo)

def salir():
    print("Gracias por su visita...\n")
    
def error():
    print("Opcion incorrecta\n")
    
opcion = 1
while opcion!= 5:
    menu()
    opcion= int(input("opcion: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        agregar()
    elif opcion == 3:
        listar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        salir()
    else:
        error()