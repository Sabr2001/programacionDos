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

inventario = [
    {"id":"1", "nombre": "alimento perros", "categoria": "alimentos", "precio": "7.000", "cantidad": "4", "proveedor": "DogChow"},
    {"id":"3", "nombre": "hueso de juguete", "categoria": "juguetes", "precio": "2.500", "cantidad": "12", "proveedor": "DogChow"},
    {"id":"45", "nombre": "collar", "categoria": "accesorios", "precio": "8.000", "cantidad": "7", "proveedor": "DogChow"},
]
ejecucio_carga_inventario = False
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
        global ejecucio_carga_inventario
        pestana2.grid(row=0, column=1, sticky="nsew")
        if ejecucio_carga_inventario == False:
            index_inventario(pestana2)
            ejecucio_carga_inventario = True
        

        
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

#funcion del inventario
def index_inventario(root):
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
from tkinter import messagebox
import customtkinter
import sqlite3
from datetime import datetime #########para las bases de datos 
import os #####es para conectarse al sistema operativo y poder usar la carpeta

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

DB_FILE = "petmate.db" #esta es la base de datos



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

ejecucion_carga_punto_venta = False
ejecucion_carga_caja = False
ejecucion_carga_productos = False
#######################################base de datos
def crear_tablas_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id TEXT PRIMARY KEY,
                        nombre TEXT,
                        categoria TEXT,
                        precio REAL,
                        cantidad INTEGER,
                        proveedor TEXT,
                        codigo_barras TEXT,
                        descripcion TEXT,
                        unidad_medida TEXT,
                        iva REAL,
                        descuento REAL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha TEXT,
                        cliente_id TEXT,
                        total REAL,
                        pagado REAL,
                        saldo REAL,
                        estado TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS venta_items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        venta_id INTEGER,
                        producto_id TEXT,
                        cantidad INTEGER,
                        precio_unitario REAL,
                        FOREIGN KEY (venta_id) REFERENCES ventas(id),
                        FOREIGN KEY (producto_id) REFERENCES productos(id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS caja (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha TEXT,
                        tipo TEXT,
                        monto REAL,
                        descripcion TEXT,
                        usuario TEXT
                    )''')
    # cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
    #                     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                     nombre TEXT,
    #                     tipo TEXT,
    #                     monto REAL,
    #                     descripcion TEXT,
    #                     usuario TEXT
    #                 )''')
    conn.commit()
    conn.close()

