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
imagenes_slider = [ 
        {"ruta":r"'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\petmate2.png'"},
        {"ruta":r"'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\dogs.png'"}
    ]
ejecucion_vista_inicio = False

clientes = [
    {"nombre":"Santiago", "apellido":"Bonilla", "id":"1", "email":"sbr@hotmail.com", "mascota":"Rufus", "codigo":"ABC123"},
    {"nombre":"Rachell", "apellido":"McAdams","id":"2", "email":"rmcadams@hotmail.com", "mascota":"Fifi", "codigo":"DEF456"}
]
ejecucion_carga_clientes = False

inventario = [
    {"id":"1", "nombre": "alimento perros", "categoria": "alimentos", "precio": "7.000", "cantidad": "4", "proveedor": "DogChow"},
    {"id":"3", "nombre": "hueso de juguete", "categoria": "juguetes", "precio": "2.500", "cantidad": "12", "proveedor": "DogChow"},
    {"id":"45", "nombre": "collar", "categoria": "accesorios", "precio": "8.000", "cantidad": "7", "proveedor": "DogChow"},
]
ejecucion_carga_inventario = False

servicios = [
    {"id": "1", "tipo": "Peluquería", "precio": "₡10.000", "duracion": "45 min"},
    {"id": "2", "tipo": "Consulta General", "precio": "₡15.000", "duracion": "30 min"},
    {"id": "3", "tipo": "Venta de Accesorios", "precio": "₡Variable", "duracion": "N/A"},
    {"id": "4", "tipo": "Venta de Medicinas", "precio": "₡Variable", "duracion": "N/A"},
]
ejecucion_carga_servicios = False
#=================================Fin Variables y Datos Auxiliares =======================#

#################################Inicio METODOS Y FUNCIONES######################################################

#Define las pestana en la que nos ubicamos, eje central del codigo
def pestana_por_defecto(name):
    boton_inicio.configure(fg_color="gray" if name == "inicio" else "#3ba55d")
    boton_pestana1.configure(fg_color="gray" if name == "pestana1" else "#3ba55d")
    boton_pestana2.configure(fg_color="gray" if name == "pestana2" else "#3ba55d")
    boton_pestana3.configure(fg_color="gray" if name == "pestana3" else "#3ba55d")

    if name == "inicio":
        global ejecucion_vista_inicio
        pestana_inicio.grid(row=0, column=1, sticky="nsew")
        colocar_logo(pestana_inicio, imagen_tk)
        colocar_logo(pestana1, imagen_tk)
        colocar_logo(pestana2, imagen_tk)
        colocar_logo(pestana3, imagen_tk)
        if ejecucion_vista_inicio == False:
            vista_inicio(pestana_inicio)
            ejecucion_vista_inicio = True

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
        global ejecucion_carga_inventario
        pestana2.grid(row=0, column=1, sticky="nsew")
        if ejecucion_carga_inventario == False:
            index_inventario(pestana2)
            ejecucion_carga_inventario = True
    else:
        pestana2.grid_forget()

    if name == "pestana3":
        global ejecucion_carga_servicios
        pestana3.grid(row=0, column=1, sticky="nsew")
        if ejecucion_carga_servicios == False:
            index_servicios(pestana3)
            ejecucion_carga_servicios = True
    else:
        pestana3.grid_forget()

#Redirecciones
def redirigir_a_inicio():
    pestana_por_defecto("inicio")
#Redirecciones
def reidirigir_a_pestana1():
    pestana_por_defecto("pestana1")
#Redirecciones
def redirigir_a_pestana2():
    pestana_por_defecto("pestana2")
#Redirecciones
def redirigir_a_pestana3():
    pestana_por_defecto("pestana3")

#Estilos para las vistas de cada pestaña
def estilos():
    config_estilo = ttk.Style() 

    config_estilo.theme_use("default")

    config_estilo.configure("Treeview",
        background = "#2b2b2b",
        foreground = "white",
        fieldbackground = "#2b2b2b")
    
    config_estilo.configure("Treeview.Heading",
        background = "#1F1F1F",
        foreground = "white")
    
# Funcion para Recibir el cambio de tamaño de la ventana.
def colocar_logo(pestana, imagen):
                    
    label_imagen = tk.Label(pestana, image=imagen, bg="#2b2b2b")
    label_imagen.image = imagen
    label_imagen.place(relx=1.0, y=5, anchor="ne")

