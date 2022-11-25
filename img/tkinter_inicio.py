from tkinter import *
import time
from tkinter import messagebox
import tkinter as tk
from datetime import datetime


principal = Tk()

principal.title("Sistema de Parqueadero UIS")

principal.geometry("1000x500")

principal.resizable(False,False)

principal.config(bg= "lime green")

target = Label(principal, text="Hola, Te damos la bienvenida al Parqueadero Público de la UIS.")
target.config(fg="black", bg="lime green", font=("Bahnschrift SemiBold SemiConden", 15))
target.place(x=280, y=120)

target2 = Label(principal, text="Define que tipo de usuario eres: ")
target2.config(fg="black", bg="lime green", font=("Bahnschrift SemiBold SemiConden", 15))
target2.place(x=380 , y= 160)

target3 = Label(principal, text="Parqueadero UIS" )
target3.config(fg="black", bg="lime green", font=("Bahnschrift SemiBold SemiConden", 15))
target3.place(x=20, y=20)

def inicio():
    print("Por favor, ingresa o regístrate.")


def salir():
    messagebox.showinfo("Cerrar", "La app se cerrará.")
    principal.destroy()

def ayuda():
    messagebox.showwarning(message="Primero que todo debes establecer que tipo de persona eres para ingresar al Parqueadero\n\nActo seguido digitas los datos que te pidan a continuación y te asignarán un lugar en el Parqueadero :))\n\nTen un lindo día ;)",title="Prevención")

boton = Button(principal, text= "Usuario", command= inicio)
boton.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton.place(x=340 , y=220)

def inicio1():
    print("Por favor digita tus credenciales.")

boton2 = Button(principal, text= "Administrativo", command= inicio1)
boton2.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton2.place(x=600 , y=220)


boton3 = Button(principal, text="Salir", command=salir)
boton3.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton3.place(x=890, y=420)

boton4 = Button(principal, text="¿Necesitas ayuda?", command=ayuda)
boton4.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton4.place(x=20, y=440)



# Contador reloj

def actualizar_hora():
    hora = time.strftime("%H:%M:%S")
    variable_control.set(hora)
    principal.after(1000, actualizar_hora)

variable_control = StringVar()

reloj = Label(textvariable= variable_control, bg="lime green", fg="white", font=("Bahnschrift SemiBold SemiConden", 15), padx=20, pady=20, compound="left")

reloj.pack()
reloj.place(x=900, y=35)
actualizar_hora()

# Logo app
#logo = PhotoImage(file= "logo.jpeg")
#lb_logo = Label(principal, image=logo)
#lb_logo.place(x=700, y=300)

#Widget fecha
def actualizar_fecha():
    fecha = time.strftime("%A, %B %D")
    variable_control2.set(fecha)
    principal.after(1000, actualizar_fecha)

variable_control2 = StringVar()

calendario = Label(textvariable=variable_control2, bg="lime green", fg="white", font=("Bahnschrift SemiBold SemiConden", 10), padx=20, pady=20, compound="left")
calendario.pack()
calendario.place(x=830, y=3)
actualizar_fecha()


# Frames

#Frame borde

frame_borde = Frame(principal)
frame_borde.config(bg="green4", width=1000, height=20)
frame_borde.place(x=0, y=0)

frame_borde2 = Frame(principal)
frame_borde2.config(bg="green4", width=1000, height=20)
frame_borde2.place(x=0, y=480)

principal.mainloop()