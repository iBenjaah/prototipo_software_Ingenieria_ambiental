# Archivos .bat del Proyecto

## Archivos Mantenidos (Activos)

### 1. `crear_ejecutable_amigable.bat`
**Propósito**: Crear el ejecutable mejorado (sin consola, abre navegador automáticamente)  
**Uso**: Ejecutar cuando necesites generar el ejecutable para distribución  
**Ubicación**: Raíz del proyecto

### 2. `crear_paquete.bat`
**Propósito**: Crear la estructura básica del paquete de distribución  
**Uso**: Crea la carpeta `distribucion\SistemaGestionAmbiental\` con todos los archivos necesarios  
**Ubicación**: Raíz del proyecto

### 3. `crear_paquete_completo.bat`
**Propósito**: Crear el paquete completo incluyendo ejecutable y ZIP  
**Uso**: Ejecutar para generar todo el paquete listo para distribuir  
**Ubicación**: Raíz del proyecto

### 4. `crear_acceso_directo.bat`
**Propósito**: Crear un acceso directo en el escritorio del ejecutable  
**Uso**: Ejecutar para facilitar el acceso al sistema desde el escritorio  
**Ubicación**: Raíz del proyecto

### 5. `subir_release.bat`
**Propósito**: Ayudar a crear un release en GitHub con el ejecutable  
**Uso**: Ejecutar cuando quieras subir una nueva versión a GitHub  
**Ubicación**: Raíz del proyecto

## Archivos en Carpeta de Distribución

Los siguientes archivos están en `distribucion\SistemaGestionAmbiental\` y son parte del paquete:

- `instalar.bat` - Instala dependencias Python (para usuarios que no usen el ejecutable)
- `iniciar.bat` - Inicia el sistema manualmente (para usuarios que no usen el ejecutable)
- `generar_datos.bat` - Genera datos ficticios de ejemplo

## Archivos Eliminados (Obsoletos)

- ❌ `crear_ejecutable.bat` - Reemplazado por `crear_ejecutable_amigable.bat`
- ❌ `iniciar.bat` (raíz) - Ya no necesario, ahora usamos el ejecutable

## Flujo de Trabajo Recomendado

1. **Desarrollo**: Usar `python app.py` directamente
2. **Crear Ejecutable**: Ejecutar `crear_ejecutable_amigable.bat`
3. **Crear Paquete**: Ejecutar `crear_paquete_completo.bat`
4. **Subir Release**: Ejecutar `subir_release.bat` o manualmente en GitHub

