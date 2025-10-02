import tkinter as tk
import random
import string

def generar_contrasena():
    # Establece la longitud y los caracteres de la contraseña
    longitud = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Genera la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

    # Muestra la contraseña en la etiqueta
    etiqueta_contrasena.config(text=contrasena)

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Generador de contraseñas")

# Crea una etiqueta para mostrar la contraseña
etiqueta_contrasena = tk.Label(ventana, text="", font=("Arial", 24))
etiqueta_contrasena.pack(pady=20)

# Crea un botón para generar una nueva contraseña
boton_generar = tk.Button(ventana, text="Generar contraseña", command=generar_contrasena)
boton_generar.pack(pady=20)

# Inicia el bucle principal de la aplicación
ventana.mainloop()