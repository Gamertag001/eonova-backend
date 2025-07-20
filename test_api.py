import requests
import json

# URL base de la API (cambia esto por tu URL de Vercel cuando la despliegues)
BASE_URL = "http://localhost:8000"

def test_api():
    """Función para probar los endpoints de la API"""
    
    print("🧪 Probando API de Eonova...\n")
    
    # 1. Probar endpoint raíz
    print("1. Probando endpoint raíz...")
    response = requests.get(f"{BASE_URL}/")
    print(f"   Status: {response.status_code}")
    print(f"   Respuesta: {response.json()}\n")
    
    # 2. Obtener productos
    print("2. Obteniendo productos...")
    response = requests.get(f"{BASE_URL}/productos")
    print(f"   Status: {response.status_code}")
    productos = response.json()
    print(f"   Productos encontrados: {len(productos['productos'])}")
    for producto in productos['productos']:
        print(f"   - {producto['nombre']}: ${producto['precio_base']}")
    print()
    
    # 3. Obtener colores disponibles
    print("3. Obteniendo colores disponibles...")
    response = requests.get(f"{BASE_URL}/colores-disponibles")
    print(f"   Status: {response.status_code}")
    colores = response.json()
    print(f"   Colores: {', '.join(colores['colores'][:5])}...")
    print()
    
    # 4. Calcular precio de personalización
    print("4. Calculando precio de personalización...")
    data = {
        "producto_id": "prod_001",
        "color_principal": "azul",
        "color_secundario": "rojo",
        "estilo": "deportivo",
        "estampado": "geométrico"
    }
    response = requests.post(f"{BASE_URL}/calcular-precio", json=data)
    print(f"   Status: {response.status_code}")
    precio = response.json()
    print(f"   Precio base: ${precio['precio_base']}")
    print(f"   Precio final: ${precio['precio_final']}")
    print(f"   Desglose: {precio['desglose']}")
    print()
    
    # 5. Crear una personalización
    print("5. Creando personalización...")
    personalizacion_data = {
        "id": "",
        "producto_id": "prod_001",
        "color_principal": "azul",
        "color_secundario": "rojo",
        "estilo": "deportivo",
        "estampado": "geométrico",
        "talle": "M",
        "precio_final": precio['precio_final'],
        "fecha_creacion": ""
    }
    response = requests.post(f"{BASE_URL}/personalizaciones", json=personalizacion_data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        personalizacion = response.json()
        print(f"   Personalización creada con ID: {personalizacion['personalizacion']['id']}")
    print()
    
    # 6. Obtener estadísticas
    print("6. Obteniendo estadísticas...")
    response = requests.get(f"{BASE_URL}/estadisticas")
    print(f"   Status: {response.status_code}")
    stats = response.json()
    print(f"   Total productos: {stats['total_productos']}")
    print(f"   Total personalizaciones: {stats['total_personalizaciones']}")
    print(f"   Total pedidos: {stats['total_pedidos']}")
    print(f"   Total usuarios: {stats['total_usuarios']}")
    print(f"   Ventas totales: ${stats['ventas_totales']}")
    print()
    
    print("✅ Pruebas completadas!")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar al servidor.")
        print("   Asegúrate de que el servidor esté ejecutándose con: python backend.py")
    except Exception as e:
        print(f"❌ Error: {e}") 