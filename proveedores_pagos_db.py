# -*- coding: utf-8 -*-
import sqlite3

# crea/abre la BD en el mismo folder
CONEXION = sqlite3.connect("pos.db")
CONEXION.row_factory = sqlite3.Row
cur = CONEXION.cursor()


try:
    cur.execute("""
        CREATE TABLE proveedores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cedula_juridica TEXT,
            telefono TEXT,
            email TEXT,
            banco TEXT,
            cuenta TEXT,
            activo INTEGER DEFAULT 1
        )
    """)
    print("Se creó la tabla 'proveedores'")
except sqlite3.OperationalError:
    print("La tabla 'proveedores' ya existe")

try:
    cur.execute("""
        CREATE TABLE proveedor_facturas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proveedor_id INTEGER NOT NULL,
            numero TEXT,
            fecha TEXT DEFAULT (date('now')),
            descripcion TEXT,
            monto_total REAL NOT NULL,
            estado TEXT DEFAULT 'PENDIENTE',
            FOREIGN KEY(proveedor_id) REFERENCES proveedores(id)
        )
    """)
    print("Se creó la tabla 'proveedor_facturas'")
except sqlite3.OperationalError:
    print("La tabla 'proveedor_facturas' ya existe")

try:
    cur.execute("""
        CREATE TABLE proveedor_pagos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            factura_id INTEGER NOT NULL,
            fecha TEXT DEFAULT (date('now')),
            monto REAL NOT NULL,
            metodo TEXT,
            nota TEXT,
            FOREIGN KEY(factura_id) REFERENCES proveedor_facturas(id) ON DELETE CASCADE
        )
    """)
    print("Se creó la tabla 'proveedor_pagos'")
except sqlite3.OperationalError:
    print("La tabla 'proveedor_pagos' ya existe")

# vista de saldos
try:
    cur.execute("DROP VIEW IF EXISTS vw_proveedor_saldos")
    cur.execute("""
        CREATE VIEW vw_proveedor_saldos AS
        SELECT f.id AS factura_id, f.proveedor_id, f.numero, f.fecha, f.descripcion,
               f.monto_total,
               IFNULL(SUM(p.monto), 0) AS monto_pagado,
               ROUND(f.monto_total - IFNULL(SUM(p.monto),0), 2) AS saldo
        FROM proveedor_facturas f
        LEFT JOIN proveedor_pagos p ON p.factura_id = f.id
        GROUP BY f.id
    """)
    print("Se creó/actualizó la vista 'vw_proveedor_saldos'")
except sqlite3.OperationalError:
    print("No se pudo crear la vista 'vw_proveedor_saldos'")

CONEXION.commit()

# ---- FUNCIONES ----
def proveedor_crear(nombre, cedula_juridica=None, telefono=None, email=None, banco=None, cuenta=None):
    CONEXION.execute("""
        INSERT INTO proveedores(nombre, cedula_juridica, telefono, email, banco, cuenta)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, cedula_juridica, telefono, email, banco, cuenta))
    CONEXION.commit()

def proveedores_listar(activos=True):
    return CONEXION.execute(
        "SELECT * FROM proveedores WHERE activo=? ORDER BY nombre",
        (1 if activos else 0,)
    ).fetchall()

def factura_registrar(proveedor_id, numero, monto_total, descripcion=""):
    cur = CONEXION.cursor()
    cur.execute("""
        INSERT INTO proveedor_facturas(proveedor_id, numero, monto_total, descripcion)
        VALUES (?, ?, ?, ?)
    """, (proveedor_id, numero, monto_total, descripcion))
    CONEXION.commit()
    return cur.lastrowid

def facturas_listar(proveedor_id=None):
    if proveedor_id:
        return CONEXION.execute(
            "SELECT * FROM vw_proveedor_saldos WHERE proveedor_id=? ORDER BY fecha DESC",
            (proveedor_id,)
        ).fetchall()
    return CONEXION.execute("SELECT * FROM vw_proveedor_saldos ORDER BY fecha DESC").fetchall()

def pago_registrar(factura_id, monto, metodo=None, nota=None):
    CONEXION.execute("""
        INSERT INTO proveedor_pagos(factura_id, monto, metodo, nota) VALUES (?, ?, ?, ?)
    """, (factura_id, monto, metodo, nota))
    # actualizar estado según saldo
    row = CONEXION.execute(
        "SELECT saldo FROM vw_proveedor_saldos WHERE factura_id=?",
        (factura_id,)
    ).fetchone()
    if row is not None:
        saldo = row["saldo"]
        nuevo = "PAGADA" if saldo <= 0 else "ABONADA"
        CONEXION.execute("UPDATE proveedor_facturas SET estado=? WHERE id=?", (nuevo, factura_id))
    CONEXION.commit()

# Prueba
if __name__ == "__main__":
    if not proveedores_listar():
        proveedor_crear("VetDistribuciones S.A.", "3-101-999999", "2222-3333", "ventas@vetdis.com", "BAC", "123456-001")
    prov = proveedores_listar()[0]
    fid = factura_registrar(prov["id"], "F-0001", 150000, "Pienso + jeringas")
    pago_registrar(fid, 50000, "SINPE", "Abono")
    for f in facturas_listar(prov["id"]):
        print(dict(f))
