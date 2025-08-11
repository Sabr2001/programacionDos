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

from proveedores_pagos_db import (
    proveedor_crear, proveedores_listar,
    factura_registrar, facturas_listar,
    pago_registrar
)


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
    
# == PROVEEDORES ==
def on_guardar_proveedor():
    proveedor_crear(
        nombre=prov_nombre.get(),
        cedula_juridica=prov_cedula.get(),
        telefono=prov_tel.get(),
        email=prov_email.get(),
        banco=prov_banco.get(),
        cuenta=prov_cuenta.get()
    )
    messagebox.showinfo("OK", "Proveedor guardado")
    cargar_proveedores()

def cargar_proveedores():
    for i in tree_proveedores.get_children():
        tree_proveedores.delete(i)
    for r in proveedores_listar():
        tree_proveedores.insert("", "end", values=(r["id"], r["nombre"], r["telefono"], r["email"]))

# == FACTURAS / PAGOS ==
def on_crear_factura():
    fid = factura_registrar(
        proveedor_id=int(fac_prov_id.get()),
        numero=fac_numero.get(),
        monto_total=float(fac_monto.get()),
        descripcion=fac_desc.get()
    )
    messagebox.showinfo("OK", f"Factura {fid} creada")
    cargar_facturas()

def on_abonar():
    pago_registrar(
        factura_id=int(pago_factura_id.get()),
        monto=float(pago_monto.get()),
        metodo=pago_metodo.get(),
        nota=pago_nota.get()
    )
    messagebox.showinfo("OK", "Pago registrado")
    cargar_facturas()

def cargar_facturas():
    for i in tree_facturas.get_children():
        tree_facturas.delete(i)
    for f in facturas_listar():
        tree_facturas.insert("", "end", values=(
            f["factura_id"], f["proveedor_id"], f["numero"],
            f["monto_total"], f["monto_pagado"], f["saldo"]
        ))

    
#################################<FIN METODOS Y FUNCIONES >########################################################

############################# Inicio Estructura y vista de la Ventana##############################################
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de pestañas con botón")
ventana.geometry("600x600")

imagen_original = Image.open(r"C:\Users\Emily\Documents\GitHub\programacionDos\assets\petmate2.PNG")
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

# Nuevas pestañas 
pestana_proveedores = ttk.Frame(notebook)
pestana_pagos = ttk.Frame(notebook)
notebook.add(pestana_proveedores, text='Proveedores')
notebook.add(pestana_pagos, text='Pagos')

# PROVEEDORES 
frm_prov = ttk.Frame(pestana_proveedores, padding=10)
frm_prov.pack(fill="both", expand=True)

# Entradas
ttk.Label(frm_prov, text="Nombre:").grid(row=0, column=0, sticky="e")
prov_nombre = ttk.Entry(frm_prov, width=30); prov_nombre.grid(row=0, column=1, padx=5, pady=2)

ttk.Label(frm_prov, text="Cédula jurídica:").grid(row=1, column=0, sticky="e")
prov_cedula = ttk.Entry(frm_prov, width=30); prov_cedula.grid(row=1, column=1, padx=5, pady=2)

ttk.Label(frm_prov, text="Teléfono:").grid(row=2, column=0, sticky="e")
prov_tel = ttk.Entry(frm_prov, width=30); prov_tel.grid(row=2, column=1, padx=5, pady=2)

ttk.Label(frm_prov, text="Email:").grid(row=3, column=0, sticky="e")
prov_email = ttk.Entry(frm_prov, width=30); prov_email.grid(row=3, column=1, padx=5, pady=2)

ttk.Label(frm_prov, text="Banco:").grid(row=4, column=0, sticky="e")
prov_banco = ttk.Entry(frm_prov, width=30); prov_banco.grid(row=4, column=1, padx=5, pady=2)

ttk.Label(frm_prov, text="Cuenta:").grid(row=5, column=0, sticky="e")
prov_cuenta = ttk.Entry(frm_prov, width=30); prov_cuenta.grid(row=5, column=1, padx=5, pady=2)

