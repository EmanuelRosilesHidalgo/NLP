import tkinter as tk
from tkinter import scrolledtext

# Crear una ventana
ventana = tk.Tk()
ventana.title("Texto Centrado en ScrolledText")

# Crear un widget ScrolledText
scrolled_text = scrolledtext.ScrolledText(ventana, width=40, height=10)
scrolled_text.pack()

# Texto que deseas centrar
texto = "Este es un ejemplo de texto centrado en un ScrolledText."

# Longitud del texto en caracteres
longitud_texto = len(texto)

# Agregar el texto al widget ScrolledText
scrolled_text.insert("1.0", texto)

# Configurar una etiqueta de estilo para centrar el texto
scrolled_text.tag_configure("center", justify="center")

# Aplicar la etiqueta de estilo al texto
scrolled_text.tag_add("center", "1.0", f"1.{longitud_texto}")

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()