def cargar_productos_prueba():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos")
    if cursor.fetchone()[0] == 0:
        productos_demo = [
            ("1", "Alimento perros", "alimentos", 7000.0, 10, "DogChow", "123456", "Comida seca para perros", "kg", 13.0, 0.0),
            ("2", "Hueso juguete", "juguetes", 2500.0, 20, "DogChow", "789101", "Hueso de goma", "unidad", 13.0, 0.0),
            ("3", "Collar", "accesorios", 8000.0, 15, "DogChow", "112131", "Collar ajustable", "unidad", 13.0, 0.0)
        ]
        cursor.executemany('''INSERT INTO productos 
        (id, nombre, categoria, precio, cantidad, proveedor, codigo_barras, descripcion, unidad_medida, iva, descuento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', productos_demo)
        conn.commit()
    conn.close()
#=================================Fin Variables y Datos Auxiliares =======================#

#################################Inicio METODOS Y FUNCIONES######################################################

#Define las pestana en la que nos ubicamos, eje central del codigo
def pestana_por_defecto(name):
    boton_inicio.configure(fg_color="gray" if name == "inicio" else "#3ba55d")
    boton_pestana1.configure(fg_color="gray" if name == "pestana1" else "#3ba55d")
    boton_pestana2.configure(fg_color="gray" if name == "pestana2" else "#3ba55d")
    boton_pestana3.configure(fg_color="gray" if name == "pestana3" else "#3ba55d")
    boton_pestana4.configure(fg_color="gray" if name == "pestana4" else "transparent")
    boton_pestana5.configure(fg_color="gray" if name == "pestana5" else "#3ba55d")
    boton_pestana6.configure(fg_color="gray" if name == "pestana6" else "#3ba55d")

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

    if name == "pestana4":
        global ejecucion_carga_punto_venta
        pestana4.grid(row=0, column=1, sticky="nsew")
        if ejecucion_carga_punto_venta == False:
            index_punto_venta(pestana4)
            ejecucion_carga_punto_venta = True
    else:
        pestana4.grid_forget()

    if name == "pestana5":
        global ejecucion_carga_caja
        pestana5.grid(row=0, column=1, sticky="nsew")
        if ejecucion_carga_caja == False:
            index_caja(pestana5)
            ejecucion_carga_caja = True
    else:
        pestana5.grid_forget()
    
    if name == "pestana6":
        global ejecucion_carga_productos
        pestana6.grid(row=0, column=1, sticky="nsew")
        if ejecucion_carga_productos == False:
            index_productos(pestana6)
            ejecucion_carga_productos = True
    else:
        pestana6.grid_forget()
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

    frame = customtkinter.CTkFrame(root)
    label = customtkinter.CTkLabel(frame, text="Inventario", font=("Arial", 16))
    label.pack(pady=5)
    tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Categoría", "Precio", "Cantidad", "Proveedor"), show="headings")
    for col in ("ID", "Nombre", "Categoría", "Precio", "Cantidad", "Proveedor"):
        tree.heading(col, text=col)
        tree.column(col, width=100)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
################eesto va a cargar productos desde la base de datos
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, categoria, precio, cantidad, proveedor FROM productos")
    for prod in cur.fetchall():
        tree.insert("", "end", values=prod)
    conn.close()
    tree.pack(fill="both", expand=True, padx=10, pady=10)
    frame.pack(fill="both", expand=True)  

    
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


############################ apartado para buscar productos
def buscar_producto(codigo=None, nombre=None, clave=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    producto = None
    if codigo:
        cursor.execute("SELECT * FROM productos WHERE codigo_barras=?", (codigo,))
        producto = cursor.fetchone()
    elif nombre:
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
        producto = cursor.fetchone()
    elif clave:
        cursor.execute("SELECT * FROM productos WHERE id=?", (clave,))
        producto = cursor.fetchone()
    
    conn.close()
    if producto:
        return {"id": producto[0], "nombre": producto[1], "precio": producto[3], "cantidad": producto[4]}
    return None
##############################################apartado para registrar las ventas
def registrar_venta(productos, cliente_id=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    total = sum(float(p['precio']) * int(p['cantidad']) for p in productos)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO ventas (fecha, cliente_id, total, pagado, saldo, estado) VALUES (?, ?, ?, ?, ?, ?)",
                (fecha, cliente_id, total, total, 0, 'completada'))
    venta_id = cursor.lastrowid
    for producto in productos:
        cursor.execute("INSERT INTO venta_items (venta_id, producto_id, cantidad, precio_unitario) VALUES (?, ?, ?, ?)",
                    (venta_id, producto['id'], producto['cantidad'], producto['precio']))
        cursor.execute("UPDATE productos SET cantidad = cantidad - ? WHERE id = ?",
                    (producto['cantidad'], producto['id']))
    conn.commit()
    conn.close()
    return venta_id
###############################################para registras productos
def registrar_producto(producto):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO productos 
                    (id, nombre, categoria, precio, cantidad, proveedor, codigo_barras, descripcion, unidad_medida, iva, descuento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (producto['id'], producto['nombre'], producto['categoria'], producto['precio'],
                    producto['cantidad'], producto['proveedor'], producto['codigo_barras'],
                    producto['descripcion'], producto['unidad_medida'], producto['iva'], producto['descuento']))
    conn.commit()
    conn.close()
###########################################################para los movimientos de cvaja
def registrar_movimiento_caja(tipo, monto, descripcion, usuario="admin"):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO caja (fecha, tipo, monto, descripcion, usuario) VALUES (?, ?, ?, ?, ?)",
                (fecha, tipo, monto, descripcion, usuario))
    conn.commit()
    conn.close()
################################################para realizar los cortes, para esto se agrega datetime arriba al inicio
def realizar_corte_caja():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("SELECT SUM(monto) FROM caja WHERE tipo='entrada' AND date(fecha)=?", (fecha,))
    total_entradas = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(monto) FROM caja WHERE tipo='salida' AND date(fecha)=?", (fecha,))
    total_salidas = cursor.fetchone()[0] or 0
    saldo = total_entradas - total_salidas
    conn.close()
    return {"fecha": fecha, "entradas": total_entradas, "salidas": total_salidas, "saldo": saldo}


def index_productos(root):
    frame = customtkinter.CTkFrame(root)
    label = customtkinter.CTkLabel(frame, text="Productos", font=("Arial", 16))
    label.pack(pady=5)
    frame_controles = customtkinter.CTkFrame(frame)
    frame_controles.pack(fill="x", padx=10, pady=5)
    btn_nuevo = customtkinter.CTkButton(frame_controles, text="Nuevo Producto", command=lambda: abrir_dialogo_producto(tree))
    btn_nuevo.pack(side="left", padx=5)
###############la lista
    tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Categoría", "Precio", "Cantidad", "Proveedor"), show="headings")
    for col in ("ID", "Nombre", "Categoría", "Precio", "Cantidad", "Proveedor"):
        tree.heading(col, text=col)
        tree.column(col, width=110)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    ###############con esto se cargan
    cargar_productos_en_tree(tree)
    tree.pack(fill="both", expand=True, padx=10, pady=10)
    frame.pack(fill="both", expand=True)  

def cargar_productos_en_tree(tree):
    for child in tree.get_children():
        tree.delete(child)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, categoria, precio, cantidad, proveedor FROM productos")
    for prod in cur.fetchall():
        tree.insert("", "end", values=prod)
    conn.close()
    
#############importante, primero tyenemos que agregar los productos a la base de datos, los que agregue como ejemplo no funcioonan
#####es decir primero hay que ir agregarlo en productos, luego en el PDV buscarlo por su nombre y ya se registra la venta
#hola

def index_punto_venta(root):
    frame = customtkinter.CTkFrame(root)
##############con estos se busca
    frame_busq = customtkinter.CTkFrame(frame)
    frame_busq.pack(fill="x", padx=10, pady=5)
    lbl = customtkinter.CTkLabel(frame_busq, text="Buscar Producto:")
    lbl.pack(side="left", padx=5)
    entry_busq = customtkinter.CTkEntry(frame_busq, width=300)
    entry_busq.pack(side="left", padx=5)
###########productos seleccionados
    frame_prod = customtkinter.CTkFrame(frame)
    frame_prod.pack(fill="both", expand=True, padx=10, pady=5)
    tree_cart = ttk.Treeview(frame_prod, columns=("ID", "Nombre", "Precio", "Cantidad", "Subtotal"), show="headings")
    for col in ("ID", "Nombre", "Precio", "Cantidad", "Subtotal"):
        tree_cart.heading(col, text=col)
        tree_cart.column(col, width=100)
    scrollbar = ttk.Scrollbar(frame_prod, orient="vertical", command=tree_cart.yview)
    scrollbar.pack(side="right", fill="y")
    tree_cart.configure(yscrollcommand=scrollbar.set)
    tree_cart.pack(fill="both", expand=True)
############el totasl y lso botones
    frame_total = customtkinter.CTkFrame(frame)
    frame_total.pack(fill="x", padx=10, pady=5)
    lbl_total = customtkinter.CTkLabel(frame_total, text="Total: $0.00", font=("Arial", 14, "bold"))
    lbl_total.pack(side="left", padx=10)
    btn_registrar = customtkinter.CTkButton(frame_total, text="Registrar Venta", command=lambda: on_registrar_venta(tree_cart, lbl_total))
    btn_registrar.pack(side="right", padx=5)
    btn_limpiar = customtkinter.CTkButton(frame_total, text="Limpiar", command=lambda: on_limpiar_venta(tree_cart, lbl_total))
    btn_limpiar.pack(side="right", padx=5)
    btn_buscar = customtkinter.CTkButton(frame_busq, text="Buscar", command=lambda: on_buscar_producto(entry_busq.get(), tree_cart, lbl_total))
    btn_buscar.pack(side="left", padx=5)
    frame.pack(fill="both", expand=True)  

def index_caja(root):
    frame = customtkinter.CTkFrame(root)
    frame_mov = customtkinter.CTkFrame(frame)
    frame_mov.pack(fill="both", expand=True, padx=10, pady=5)
    tree = ttk.Treeview(frame_mov, columns=("Fecha", "Tipo", "Monto", "Descripción", "Usuario"), show="headings")
    for col in ("Fecha", "Tipo", "Monto", "Descripción", "Usuario"):
        tree.heading(col, text=col)
        tree.column(col, width=130)
    scrollbar = ttk.Scrollbar(frame_mov, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(fill="both", expand=True)
    frame.pack(fill="both", expand=True)  
##################carga mnovimientos
    cargar_movimientos_caja(tree)
    ############acciojes
    frame_acc = customtkinter.CTkFrame(frame)
    frame_acc.pack(fill="x", padx=10, pady=5)
    btn_entrada = customtkinter.CTkButton(frame_acc, text="Registrar Entrada", command=lambda: abrir_dialogo_movimiento("entrada", tree))
    btn_entrada.pack(side="left", padx=5)
    btn_salida = customtkinter.CTkButton(frame_acc, text="Registrar Salida", command=lambda: abrir_dialogo_movimiento("salida", tree))
    btn_salida.pack(side="left", padx=5)
    btn_corte = customtkinter.CTkButton(frame_acc, text="Realizar Corte", command=lambda: realizar_corte_caja_gui(tree))
    btn_corte.pack(side="right", padx=5)
    return frame

#########################Punto de venta
def on_buscar_producto(criterio, tree_cart, lbl_total):
    if not criterio:
        messagebox.showwarning("Aviso", "Ingrese criterio de búsqueda (nombre o código).")
        return
    producto = buscar_producto(nombre=criterio, codigo=criterio)
    if not producto:
        messagebox.showwarning("No encontrado", "Producto no encontrado.")
        return
###############verifica existencia
    for child in tree_cart.get_children():
        datos = tree_cart.item(child)["values"]
        if str(datos[0]) == str(producto["id"]):
        #####aumenta cantidad
            nueva_cant = int(datos[3]) + 1
            subtotal = float(producto["precio"]) * nueva_cant
            tree_cart.item(child, values=(datos[0], datos[1], datos[2], nueva_cant, f"{subtotal:.2f}"))
            actualizar_total_cart(tree_cart, lbl_total)
            return
###########si no existe inserta uno nmuyevo
    tree_cart.insert("", "end", values=(producto["id"], producto["nombre"], f"{producto['precio']:.2f}", 1, f"{producto['precio']:.2f}"))
    actualizar_total_cart(tree_cart, lbl_total)

def actualizar_total_cart(tree_cart, lbl_total):
    total = 0.0
    for child in tree_cart.get_children():
        datos = tree_cart.item(child)["values"]
        try:
            total += float(datos[4])
        except Exception:
            pass
    lbl_total.configure(text=f"Total: ${total:.2f}")

def on_registrar_venta(tree_cart, lbl_total):
    items = []
    for child in tree_cart.get_children():
        datos = tree_cart.item(child)["values"]
        items.append({"id": str(datos[0]), "nombre": datos[1], "precio": float(datos[2]), "cantidad": int(datos[3])})
    if not items:
        messagebox.showwarning("Error", "No hay productos en la venta.")
        return
#########registra en la base de datos
    venta_id = registrar_venta(items)
    messagebox.showinfo("Venta", f"Venta registrada (ID {venta_id}).")
##########limpia el carritpo
    on_limpiar_venta(tree_cart, lbl_total)

def on_limpiar_venta(tree_cart, lbl_total):
    for child in tree_cart.get_children():
        tree_cart.delete(child)
    lbl_total.configure(text="Total: $0.00")

###############caja
def cargar_movimientos_caja(tree):
    for child in tree.get_children():
        tree.delete(child)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT fecha, tipo, monto, descripcion, usuario FROM caja ORDER BY fecha DESC")
    for mov in cur.fetchall():
        tree.insert("", "end", values=mov)
    conn.close()

def abrir_dialogo_movimiento(tipo, tree):
    ventana = tk.Toplevel(programa)
    ventana.title(f"Registrar {tipo.capitalize()}")
    ventana.geometry("320x150")
    tk.Label(ventana, text="Monto:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_monto = tk.Entry(ventana)
    entry_monto.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(ventana, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_desc = tk.Entry(ventana)
    entry_desc.grid(row=1, column=1, padx=5, pady=5)
    def guardar():
        try:
            monto = float(entry_monto.get())
        except ValueError:
            messagebox.showerror("Error", "Monto inválido.")
            return
        descripcion = entry_desc.get()
        registrar_movimiento_caja(tipo, monto, descripcion)
        cargar_movimientos_caja(tree)
        ventana.destroy()
    tk.Button(ventana, text="Guardar", command=guardar).grid(row=2, column=0, columnspan=2, pady=10)

def realizar_corte_caja_gui(tree):
    corte = realizar_corte_caja()
    tree.insert("", "end", values=(corte["fecha"], "CORTE", f"Entradas: {corte['entradas']}", f"Salidas: {corte['salidas']} - Saldo: {corte['saldo']}", "Sistema"))

##############lo mas importante con esto se agregan los productos
def abrir_dialogo_producto(tree_productos=None):
    ventana = tk.Toplevel(programa)
    ventana.title("Nuevo Producto")
    campos = ["id", "nombre", "categoria", "precio", "cantidad", "proveedor", "codigo_barras", "descripcion", "unidad_medida", "iva", "descuento"]
    entradas = {}
    for i, campo in enumerate(campos):
        tk.Label(ventana, text=campo.capitalize()+":").grid(row=i, column=0, padx=5, pady=4, sticky="e")
        e = tk.Entry(ventana)
        e.grid(row=i, column=1, padx=5, pady=4)
        entradas[campo] = e
    def guardar():
        datos = {campo: entradas[campo].get() for campo in campos}
        try:
            datos["precio"] = float(datos["precio"])
            datos["cantidad"] = int(datos["cantidad"])
            datos["iva"] = float(datos["iva"])
            datos["descuento"] = float(datos["descuento"])
        except Exception:
            messagebox.showerror("Error", "Precio, cantidad, IVA y descuento deben ser numéricos.")
            return
        registrar_producto(datos)
        messagebox.showinfo("Éxito", "Producto registrado correctamente.")
        ventana.destroy()
        if tree_productos is not None:
            cargar_productos_en_tree(tree_productos)
    tk.Button(ventana, text="Guardar", command=guardar).grid(row=len(campos), column=0, columnspan=2, pady=8)


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

boton_pestana4 = customtkinter.CTkButton(marco_navegacion, text="Punto de Venta", command=lambda: pestana_por_defecto("pestana4"))
boton_pestana4.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

boton_pestana5 = customtkinter.CTkButton(marco_navegacion, text="Caja", command=lambda: pestana_por_defecto("pestana5"))
boton_pestana5.grid(row=6, column=0, sticky="ew", padx=10, pady=5)

boton_pestana6 = customtkinter.CTkButton(marco_navegacion, text="Productos", command=lambda: pestana_por_defecto("pestana6"))
boton_pestana6.grid(row=7, column=0, sticky="ew", padx=10, pady=5)
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

pestana4 = customtkinter.CTkFrame(programa, corner_radius=0)


pestana5 = customtkinter.CTkFrame(programa, corner_radius=0)


pestana6 = customtkinter.CTkFrame(programa, corner_radius=0)


imagen_original = Image.open(r'C:\Users\Santiago\Desktop\Ing. en Sistemas - UIA\3er CUATRIMESTRE\PROGRAMACION II\prograDos\programacionDos\assets\petmatepng1.png')
imagen_redimensionada = imagen_original.resize((150, 150), Image.Resampling.LANCZOS) ## Se redimensiona la imagen usando la libreria PIL, y su funcion resize.
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)                                ## Se asigna la imagen redimensionada

redirigir_a_inicio()
crear_tablas_db()
cargar_productos_prueba()
# Ejecutar la aplicación
programa.mainloop()

################################### Inicializar Programa#########################
