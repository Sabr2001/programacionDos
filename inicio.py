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

# Funcion para Recibir el cambio de tamaño de la ventana.
def resize_imagen(event):

    width = event.width
    height = event.height

    imagen_redimensionada= imagen_original.resize((width, height), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    canvas.create_image(0, 0, anchor='nw', image=imagen_tk)
    canvas.image = imagen_tk  # evitar que se libere de memoria

# Función para cambiar a la pestaña 2.
def ir_a_pestana2():
    notebook.select(pestana2)
    
#################################FIN METODOS Y FUNCIONES########################################################

############################# Inicio Estructura y vista de la Ventana##############################################

def main():

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
    boton_inicio = customtkinter.CTkButton(marco_navegacion, text="Inicio")
    boton_inicio.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

    boton_pestana1 = customtkinter.CTkButton(marco_navegacion, text="Clientes")
    boton_pestana1.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    boton_pestana2 = customtkinter.CTkButton(marco_navegacion, text="Inventario")
    boton_pestana2.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

    boton_pestana3 = customtkinter.CTkButton(marco_navegacion, text="Servicios")
    boton_pestana3.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
    #========================= FIN MARCO LATERAL ===============================#
    
    #========================INICIO VENTANAS SECUNDARIAS========================#
        # === Frames del contenido principal ===
    pestana_inicio = customtkinter.CTkFrame(programa, corner_radius=0)
    pestana_inicio.grid_columnconfigure(0, weight=1)
    label_inicio = customtkinter.CTkLabel(pestana_inicio, text="Bienvenido a la página de Inicio", font=("TkHeadingFont", 24,"bold"))
    label_inicio.grid(row=0, column=0, pady=50)

    # self.second_frame = customtkinter.CTkFrame(self, corner_radius=0)
    # self.label_2 = customtkinter.CTkLabel(self.second_frame, text="Clientes", font=("Arial", 18))
    # self.label_2.pack(pady=50)

    # self.third_frame = customtkinter.CTkFrame(self, corner_radius=0)
    # self.label_3 = customtkinter.CTkLabel(self.third_frame, text="Servicios", font=("Arial", 18))
    # self.label_3.pack(pady=50)




    #imagen_original = Image.open(r'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\petmate1.png')
    #imagen_redimensionada = imagen_original.resize((600, 600), Image.Resampling.LANCZOS) ## Se redimensiona la imagen usando la libreria PIL, y su funcion resize.
    #imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)                                ## Se asigna la imagen redimensionada
        
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
main()