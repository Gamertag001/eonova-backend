from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json
import uuid
from datetime import datetime
import os

# Configuración de la aplicación
app = FastAPI(
    title="Eonova API",
    description="API para personalización de ropa - Eonova",
    version="1.0.0"
)

# Configurar CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de datos
class Producto(BaseModel):
    id: str
    nombre: str
    categoria: str
    precio_base: float
    descripcion: str
    talles_disponibles: List[str]
    colores_base: List[str]
    imagen_base: str

class Personalizacion(BaseModel):
    id: str
    producto_id: str
    color_principal: str
    color_secundario: Optional[str] = None
    estilo: str
    estampado: Optional[str] = None
    talle: str
    precio_final: float
    fecha_creacion: str

class Pedido(BaseModel):
    id: str
    usuario_id: str
    personalizaciones: List[Personalizacion]
    total: float
    estado: str
    fecha_pedido: str
    direccion_envio: str

class Usuario(BaseModel):
    id: str
    nombre: str
    email: str
    telefono: Optional[str] = None

# Base de datos simulada (en producción usarías una base de datos real)
productos_db = {}
personalizaciones_db = {}
pedidos_db = {}
usuarios_db = {}

# Datos de ejemplo
def inicializar_datos():
    productos_ejemplo = [
        {
            "id": "prod_001",
            "nombre": "Camiseta Básica",
            "categoria": "camisetas",
            "precio_base": 25.00,
            "descripcion": "Camiseta de algodón 100% personalizable",
            "talles_disponibles": ["XS", "S", "M", "L", "XL", "XXL"],
            "colores_base": ["blanco", "negro", "gris", "azul", "rojo"],
            "imagen_base": "camiseta_base.jpg"
        },
        {
            "id": "prod_002",
            "nombre": "Hoodie Clásico",
            "categoria": "hoodies",
            "precio_base": 45.00,
            "descripcion": "Hoodie con capucha personalizable",
            "talles_disponibles": ["S", "M", "L", "XL", "XXL"],
            "colores_base": ["negro", "gris", "azul marino", "verde"],
            "imagen_base": "hoodie_base.jpg"
        },
        {
            "id": "prod_003",
            "nombre": "Pantalón Deportivo",
            "categoria": "pantalones",
            "precio_base": 35.00,
            "descripcion": "Pantalón deportivo personalizable",
            "talles_disponibles": ["28", "30", "32", "34", "36", "38"],
            "colores_base": ["negro", "gris", "azul", "verde"],
            "imagen_base": "pantalon_base.jpg"
        }
    ]
    
    for producto in productos_ejemplo:
        productos_db[producto["id"]] = producto

# Inicializar datos al arrancar
inicializar_datos()

# Rutas de la API

@app.get("/")
async def root():
    return {"mensaje": "¡Bienvenido a Eonova API! Tu tienda de ropa personalizable"}

@app.get("/productos")
async def obtener_productos():
    """Obtener todos los productos disponibles"""
    return {"productos": list(productos_db.values())}

@app.get("/productos/{producto_id}")
async def obtener_producto(producto_id: str):
    """Obtener un producto específico por ID"""
    if producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos_db[producto_id]

@app.get("/productos/categoria/{categoria}")
async def obtener_productos_por_categoria(categoria: str):
    """Obtener productos por categoría"""
    productos_categoria = [
        producto for producto in productos_db.values() 
        if producto["categoria"].lower() == categoria.lower()
    ]
    return {"productos": productos_categoria}

@app.post("/personalizaciones")
async def crear_personalizacion(personalizacion: Personalizacion):
    """Crear una nueva personalización"""
    if personalizacion.producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Generar ID único si no se proporciona
    if not personalizacion.id:
        personalizacion.id = str(uuid.uuid4())
    
    # Establecer fecha de creación
    personalizacion.fecha_creacion = datetime.now().isoformat()
    
    personalizaciones_db[personalizacion.id] = personalizacion.dict()
    return {"mensaje": "Personalización creada exitosamente", "personalizacion": personalizacion}

@app.get("/personalizaciones/{personalizacion_id}")
async def obtener_personalizacion(personalizacion_id: str):
    """Obtener una personalización específica"""
    if personalizacion_id not in personalizaciones_db:
        raise HTTPException(status_code=404, detail="Personalización no encontrada")
    return personalizaciones_db[personalizacion_id]

