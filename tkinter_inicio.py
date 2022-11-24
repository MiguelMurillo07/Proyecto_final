from tkinter import *
import time


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

# Contador reloj

def actualizar_hora():
    hora = time.strftime("%H:%M:%S")
    variable_control.set(hora)
    root.after(1000, actualizar_hora)

root = Tk()
root.resizable(False, False)

variable_control = StringVar()

reloj = Label(textvariable= variable_control, fg="red", font=("Arial", 18), padx=20, pady=20, bitmap="hourglass", compound="left")
reloj = Label(textvariable= variable_control, fg="red", font=("Arial", 18), padx=20, pady=20)
reloj.pack()

actualizar_hora()
root.mainloop()
principal.mainloop()