from tkinter import *
import time
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
import sys


# Ventana Usuario 
def ventana_estudiantes():
   global ventana_estudiantes
   ventana_estudiantes=Toplevel(principal)
   ventana_estudiantes.geometry("1000x500")
   ventana_estudiantes.title("ventana del Usuario")
   ventana_estudiantes.config(bg="lime green")
   ventana_estudiantes.iconbitmap("icono2.ico")

   Button(ventana_estudiantes, text="Regresar", width=20, command=volver_ventana).place(relx=0.5, rely=0.5)
   Button(ventana_estudiantes, text="Haz click aquí para generar tu código QR.", command=generar_codigo).place(x=500, y=250)       
    
   ventana_estudiantes.mainloop()

# Ventana del administrador 
def ventana_administrador():
   global ventana_administrador
   ventana_administrador=Toplevel(principal)
   ventana_administrador.geometry("1000x500")
   ventana_administrador.title("Ventana del Administrador")
   ventana_administrador.config(bg="lime green")
   ventana_administrador.iconbitmap("icono3.ico")
    
   Button(ventana_administrador, text="Regresar", width=20, command=volver_ventana2).place(x=400, y=250)
   
   ventana_administrador.mainloop()

# Volver a la ventana principal desde Usuario 
def volver_ventana():
   ventana_estudiantes.iconify()
   ventana_estudiantes.deiconify()
   ventana_estudiantes.destroy()

# Generar código qr para Usuario
def generar_codigo():
    ventana_estudiantes.iconify()
    ventana_estudiantes.deiconify()
    ventana_estudiantes.destroy()

# Volver a la ventana principal desde Administrador 
def volver_ventana2():
   ventana_administrador.iconify()
   ventana_administrador.deiconify()
   ventana_administrador.destroy()

# Estructura de la ventana principal

principal = Tk()
principal.title("Sistema de Parqueadero UIS")
principal.geometry("1000x500")
principal.iconbitmap("icono.ico")
principal.resizable(False,False)
principal.config(bg= "lime green")

# Labels principales

target = Label(principal, text="Hola, Te damos la bienvenida al Parqueadero Público de la UIS.")
target.config(fg="black", bg="lime green", font=("Bahnschrift SemiBold SemiConden", 15))
target.place(x=280, y=120)

target2 = Label(principal, text="Define que tipo de usuario eres: ")
target2.config(fg="black", bg="lime green", font=("Bahnschrift SemiBold SemiConden", 15))
target2.place(x=380 , y= 160)

target3 = Label(principal, text="Parqueadero UIS" )
target3.config(fg="black", bg="lime green", font=("Bahnschrift SemiBold SemiConden", 15))
target3.place(x=28, y=25)

def inicio():
    print("Por favor, ingresa o regístrate.")


def salir():
    messagebox.showinfo("Salida", "La app se cerrará.")
    principal.destroy()

def ayuda():
    messagebox.showwarning(message="Primero que todo debes establecer que tipo de persona eres para ingresar al Parqueadero\n\nActo seguido digitas los datos que te pidan a continuación y te asignarán un lugar en el Parqueadero :))\n\nTen un lindo día ;)",title="Prevención")


def inicio1():
    print("Por favor digita tus credenciales.")

def borrar():
     messagebox.showinfo("Reestablecer datos", "Los datos a continuación serán borrados...")
# Botones ventana principal

boton = Button(principal, text= "Usuario", command= ventana_estudiantes)
boton.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton.place(x=380 , y=220)

boton2 = Button(principal, text= "Administrativo", command= ventana_administrador)
boton2.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton2.place(x=600 , y=220)


boton3 = Button(principal, text="Salir", command=salir)
boton3.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 15))
boton3.place(x=600, y=350, width=115, height=35)

boton4 = Button(principal, text="¿Necesitas ayuda?", command=ayuda)
boton4.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton4.place(x=20, y=430, width=130, height=30)

boton5 = Button(principal, text="Reestablecer", command=borrar)
boton5.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton5.place(x=400, y=350)


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
logo = PhotoImage(file= "logo.png")
lb_logo = Label(principal, image=logo)
lb_logo.place(x=18, y=60)

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

frame_borde = Frame(principal)
frame_borde.config(bg="green4", width=1000, height=20)
frame_borde.place(x=0, y=0)

frame_borde2 = Frame(principal)
frame_borde2.config(bg="green4", width=1000, height=20)
frame_borde2.place(x=0, y=480)



# Inicio login Usuario

def aceptar():
    usuario = usuario_entry.get()
    if usuario:
        etiqueta.configure(text="Usuario: " + usuario)
    else:
        etiqueta.configure(text="Usuario no introducido")
    ventana_acceso.destroy()
    
def cancelar():
    usuario_entry.delete(0, "end")
    contraseña_entry.delete(0, "end")

def acceder():
    global ventana_acceso, usuario_entry, contraseña_entry
    
    ventana_acceso = Toplevel()
    ventana_acceso.title("Login")
    ventana_acceso.resizable(False, False)

    usuario_label = Label(ventana_acceso, text="USUARIO:")
    usuario_entry = Entry(ventana_acceso, bd=5, highlightcolor="red", highlightthickness=2)
    contraseña_label = Label(ventana_acceso, text="CONTRASEÑA:")
    contraseña_entry = Entry(ventana_acceso, bd=5, show='*', highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_acceso, text="ACEPTAR", command=aceptar)
    boton_cancelar = Button(ventana_acceso, text="CANCELAR", command=cancelar)

    usuario_label.grid(row=0, column=0, sticky= "W", padx=10, pady=10)
    usuario_entry.grid(row=0, column=1, padx=10)
    contraseña_label.grid(row=1, column=0, sticky= "W", padx=10, pady=10)
    contraseña_entry.grid(row=1, column=1, padx=10)
    boton_aceptar.grid(row=2, column=0, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=1, padx=10, pady=10, sticky= "E")

root = Tk()
root.title("Ventana de acceso")
root.geometry("300x150")
root.minsize(300, 150)
boton = Button(text="ACCEDER",command=acceder)
etiqueta = Label(text="Usuario no introducido")
boton.place(relx=0.5, rely=0.5, anchor="center")
etiqueta.pack(side="bottom", pady=5)


principal.mainloop()