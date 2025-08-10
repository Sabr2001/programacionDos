################################################################
#Nombre del Programa: 
#Numero de Grupo de trabajo: 03
#Nombre de los Programadores: Santiago Bonilla
#Version del PYTHON: 3.13
#nombre del IDE donde se trabajo el codigo: VSC
###############################################################

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import customtkinter
import sqlite3
from datetime import datetime #########para las bases de datos 
import os #####es para conectarse al sistema operativo y poder usar la carpeta

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

DB_FILE = "petmate.db" #esta es la base de datos

ejecucion_carga_clientes = False
ejecucio_carga_inventario = False
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

############################apartado para buscar productos
def buscar_producto(codigo=None, nombre=None, clave=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if codigo:
        cursor.execute("SELECT * FROM productos WHERE codigo_barras=?", (codigo,))
    elif nombre:
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
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

#================================= Variables y Datos Auxiliares =======================#
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
    
    clientes = [
    {"nombre":"Santiago", "apellido":"Bonilla", "id":"1", "email":"sbr@hotmail.com", "mascota":"Rufus", "codigo":"ABC123"},
    {"nombre":"Rachell", "apellido":"McAdams","id":"2", "email":"rmcadams@hotmail.com", "mascota":"Fifi", "codigo":"DEF456"}
]

def index_inventario(root):
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
    return frame

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
    return frame

def cargar_productos_en_tree(tree):
    for child in tree.get_children():
        tree.delete(child)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, categoria, precio, cantidad, proveedor FROM productos")
    for prod in cur.fetchall():
        tree.insert("", "end", values=prod)
    conn.close()
    
    
    
    
##############importante, primero tyenemos que agregar los productos a la base de datos, los que agregue como ejemplo no funcioonan
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
    return frame

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


##########la navegacion y eso
programa = customtkinter.CTk()
programa.title("PetMate - Veterinaria")
programa.geometry("900x600")
programa.grid_rowconfigure(0, weight=1)
programa.grid_columnconfigure(1, weight=1)

#########navegacion
marco_navegacion = customtkinter.CTkFrame(programa, corner_radius=0)
marco_navegacion.grid(row=0, column=0, sticky="nsew")
marco_navegacion.grid_rowconfigure(7, weight=1)
marco_navegacion_label = customtkinter.CTkLabel(marco_navegacion, text="  Menú Navegación", font=customtkinter.CTkFont(size=15, weight="bold"))
marco_navegacion_label.grid(row=0, column=0, padx=20, pady=20)
############botones
boton_inicio = customtkinter.CTkButton(marco_navegacion, text="Inicio", command=lambda: pestana_por_defecto("inicio"))
boton_inicio.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
boton_pestana1 = customtkinter.CTkButton(marco_navegacion, text="Clientes", command=lambda: pestana_por_defecto("pestana1"))
boton_pestana1.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
boton_pestana2 = customtkinter.CTkButton(marco_navegacion, text="Inventario", command=lambda: pestana_por_defecto("pestana2"))
boton_pestana2.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
boton_pestana3 = customtkinter.CTkButton(marco_navegacion, text="Servicios", command=lambda: pestana_por_defecto("pestana3"))
boton_pestana3.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
boton_pestana4 = customtkinter.CTkButton(marco_navegacion, text="Punto de Venta", command=lambda: pestana_por_defecto("pestana4"))
boton_pestana4.grid(row=5, column=0, sticky="ew", padx=10, pady=5)
boton_pestana5 = customtkinter.CTkButton(marco_navegacion, text="Caja", command=lambda: pestana_por_defecto("pestana5"))
boton_pestana5.grid(row=6, column=0, sticky="ew", padx=10, pady=5)
boton_pestana6 = customtkinter.CTkButton(marco_navegacion, text="Productos", command=lambda: pestana_por_defecto("pestana6"))
boton_pestana6.grid(row=7, column=0, sticky="ew", padx=10, pady=5)
############contenido
pestana_inicio = customtkinter.CTkFrame(programa, corner_radius=0)
pestana_inicio.grid_columnconfigure(0, weight=1)
label_inicio = customtkinter.CTkLabel(pestana_inicio, text="Bienvenido a PetMate", font=("TkHeadingFont", 24,"bold"))
label_inicio.grid(row=0, column=0, pady=50)

pestana1 = customtkinter.CTkFrame(programa, corner_radius=0)
pestana2 = customtkinter.CTkFrame(programa, corner_radius=0)
pestana3 = customtkinter.CTkFrame(programa, corner_radius=0)
pestana4 = customtkinter.CTkFrame(programa, corner_radius=0)
pestana5 = customtkinter.CTkFrame(programa, corner_radius=0)
pestana6 = customtkinter.CTkFrame(programa, corner_radius=0)

#############pestanas
def pestana_por_defecto(name):
    boton_inicio.configure(fg_color="gray" if name == "inicio" else "transparent")
    boton_pestana1.configure(fg_color="gray" if name == "pestana1" else "transparent")
    boton_pestana2.configure(fg_color="gray" if name == "pestana2" else "transparent")
    boton_pestana3.configure(fg_color="gray" if name == "pestana3" else "transparent")
    boton_pestana4.configure(fg_color="gray" if name == "pestana4" else "transparent")
    boton_pestana5.configure(fg_color="gray" if name == "pestana5" else "transparent")
    boton_pestana6.configure(fg_color="gray" if name == "pestana6" else "transparent")

##########esconde lo demas
    pestana_inicio.grid_forget()
    pestana1.grid_forget()
    pestana2.grid_forget()
    pestana3.grid_forget()
    pestana4.grid_forget()
    pestana5.grid_forget()
    pestana6.grid_forget()

    global ejecucion_carga_clientes, ejecucio_carga_inventario, ejecucion_carga_punto_venta, ejecucion_carga_caja, ejecucion_carga_productos

    if name == "inicio":
        pestana_inicio.grid(row=0, column=1, sticky="nsew")
    elif name == "pestana1":
        pestana1.grid(row=0, column=1, sticky="nsew")
        if not ejecucion_carga_clientes:
            # crear vista clientes
            frame = index_clientes(pestana1)
            frame.pack(fill="both", expand=True)
            ejecucion_carga_clientes = True
    elif name == "pestana2":
        pestana2.grid(row=0, column=1, sticky="nsew")
        if not ejecucio_carga_inventario:
            frame = index_inventario(pestana2)
            frame.pack(fill="both", expand=True)
            ejecucio_carga_inventario = True
    elif name == "pestana3":
        pestana3.grid(row=0, column=1, sticky="nsew")
        lbl = customtkinter.CTkLabel(pestana3, text="Servicios (pendiente)", font=("Arial", 16))
        lbl.pack(pady=20)
    elif name == "pestana4":
        pestana4.grid(row=0, column=1, sticky="nsew")
        if not ejecucion_carga_punto_venta:
            frame = index_punto_venta(pestana4)
            frame.pack(fill="both", expand=True)
            ejecucion_carga_punto_venta = True
    elif name == "pestana5":
        pestana5.grid(row=0, column=1, sticky="nsew")
        if not ejecucion_carga_caja:
            frame = index_caja(pestana5)
            frame.pack(fill="both", expand=True)
            ejecucion_carga_caja = True
    elif name == "pestana6":
        pestana6.grid(row=0, column=1, sticky="nsew")
        if not ejecucion_carga_productos:
            frame = index_productos(pestana6)
            frame.pack(fill="both", expand=True)
            ejecucion_carga_productos = True

###########esto inicializa la base de datos
crear_tablas_db()
cargar_productos_prueba()


pestana_por_defecto("inicio")
programa.mainloop()
