# 🚀 Guía de Despliegue - Eonova en Vercel

## 📋 **Paso a Paso Completo**

### **1. Preparar tu repositorio en GitHub**

1. Ve a [GitHub.com](https://github.com) y crea una cuenta si no tienes
2. Crea un nuevo repositorio llamado `eonova-backend`
3. Sube tus archivos:
   ```bash
   git init
   git add .
   git commit -m "Primer commit - Backend Eonova"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/eonova-backend.git
   git push -u origin main
   ```

### **2. Conectar GitHub con Vercel**

1. Ve a [Vercel.com](https://vercel.com) y crea una cuenta
2. Haz clic en "New Project"
3. Selecciona tu repositorio `eonova-backend`
4. Vercel detectará automáticamente que es Python

### **3. Configuración en Vercel**

Vercel leerá automáticamente estos archivos:
- `requirements.txt` → Instala las librerías
- `vercel.json` → Configura cómo ejecutar la app
- `backend.py` → Tu aplicación principal

### **4. Despliegue Automático**

Una vez conectado:
- Cada vez que hagas `git push` a GitHub
- Vercel automáticamente desplegará tu aplicación
- Te dará una URL como: `https://tu-app.vercel.app`

## 📁 **Archivos Necesarios (Solo estos 4)**

```
eonova-backend/
├── backend.py          ← Tu aplicación principal
├── requirements.txt    ← Librerías necesarias
├── vercel.json        ← Configuración para Vercel
└── README.md          ← Documentación
```

## 🔧 **¿Qué hace cada archivo?**

### `backend.py`
- Tu aplicación principal
- Contiene toda la lógica de la API
- **NO necesitas cambiarlo**

### `requirements.txt`
- Lista de librerías que necesita Python
- Vercel las instala automáticamente
- **NO necesitas cambiarlo**

### `vercel.json`
- Le dice a Vercel: "Ejecuta `backend.py` con Python"
- **NO necesitas cambiarlo**

## 🌐 **Después del Despliegue**

Tu API estará disponible en:
- **API**: `https://tu-app.vercel.app`
- **Documentación**: `https://tu-app.vercel.app/docs`

## 📝 **Comandos Útiles**

```bash
# Ver el estado de tu repositorio
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Descripción de los cambios"

# Subir a GitHub (esto activará el despliegue automático)
git push
```

## ❓ **Preguntas Frecuentes**

**Q: ¿Necesito instalar algo en mi computadora?**
A: Solo Git y Python. Vercel hace todo lo demás.

**Q: ¿Qué pasa si cambio el código?**
A: Haz `git push` y Vercel se actualiza automáticamente.

**Q: ¿Es gratis?**
A: Sí, Vercel tiene un plan gratuito muy generoso.

## 🎯 **Próximo Paso**

Una vez que tengas tu backend funcionando en Vercel, podrás crear tu frontend con HTML, CSS y JavaScript que se conecte a tu API.

¿Tienes alguna duda sobre algún paso específico? 