btn_prov_guardar = ttk.Button(frm_prov, text="Guardar proveedor", command=on_guardar_proveedor)
btn_prov_guardar.grid(row=6, column=1, sticky="w", pady=6)

# Tabla de proveedores
cols_p = ("ID", "Nombre", "Teléfono", "Email")
tree_proveedores = ttk.Treeview(frm_prov, columns=cols_p, show="headings", height=8)
for c in cols_p:
    tree_proveedores.heading(c, text=c)
tree_proveedores.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=8)

frm_prov.rowconfigure(7, weight=1)
frm_prov.columnconfigure(1, weight=1)

# FACTURAS / PAGOS
frm_fac = ttk.Frame(pestana_pagos, padding=10)
frm_fac.pack(fill="both", expand=True)

# Crear factura
ttk.Label(frm_fac, text="Proveedor ID:").grid(row=0, column=0, sticky="e")
fac_prov_id = ttk.Entry(frm_fac, width=10); fac_prov_id.grid(row=0, column=1, padx=5, pady=2, sticky="w")

ttk.Label(frm_fac, text="N° Factura:").grid(row=0, column=2, sticky="e")
fac_numero = ttk.Entry(frm_fac, width=14); fac_numero.grid(row=0, column=3, padx=5, pady=2, sticky="w")

ttk.Label(frm_fac, text="Monto total:").grid(row=1, column=0, sticky="e")
fac_monto = ttk.Entry(frm_fac, width=14); fac_monto.grid(row=1, column=1, padx=5, pady=2, sticky="w")

ttk.Label(frm_fac, text="Descripción:").grid(row=1, column=2, sticky="e")
fac_desc = ttk.Entry(frm_fac, width=30); fac_desc.grid(row=1, column=3, padx=5, pady=2, sticky="w")

btn_fac_crear = ttk.Button(frm_fac, text="Crear factura", command=on_crear_factura)
btn_fac_crear.grid(row=0, column=4, rowspan=2, padx=10)

# Abonar pago
ttk.Label(frm_fac, text="Factura ID:").grid(row=2, column=0, sticky="e")
pago_factura_id = ttk.Entry(frm_fac, width=10); pago_factura_id.grid(row=2, column=1, padx=5, pady=2, sticky="w")

ttk.Label(frm_fac, text="Monto pago:").grid(row=2, column=2, sticky="e")
pago_monto = ttk.Entry(frm_fac, width=14); pago_monto.grid(row=2, column=3, padx=5, pady=2, sticky="w")

ttk.Label(frm_fac, text="Método:").grid(row=3, column=0, sticky="e")
pago_metodo = ttk.Entry(frm_fac, width=14); pago_metodo.grid(row=3, column=1, padx=5, pady=2, sticky="w")

ttk.Label(frm_fac, text="Nota:").grid(row=3, column=2, sticky="e")
pago_nota = ttk.Entry(frm_fac, width=30); pago_nota.grid(row=3, column=3, padx=5, pady=2, sticky="w")

btn_abonar = ttk.Button(frm_fac, text="Registrar pago", command=on_abonar)
btn_abonar.grid(row=2, column=4, rowspan=2, padx=10)

# Tabla de facturas
cols_f = ("FacturaID", "ProveedorID", "Número", "Total", "Pagado", "Saldo")
tree_facturas = ttk.Treeview(frm_fac, columns=cols_f, show="headings", height=10)
for c in cols_f:
    tree_facturas.heading(c, text=c)
tree_facturas.grid(row=4, column=0, columnspan=5, sticky="nsew", pady=8)

frm_fac.rowconfigure(4, weight=1)
for c in range(5):
    frm_fac.columnconfigure(c, weight=1)



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

# Cargar listas al inicio 
try:
    cargar_proveedores()
    cargar_facturas()
except Exception as e:
    print("Aviso:", e)


# Ejecutar la aplicación
ventana.mainloop()