@app.post("/pedidos")
async def crear_pedido(pedido: Pedido):
    """Crear un nuevo pedido"""
    # Generar ID único si no se proporciona
    if not pedido.id:
        pedido.id = str(uuid.uuid4())
    
    # Establecer fecha del pedido
    pedido.fecha_pedido = datetime.now().isoformat()
    
    pedidos_db[pedido.id] = pedido.dict()
    return {"mensaje": "Pedido creado exitosamente", "pedido": pedido}

@app.get("/pedidos/{pedido_id}")
async def obtener_pedido(pedido_id: str):
    """Obtener un pedido específico"""
    if pedido_id not in pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedidos_db[pedido_id]

@app.get("/pedidos/usuario/{usuario_id}")
async def obtener_pedidos_usuario(usuario_id: str):
    """Obtener todos los pedidos de un usuario"""
    pedidos_usuario = [
        pedido for pedido in pedidos_db.values() 
        if pedido["usuario_id"] == usuario_id
    ]
    return {"pedidos": pedidos_usuario}

@app.put("/pedidos/{pedido_id}/estado")
async def actualizar_estado_pedido(pedido_id: str, estado: str):
    """Actualizar el estado de un pedido"""
    if pedido_id not in pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    pedidos_db[pedido_id]["estado"] = estado
    return {"mensaje": "Estado del pedido actualizado", "pedido": pedidos_db[pedido_id]}

@app.post("/usuarios")
async def crear_usuario(usuario: Usuario):
    """Crear un nuevo usuario"""
    # Generar ID único si no se proporciona
    if not usuario.id:
        usuario.id = str(uuid.uuid4())
    
    usuarios_db[usuario.id] = usuario.dict()
    return {"mensaje": "Usuario creado exitosamente", "usuario": usuario}

@app.get("/usuarios/{usuario_id}")
async def obtener_usuario(usuario_id: str):
    """Obtener un usuario específico"""
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios_db[usuario_id]

@app.get("/estilos-disponibles")
async def obtener_estilos_disponibles():
    """Obtener estilos disponibles para personalización"""
    estilos = [
        "clásico", "deportivo", "elegante", "casual", "vintage", 
        "moderno", "minimalista", "colorido", "monocromático"
    ]
    return {"estilos": estilos}

@app.get("/estampados-disponibles")
async def obtener_estampados_disponibles():
    """Obtener estampados disponibles"""
    estampados = [
        "floral", "geométrico", "animal print", "abstracto", "texto", 
        "logotipo", "rayas", "cuadros", "puntos", "sin estampado"
    ]
    return {"estampados": estampados}

@app.get("/colores-disponibles")
async def obtener_colores_disponibles():
    """Obtener colores disponibles"""
    colores = [
        "blanco", "negro", "gris", "azul", "rojo", "verde", "amarillo", 
        "naranja", "rosa", "morado", "marrón", "beige", "azul marino"
    ]
    return {"colores": colores}

@app.post("/calcular-precio")
async def calcular_precio_personalizacion(
    producto_id: str,
    color_principal: str,
    color_secundario: Optional[str] = None,
    estilo: str = "clásico",
    estampado: Optional[str] = None
):
    """Calcular el precio de una personalización"""
    if producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto = productos_db[producto_id]
    precio_base = producto["precio_base"]
    
    # Cálculo de precio según personalizaciones
    precio_final = precio_base
    
    # Costo adicional por color secundario
    if color_secundario:
        precio_final += 5.00
    
    # Costo adicional por estampado
    if estampado and estampado != "sin estampado":
        precio_final += 8.00
    
    # Costo adicional por estilo especial
    if estilo in ["elegante", "vintage"]:
        precio_final += 3.00
    
    return {
        "precio_base": precio_base,
        "precio_final": round(precio_final, 2),
        "desglose": {
            "color_secundario": 5.00 if color_secundario else 0.00,
            "estampado": 8.00 if estampado and estampado != "sin estampado" else 0.00,
            "estilo_especial": 3.00 if estilo in ["elegante", "vintage"] else 0.00
        }
    }

@app.get("/estadisticas")
async def obtener_estadisticas():
    """Obtener estadísticas generales de la tienda"""
    total_productos = len(productos_db)
    total_personalizaciones = len(personalizaciones_db)
    total_pedidos = len(pedidos_db)
    total_usuarios = len(usuarios_db)
    
    # Calcular ventas totales
    ventas_totales = sum(pedido["total"] for pedido in pedidos_db.values())
    
    return {
        "total_productos": total_productos,
        "total_personalizaciones": total_personalizaciones,
        "total_pedidos": total_pedidos,
        "total_usuarios": total_usuarios,
        "ventas_totales": round(ventas_totales, 2)
    }

# Configuración para Vercel
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
