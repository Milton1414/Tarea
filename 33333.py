from tkinter import *

# Función para mostrar un mensaje cuando se hace clic en el Checkbutton
def mostrar_mensaje():
    if check_var.get() == 1:  # Si el Checkbutton está marcado
        mensaje.config(text="El Checkbutton está marcado")
    else:
        mensaje.config(text="El Checkbutton no está marcado")

# Configuración de la ventana
ventana = Tk()
ventana.title("Ejemplo de Checkbutton")
ventana.geometry("300x150")

# Variable de control para el Checkbutton
check_var = IntVar()

# Crear un Checkbutton
checkbutton = Checkbutton(ventana, text="Marcar este Checkbutton", variable=check_var, command=mostrar_mensaje)
checkbutton.pack(pady=20)

# Etiqueta para mostrar el estado del Checkbutton
mensaje = Label(ventana, text="")
mensaje.pack()

ventana.mainloop()