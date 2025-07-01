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


#================================= Variables y Datos Auxiliares =======================#
clientes = [
    {"nombre":"Santiago", "apellido":"Bonilla", "id":"1", "email":"sbr@hotmail.com", "mascota":"Rufus", "codigo":"ABC123"},
    {"nombre":"Rachell", "apellido":"McAdams","id":"2", "email":"rmcadams@hotmail.com", "mascota":"Fifi", "codigo":"DEF456"}
]
ejecucion_carga_clientes = False
#################################INICIO METODOS Y FUNCIONES######################################################

#
def pestana_por_defecto(name):
    boton_inicio.configure(fg_color="gray" if name == "inicio" else "transparent")
    boton_pestana1.configure(fg_color="gray" if name == "pestana1" else "transparent")
    boton_pestana2.configure(fg_color="gray" if name == "pestana2" else "transparent")
    boton_pestana3.configure(fg_color="gray" if name == "pestana3" else "transparent")
 

    if name == "inicio":
        pestana_inicio.grid(row=0, column=1, sticky="nsew")
        colocar_logo(pestana_inicio, imagen_tk)
        colocar_logo(pestana1, imagen_tk)
        colocar_logo(pestana2, imagen_tk)
        colocar_logo(pestana3, imagen_tk)

    else:
        pestana_inicio.grid_forget()

    if name == "pestana1":
        global ejecucion_carga_clientes
        pestana1.grid(row=0, column=1, sticky="nsew")
        if ejecucion_carga_clientes == False:
            index_clientes(pestana1)
            ejecucion_carga_clientes = True
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

def index_clientes(root):
    tree = ttk.Treeview(root, columns=("ID", "Nombre","Apellido", "Correo", "Mascota","Codigo"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Correo", text="Correo")
    tree.heading("Mascota", text="Mascota")
    tree.heading("Codigo", text="Código de Mascota")

    for cliente in clientes:
        tree.insert("", "end", values=(cliente["id"],cliente["nombre"],cliente["apellido"],cliente["email"], cliente["mascota"],cliente["codigo"]))

    tree.pack(fill="both", expand=True)


# Funcion para Recibir el cambio de tamaño de la ventana.
def colocar_logo(pestana, imagen):
                         
    label_imagen = tk.Label(pestana, image=imagen, bg="#2b2b2b")
    label_imagen.image = imagen
    label_imagen.place(relx=1.0, y=5, anchor="ne")

    
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


imagen_original = Image.open(r'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\petmatepng1.png')
imagen_redimensionada = imagen_original.resize((150, 150), Image.Resampling.LANCZOS) ## Se redimensiona la imagen usando la libreria PIL, y su funcion resize.
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)                                ## Se asigna la imagen redimensionada

redirigir_a_inicio()

# Ejecutar la aplicación
programa.mainloop()

################################### Inicializar Programa#########################
