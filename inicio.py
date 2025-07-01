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
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
#################################INICIO METODOS Y FUNCIONES######################################################

#

def pestana_por_defecto(name):
    boton_inicio.configure(fg_color="gray" if name == "inicio" else "transparent")
    boton_pestana1.configure(fg_color="gray" if name == "pestana1" else "transparent")
    boton_pestana2.configure(fg_color="gray" if name == "pestana2" else "transparent")
    boton_pestana3.configure(fg_color="gray" if name == "pestana3" else "transparent")
 

    if name == "inicio":
        pestana_inicio.grid(row=0, column=1, sticky="nsew")
    else:
        pestana_inicio.grid_forget()

    if name == "pestana1":
        pestana1.grid(row=0, column=1, sticky="nsew")
    else:
        pestana1.grid_forget()

    if name == "pestana2":
        pestana2.grid(row=0, column=1, sticky="nsew")
    else:
        pestana2.grid_forget()
    if name == "pestana3":
        pestana3.grid(row=0, column=1, sticky="nsew")
    else:
        pestana3.grid_forget()

def redirigir_a_inicio():
    pestana_por_defecto("inicio")

def reidirigir_a_pestana1():
    pestana_por_defecto("pestana1")

def redirigir_a_pestana2():
    pestana_por_defecto("pestana2")

def redirigir_a_pestana3():
    pestana_por_defecto("pestana3")




# Funcion para Recibir el cambio de tamaño de la ventana.
def resize_imagen(event):

    width = event.width
    height = event.height

    imagen_redimensionada= imagen_original.resize((width, height), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    canvas.create_image(0, 0, anchor='nw', image=imagen_tk)
    canvas.image = imagen_tk  # evitar que se libere de memoria

    
#################################FIN METODOS Y FUNCIONES########################################################

############################# Inicio Estructura y vista de la Ventana##############################################

#===================================VENTANA DEL PROGRAMA================================#
# Crear la ventana principal 
programa = customtkinter.CTk()
programa.title("PetMate")
programa.geometry("700x450")
programa.grid_rowconfigure(0, weight=1)
programa.grid_columnconfigure(1, weight=1)
#icono de la Ventana
programa.iconbitmap(r'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\icopet.ico')
#======================================================================================#


#========================= INICIO  MARCO LATERAL ===============================#
#Crear el Marco del widget de navegacion(contenedor de lateral de pestañas) ====
marco_navegacion = customtkinter.CTkFrame(programa, corner_radius=0)
marco_navegacion.grid(row=0, column=0, sticky="nsew")
marco_navegacion.grid_rowconfigure(5, weight=1)

#Etiqueta con Encabezado para el Marco lateral.
marco_navegacion_label = customtkinter.CTkLabel(marco_navegacion,text="  Menú Navegación", font=customtkinter.CTkFont(size=15, weight="bold"))
marco_navegacion_label.grid(row=0, column=0, padx=20, pady=20)

# Botones del Marco lateral.
boton_inicio = customtkinter.CTkButton(marco_navegacion, text="Inicio", command=redirigir_a_inicio)
boton_inicio.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

boton_pestana1 = customtkinter.CTkButton(marco_navegacion, text="Clientes", command=reidirigir_a_pestana1)
boton_pestana1.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

boton_pestana2 = customtkinter.CTkButton(marco_navegacion, text="Inventario", command=redirigir_a_pestana2)
boton_pestana2.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

boton_pestana3 = customtkinter.CTkButton(marco_navegacion, text="Servicios", command=redirigir_a_pestana3)
boton_pestana3.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
#========================= FIN MARCO LATERAL ===============================#

#========================INICIO VENTANAS SECUNDARIAS========================#
    # === Frames del contenido principal ===
pestana_inicio = customtkinter.CTkFrame(programa, corner_radius=0)
pestana_inicio.grid_columnconfigure(0, weight=1)
label_inicio = customtkinter.CTkLabel(pestana_inicio, text="Bienvenido a PetMate", font=("TkHeadingFont", 24,"bold"))
label_inicio.grid(row=0, column=0, pady=50)

pestana1 = customtkinter.CTkFrame(programa, corner_radius=0)
label_1 = customtkinter.CTkLabel(pestana1, text="Clientes", font=("Arial", 18))
label_1.pack(pady=50)

pestana2 = customtkinter.CTkFrame(programa, corner_radius=0)
label_2 = customtkinter.CTkLabel(pestana2, text="Inventario", font=("Arial", 18))
label_2.pack(pady=50)

pestana3 = customtkinter.CTkFrame(programa, corner_radius=0)
label_3 = customtkinter.CTkLabel(pestana3, text="Servicios", font=("Arial", 18))
label_3.pack(pady=50)

redirigir_a_inicio()


imagen_original = Image.open(r'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\petmatepng1.png')
imagen_redimensionada = imagen_original.resize((200, 200), Image.Resampling.LANCZOS) ## Se redimensiona la imagen usando la libreria PIL, y su funcion resize.
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)                                ## Se asigna la imagen redimensionada
label_imagen = tk.Label(pestana_inicio, image=imagen_tk, bg="#2b2b2b")
label_imagen.image = imagen_tk
label_imagen.grid(row=0, column=0, sticky="ne", pady=50)
# Crear los marcos (pestañas)
# pestana1 = customtkinter.CTkFrame(programa)
# pestana2 = customtkinter.CTkFrame(notebook)
# pestana3 = customtkinter.CTkFrame(notebook)
# pestana4 = customtkinter.CTkFrame(notebook)

# Agregar las pestañas al notebook  
# notebook.add(pestana1, text='Inicio')
# notebook.add(pestana2, text='Clientes')
# notebook.add(pestana3, text='Inventario')
# notebook.add(pestana4, text='Servicios')


# --- PESTAÑA 1: Imagen + botón sobre Canvas ---
#canvas = tk.Canvas(pestana1, width=600, height=600, highlightthickness=0)
#canvas.pack(fill="both", expand=True)

# Poner imagen como fondo
#canvas.create_image(0, 0, anchor='nw', image=imagen_tk)
#canvas.image = imagen_tk  # evitar que se libere de memoria

# Botón que cambia a la pestaña 2
# etiqueta_bienvenida = tk.Label(
#     programa,
#     text="!Bienvenido a Petmate!",
#     fg="white",
#     bg = "#242424",
#     font=("TkHeadingFont", 24, "bold"))
# etiqueta_bienvenida.place(x=350, y=50)    

# Contenido de la pestaña 2
# label = ttk.Label(pestana2, text="¡Estás en la pestaña 2!")

#canvas.bind("<Configure>",resize_imagen)

# Ejecutar la aplicación
programa.mainloop()

################################### Inicializar Programa#########################
