from tkinter import *
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")

# Define colores personalizados
color_fondo = "#333333"  # Color de fondo oscuro
color_texto = "white"  # Color de texto blanco
color_botones = "#666666"  # Color de fondo de los botones
color_boton_operacion = "#ff9933"  # Color de fondo de los botones de operación
color_boton_igual = "#ffcc00"  # Color de fondo del botón igual

i = 0
e_texto = Entry(ventana, font=("Arial", 20))
e_texto.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=10, ipady=10)

ventana.configure(bg=color_fondo)

# Resto del código...
frame = Frame(ventana, borderwidth=2, relief="solid")  # Puedes personalizar el borde y el relieve
etiqueta = Label(frame, text="Esto está dentro del frame")
etiqueta.pack()
boton = Button(frame, text="Haz clic aquí")
boton.pack()


# Funciones para los botones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    global i
    e_texto.delete(0, END)
    i = 0

def operacion():
    ecuacion = e_texto.get()
    try:
        resultado = eval(ecuacion)
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
    except Exception as e:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

def decimal_a_binario():
    ecuacion = e_texto.get()
    try:
        resultado_decimal = eval(ecuacion)
        resultado_binario = format(int(resultado_decimal), 'b')  # Convierte a binario y elimina el prefijo
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_binario)
    except Exception as e:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

def decimal_a_hexadecimal():
    ecuacion = e_texto.get()
    try:
        resultado_decimal = eval(ecuacion)
        resultado_hexadecimal = format(int(resultado_decimal), 'X')  # Convierte a hexadecimal en mayúsculas
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_hexadecimal)
    except Exception as e:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

def binario_a_hexadecimal():
    ecuacion = e_texto.get()
    try:
        resultado_decimal = int(ecuacion, 2)  # Convierte binario a decimal
        resultado_hexadecimal = format(resultado_decimal, 'X')  # Convierte a hexadecimal en mayúsculas
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_hexadecimal)
    except Exception as e:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

def Back():
    global i
    i = i-1
    e_texto.delete(i, END)

# Definir la función de cambio de estado del botón ON/OFF
def switchButtonState():
    if boton_ON["text"] == "ON":
        boton_ON["text"] = "OFF"
    else:
        boton_ON["text"] = "ON"

    botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0, boton_binario,
               boton_CLR, boton_div, boton_mult, boton_suma, boton_resta, boton_borrar, boton_igual, boton_Punto,
               boton_Parentesis1, boton_Parentesis2, boton_decimal_a_hex, boton_binario_a_hex]

    for boton in botones:
        boton["state"] = NORMAL if boton["state"] == DISABLED else DISABLED

checkbox_var = IntVar()

# Definir la función para alternar el estado de los botones
def toggleButtonState():
    if checkbox_var.get() == 1:  # Si el checkbox está marcado
        for widget in ventana.winfo_children():
            if isinstance(widget, Button):
                widget.configure(state=NORMAL)
    else:
        for widget in ventana.winfo_children():
            if isinstance(widget, Button):
                widget.configure(state=DISABLED)

# Crear el checkbox ON/OFF
checkbox = Checkbutton(ventana, text="ON/OFF", variable=checkbox_var, onvalue=1, offvalue=0, command=toggleButtonState)
checkbox.grid(row=5, column=4, padx=5, pady=5, sticky="e")
# Crear botones con colores personalizados
boton1 = Button(ventana, text="1", width=5, height=2, state=DISABLED, command=lambda: click_boton(1), bg=color_botones, fg=color_texto)
boton2 = Button(ventana, text="2", width=5, height=2, state=DISABLED, command=lambda: click_boton(2), bg=color_botones, fg=color_texto)
boton3 = Button(ventana, text="3", width=5, height=2, state=DISABLED, command=lambda: click_boton(3), bg=color_botones, fg=color_texto)
boton4 = Button(ventana, text="4", width=5, height=2, state=DISABLED, command=lambda: click_boton(4), bg=color_botones, fg=color_texto)
boton5 = Button(ventana, text="5", width=5, height=2, state=DISABLED, command=lambda: click_boton(5), bg=color_botones, fg=color_texto)
boton6 = Button(ventana, text="6", width=5, height=2, state=DISABLED, command=lambda: click_boton(6), bg=color_botones, fg=color_texto)
boton7 = Button(ventana, text="7", width=5, height=2, state=DISABLED, command=lambda: click_boton(7), bg=color_botones, fg=color_texto)
boton8 = Button(ventana, text="8", width=5, height=2, state=DISABLED, command=lambda: click_boton(8), bg=color_botones, fg=color_texto)
boton9 = Button(ventana, text="9", width=5, height=2, state=DISABLED, command=lambda: click_boton(9), bg=color_botones, fg=color_texto)
boton0 = Button(ventana, text="0", width=5, height=2, state=DISABLED, command=lambda: click_boton(0), bg=color_botones, fg=color_texto)

