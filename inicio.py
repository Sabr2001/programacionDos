################################################################
#Nombre del Programa: 
#Numero de Grupo de trabajo: 03
#Nombre de los Programadores: Santiago Bonilla
#Version del PYTHON: 3.13
#nombre del IDE donde se trabajo el codigo: VSC
###############################################################

##Librerias##
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, PhotoImage

#################################<INICIO METODOS Y FUNCIONES >######################################################

def resize_imagen(event):

    widtd = event.width
    height = event.height

    imagen_redimensionada= imagen_original.resize((widtd, height), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    canvas.create_image(0, 0, anchor='nw', image=imagen_tk)
    canvas.image = imagen_tk  # evitar que se libere de memoria



# Función para cambiar a la pestaña 2
def ir_a_pestana2():
    notebook.select(pestana2)
    
#################################<FIN METODOS Y FUNCIONES >########################################################

############################# Inicio Estructura y vista de la Ventana##############################################
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de pestañas con botón")
ventana.geometry("600x600")

imagen_original = Image.open(r'C:\Users\Santiago\Downloads\petmate.png')
imagen_redimensionada = imagen_original.resize((600, 600), Image.Resampling.LANCZOS) ## Se redimensiona la imagen usando la libreria PIL, y su funcion resize.
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)                                ## Se asigna la imagen redimensionada

# Crear el widget Notebook (contenedor de pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill='both')
    
# Crear los marcos (pestañas)
pestana1 = ttk.Frame(notebook)
pestana2 = ttk.Frame(notebook)
pestana3 = ttk.Frame(notebook)
pestana4 = ttk.Frame(notebook)

# Agregar las pestañas al notebook
notebook.add(pestana1, text='Inicio')
notebook.add(pestana2, text='Clientes')
notebook.add(pestana3, text='Inventario')
notebook.add(pestana4, text='Servicios')


# --- PESTAÑA 1: Imagen + botón sobre Canvas ---
canvas = tk.Canvas(pestana1, width=600, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Poner imagen como fondo
canvas.create_image(0, 0, anchor='nw', image=imagen_tk)
canvas.image = imagen_tk  # evitar que se libere de memoria

# Botón que cambia a la pestaña 2
etiqueta_bienvenida = tk.Label(
    pestana1,
    text="!Bienvenido a Petmate!",
    bg="#16BC69",
    fg="#FFFFFF",
    font=("TkHeadingFont", 24, "bold"))
etiqueta_bienvenida.place(x=125, y=50)    

boton = ttk.Button(pestana1, text="Ir a Clientes", command=ir_a_pestana2)
boton.place(x=250, y=100)

# Contenido de la pestaña 2
label = ttk.Label(pestana2, text="¡Estás en la pestaña 2!")

canvas.bind("<Configure>",resize_imagen)

# Ejecutar la aplicación
ventana.mainloop()