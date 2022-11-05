# Ingreso de nuevos registros 
import numpy as np
import os
import io

#Boton ingresar 
#funcion para elegir usuario o admin
#si escoge admin ingresa credenciales 
#si son credenciales correctas despliega menu de operaciones 
#si escoge agregar usuarios 
print("Las opciones para administrador son: ")
print("1. Para Agregar ")
print("2. Para Modificar ")
print("3. Para Borrar ")
print("4. Para Mostrar ")

s=int(input("Por Favor escoja la acción que desea realizar: "))

m=2
n=3
if s==1:
  Matriz=[]
  archivo=open("matriz.txt","w")
  for i in range(2):
    Matriz.append([])
    for j in range(3):
      if j==0:
        a=input("Ingrese un nombre: ")
        Matriz[i].append(a)
        archivo.write(a+" ")
      elif j==1:
        b=input("Ingrese el documento: ")
        Matriz[i].append(b)
        archivo.write(b+" ")
      elif j==2:
        c=input("Ingrese la placa: ")
        Matriz[i].append(c)
        archivo.write(c+"\n")
  archivo.close()


#si escoge modificar 
# se recibe el parametro de cc
if s==2:
  b=input("\nIngrese el documento del usuario a modificar: ")
  archivo=open("matriz.txt", "r+")
  print(archivo.readlines())
  archivo.close()

# si escoge mostrar 
if s==4:
      archivo=open("matriz.txt")
      print(archivo.read())
      archivo.close()
      print(" ")