boton_borrar = Button(ventana, text="AC", width=5, height=2, state=DISABLED, font=("Arial", 10), command=borrar, bg="red", fg=color_texto)
boton_CLR = Button(ventana, text="C", width=5, height=2, state=DISABLED, command = lambda: Back(), bg=color_boton_operacion, fg=color_texto)
boton_Parentesis1 = Button(ventana, text="(", width=5, height=2, state=DISABLED, command=lambda: click_boton("("), bg=color_botones, fg=color_texto)
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2, state=DISABLED, command=lambda: click_boton(")"), bg=color_botones, fg=color_texto)
boton_Punto = Button(ventana, text=".", width=5, height=2, state=DISABLED, command=lambda: click_boton("."), bg=color_botones, fg=color_texto)

boton_div = Button(ventana, text="/", width=5, height=2, state=DISABLED, command=lambda: click_boton("/"), bg=color_boton_operacion, fg=color_texto)
boton_mult = Button(ventana, text="x", width=5, height=2, state=DISABLED, command=lambda: click_boton("*"), bg=color_boton_operacion, fg=color_texto)
boton_suma = Button(ventana, text="+", width=5, height=2, state=DISABLED, command=lambda: click_boton("+"), bg=color_boton_operacion, fg=color_texto)
boton_resta = Button(ventana, text="-", width=5, height=2, state=DISABLED, command=lambda: click_boton("-"), bg=color_boton_operacion, fg=color_texto)
boton_igual = Button(ventana, text="=", width=5, height=2, state=DISABLED, command=lambda: operacion(), bg=color_boton_igual, fg="black")
boton_binario = Button(ventana, text="Binario", width=5, height=2, state=DISABLED, command=decimal_a_binario, bg=color_boton_operacion, fg=color_texto)
boton_decimal_a_hex = Button(ventana, text="D a H", width=5, height=2, state=DISABLED, command=decimal_a_hexadecimal, bg=color_boton_operacion, fg=color_texto)
boton_binario_a_hex = Button(ventana, text="B a H", width=5, height=2, state=DISABLED, command=binario_a_hexadecimal, bg=color_boton_operacion, fg=color_texto)
boton_ON = Button(ventana, text="ON", width=5, height=2, state=DISABLED, command=lambda: switchButtonState(), bg=color_botones, fg=color_texto)

# Definir la disposición de los botones en la cuadrícula
botones = [
    (boton_borrar, boton_CLR, boton_Parentesis1, boton_Parentesis2),
    (boton7, boton8, boton9, boton_div),
    (boton4, boton5, boton6, boton_mult),
    (boton1, boton2, boton3, boton_suma),
    (boton0, boton_Punto, boton_igual, boton_resta)
]

for i, fila in enumerate(botones):
    for j, boton in enumerate(fila):
        boton.grid(row=i + 1, column=j, padx=5, pady=5)

# Agregar botones adicionales
boton_binario.grid(row=2, column=4, padx=5, pady=5)
boton_decimal_a_hex.grid(row=3, column=4, padx=5, pady=5)
boton_binario_a_hex.grid(row=4, column=4, padx=5, pady=5)
boton_ON.grid(row=1, column=4, padx=5, pady=5)

# Establecer el tamaño mínimo de la ventana
ventana.minsize(350, 350)

# Configuración de la disposición de las filas y columnas
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

ventana.mainloop()