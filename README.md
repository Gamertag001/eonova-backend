# Eonova - API de Personalización de Ropa

## Descripción
Backend API para Eonova, una plataforma de personalización de ropa donde los usuarios pueden personalizar colores, estilos, estampados y más directamente en la página web.

## Características
- ✅ Gestión de productos (camisetas, hoodies, pantalones)
- ✅ Sistema de personalización (colores, estilos, estampados)
- ✅ Gestión de pedidos y usuarios
- ✅ Cálculo automático de precios
- ✅ API RESTful completa
- ✅ Documentación automática con Swagger

## Tecnologías
- **FastAPI** - Framework web moderno y rápido
- **Python 3.8+** - Lenguaje de programación
- **Pydantic** - Validación de datos
- **Vercel** - Plataforma de despliegue

## Instalación Local

1. Clona el repositorio:
```bash
git clone <tu-repositorio>
cd pagina-web
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el servidor:
```bash
python backend.py
```

4. Abre tu navegador en: `http://localhost:8000`

## Despliegue en Vercel

1. Instala Vercel CLI:
```bash
npm i -g vercel
```

2. Despliega el proyecto:
```bash
vercel
```

3. Sigue las instrucciones en pantalla

## Endpoints de la API

### Productos
- `GET /productos` - Obtener todos los productos
- `GET /productos/{id}` - Obtener producto específico
- `GET /productos/categoria/{categoria}` - Productos por categoría

### Personalizaciones
- `POST /personalizaciones` - Crear personalización
- `GET /personalizaciones/{id}` - Obtener personalización

### Pedidos
- `POST /pedidos` - Crear pedido
- `GET /pedidos/{id}` - Obtener pedido
- `GET /pedidos/usuario/{usuario_id}` - Pedidos de usuario
- `PUT /pedidos/{id}/estado` - Actualizar estado

### Usuarios
- `POST /usuarios` - Crear usuario
- `GET /usuarios/{id}` - Obtener usuario

### Utilidades
- `GET /estilos-disponibles` - Lista de estilos
- `GET /estampados-disponibles` - Lista de estampados
- `GET /colores-disponibles` - Lista de colores
- `POST /calcular-precio` - Calcular precio personalización
- `GET /estadisticas` - Estadísticas de la tienda

## Documentación de la API
Una vez ejecutado el servidor, puedes acceder a la documentación automática en:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Estructura del Proyecto
```
pagina-web/
├── backend.py          # API principal
├── requirements.txt    # Dependencias
├── vercel.json        # Configuración Vercel
└── README.md          # Documentación
```

## Próximos Pasos
1. Crear el frontend con HTML, CSS y JavaScript
2. Integrar base de datos real (PostgreSQL, MongoDB)
3. Implementar autenticación de usuarios
4. Agregar sistema de pagos
5. Implementar carga de imágenes

## Contacto
Para más información sobre Eonova, contacta al equipo de desarrollo. 