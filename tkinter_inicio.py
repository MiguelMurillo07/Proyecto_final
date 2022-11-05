from tkinter import *

principal = Tk()

principal.title("Sistema de Parqueadero UIS")

principal.geometry("1000x500")

principal.resizable(False,False)

principal.config(bg= "purple")

target = Label(principal, text="Hola, Te damos la bienvenida al Parqueadero Público de la UIS.")
target.place(x=330, y=10)

target2 = Label(principal, text="Define que tipo de usuario eres: ")
target2.place(x=400 , y= 60)

def inicio():
    print("Por favor, ingresa o regístrate.")

boton = Button(principal, text= "Estudiante", command= inicio)
boton.place(x=230 , y=140)

def inicio1():
    print("Por favor digita tus credenciales.")

boton2 = Button(principal, text= "Administrativo", command= inicio1)
boton2.place(x=600 , y=140)


principal.mainloop()
