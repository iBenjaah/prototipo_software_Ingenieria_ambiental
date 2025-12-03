# Guía de Instalación - Sistema de Gestión Ambiental

## Requisitos del Sistema

- **Windows 10 o superior**
- **Python 3.8 o superior** (descargar de https://www.python.org/downloads/)
- **Navegador web moderno** (Chrome, Firefox, Edge, Safari)

## Instalación Manual

### Paso 1: Instalar Python

1. Descargar Python desde https://www.python.org/downloads/
2. Durante la instalación, **asegurarse de marcar** "Add Python to PATH"
3. Verificar la instalación abriendo PowerShell y ejecutando:
   ```
   python --version
   ```

### Paso 2: Instalar el Sistema

1. Extraer el archivo ZIP del sistema en una carpeta (ej: `C:\SistemaGestionAmbiental`)
2. Abrir PowerShell o CMD en esa carpeta
3. Ejecutar el script de instalación:
   ```
   instalar.bat
   ```
   O manualmente:
   ```
   python -m pip install -r requirements.txt
   ```

### Paso 3: Generar Datos de Ejemplo (Opcional)

Para ver el sistema con datos de ejemplo, ejecutar:
```
generar_datos.bat
```
O manualmente:
```
python datos_ejemplo.py
```

### Paso 4: Iniciar el Sistema

1. Ejecutar `iniciar.bat` o desde la línea de comandos:
   ```
   python app.py
   ```
2. Abrir el navegador en: `http://127.0.0.1:5000`

## Estructura de Archivos

```
SistemaGestionAmbiental/
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── datos_ejemplo.py      # Script para generar datos de ejemplo
├── instalar.bat          # Script de instalación
├── iniciar.bat           # Script para iniciar el sistema
├── generar_datos.bat     # Script para generar datos
├── README.md             # Documentación
├── templates/            # Plantillas HTML
└── gestion_ambiental.db  # Base de datos (se crea automáticamente)
```

## Solución de Problemas

### Error: "python no se reconoce como comando"
- Verificar que Python esté instalado y agregado al PATH
- Reintentar con: `python3` o `py`

### Error: "No module named 'flask'"
- Ejecutar: `python -m pip install -r requirements.txt`

### El puerto 5000 está en uso
- Cerrar otras aplicaciones que usen el puerto 5000
- O modificar el puerto en `app.py` (línea final)

### No se pueden ver los datos
- Ejecutar `generar_datos.bat` para crear datos de ejemplo

## Desinstalación

1. Detener el servidor (Ctrl+C)
2. Eliminar la carpeta del sistema
3. (Opcional) Desinstalar Python si no se usa para otros proyectos

## Soporte

Para consultas o problemas, revisar el archivo README.md o contactar al equipo de desarrollo.

---

**Versión**: 1.0.0  
**Fecha**: Diciembre 2025