#funcion de la vista Inicio
def vista_inicio(root):
    
    # Tab
    tab = customtkinter.CTkTabview(master=root, width=460, height=220)
    tab.grid(row=1, column=0, pady=(10, 20), padx=20)
    tab.add("←")
    tab.add("→")

        # Centramos la imagen dentro del tab (←)
    tab.tab("←").grid_rowconfigure(0, weight=1)
    tab.tab("←").grid_columnconfigure(0, weight=1)

    # Centramos la imagen dentro del tab (→)
    tab.tab("→").grid_rowconfigure(0, weight=1)
    tab.tab("→").grid_columnconfigure(0, weight=1)


    # Logo
    imagen_original = Image.open(r'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\petmate2.PNG')
    imagen_redimensionada = imagen_original.resize((456, 200), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    label_img1 = tk.Label(tab.tab("←"), image=imagen_tk, bg="#2b2b2b")
    label_img1.image = imagen_tk
    label_img1.grid(row=0, column=0, pady=10)

    # Animales
    imagen_original2 = Image.open(r'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\dogs.png')
    imagen_redimensionada2 = imagen_original2.resize((456, 200), Image.Resampling.LANCZOS)
    imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada2)
    label_img2 = tk.Label(tab.tab("→"), image=imagen_tk2, bg="#2b2b2b")
    label_img2.image = imagen_tk2
    label_img2.grid(row=0, column=0, pady=10)

    # === Espaciado entre carrusel y login ===
    separador = customtkinter.CTkLabel(root, text="")  # Espacio vacío
    separador.grid(row=2, column=0, pady=5)

    # === Login Form ===
    entry_usuario = customtkinter.CTkEntry(root, placeholder_text="Usuario", width=240)
    entry_usuario.grid(row=3, column=0, pady=(10, 5))

    entry_contrasena = customtkinter.CTkEntry(root, placeholder_text="Contraseña", show="*", width=240)
    entry_contrasena.grid(row=4, column=0, pady=(5, 15))

    # Contenedor de botones
    contenedor_botones = customtkinter.CTkFrame(root, fg_color="transparent")
    contenedor_botones.grid(row=5, column=0, pady=10)

    btn_ingresar = customtkinter.CTkButton(contenedor_botones, text="Ingresar", width=100)
    btn_ingresar.grid(row=0, column=0, padx=10)

    btn_registrarse = customtkinter.CTkButton(contenedor_botones, text="Registrarse", width=100)
    btn_registrarse.grid(row=0, column=1, padx=10)
#funcion de la vista Clientes
def index_clientes(root):

    estilos()

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

#funcion de la vista Inventario
def index_inventario(root):
    estilos()

    tree = ttk.Treeview(root, columns=("ID", "nombre", "categoria", "precio", "cantidad", "proveedor"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("nombre", text="nombre")
    tree.heading("categoria", text="categoria")
    tree.heading("precio", text="precio")
    tree.heading("cantidad", text="cantidad")
    tree.heading("proveedor", text="proveedor")
    
    tree.column("ID", width=50, anchor="center")
    tree.column("nombre", width=150)
    tree.column("categoria", width=100)
    tree.column("precio", width=50, anchor="center")
    tree.column("cantidad", width=50, anchor="center")
    tree.column("proveedor", width=150)
    
    for producto in inventario:
        tree.insert("", "end", values=(
            producto["id"],
            producto["nombre"],
            producto["categoria"],
            producto["precio"],
            producto["cantidad"],
            producto["proveedor"]
        ))
        
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    
    tree.pack(fill="both", expand=True, padx=10, pady=10)
    
#funcion de la vista Servicios
def index_servicios(root):

    estilos()
    tree = ttk.Treeview(root, columns=("ID", "Servicio", "Precio", "Duración"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Servicio", text="Servicio")
    tree.heading("Precio", text="Precio")
    tree.heading("Duración", text="Duración")

    tree.column("ID", width=50, anchor="center")
    tree.column("Servicio", width=200)
    tree.column("Precio", width=100, anchor="center")
    tree.column("Duración", width=100, anchor="center")

    for servicio in servicios:
        tree.insert("", "end", values=(servicio["id"], servicio["tipo"], servicio["precio"], servicio["duracion"]))

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(fill="both", expand=True, padx=10, pady=10) 

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
