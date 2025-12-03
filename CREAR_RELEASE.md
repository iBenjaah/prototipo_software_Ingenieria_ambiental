# Guía para Crear Release en GitHub

## Ubicación del Ejecutable

El archivo ejecutable se encuentra en:
- **`dist\SistemaGestionAmbiental.exe`** (49.5 MB aproximadamente)

## Pasos para Crear un Release en GitHub

### Opción 1: Desde la Interfaz Web de GitHub

1. **Ir al repositorio**: https://github.com/iBenjaah/prototipo_software_Ingenieria_ambiental

2. **Crear un nuevo release**:
   - Click en "Releases" (lado derecho de la página)
   - Click en "Create a new release" o "Draft a new release"

3. **Completar la información**:
   - **Tag version**: `v1.0.0` (o la versión que desees)
   - **Release title**: `Sistema de Gestión Ambiental v1.0.0`
   - **Description**: 
     ```
     ## Sistema de Gestión Ambiental - Baterías Zinc-Aire
     
     Primera versión del sistema completo.
     
     ### Características:
     - Gestión de producción
     - Monitoreo de consumos
     - Gestión de residuos
     - Reciclaje y recuperación
     - Indicadores ambientales
     - Reportes y escenarios
     
     ### Instalación:
     1. Descargar `SistemaGestionAmbiental.exe`
     2. Ejecutar el archivo
     3. Abrir navegador en: http://127.0.0.1:5000
     
     ### Requisitos:
     - Windows 10 o superior
     - Navegador web moderno
     ```

4. **Subir el ejecutable**:
   - Arrastrar y soltar `dist\SistemaGestionAmbiental.exe` en la sección "Attach binaries"
   - O hacer click en "Attach binaries" y seleccionar el archivo

5. **Publicar**:
   - Click en "Publish release"

### Opción 2: Usando GitHub CLI (gh)

Si tienes GitHub CLI instalado:

```bash
gh release create v1.0.0 dist\SistemaGestionAmbiental.exe --title "Sistema de Gestión Ambiental v1.0.0" --notes "Primera versión del sistema completo"
```

## Archivos para el Release

### Archivo Principal:
- `dist\SistemaGestionAmbiental.exe` (ejecutable standalone)

### Archivos Opcionales (puedes incluirlos también):
- `SistemaGestionAmbiental.zip` (paquete completo con código fuente)
- `README.md` (documentación)

## Notas Importantes

- El ejecutable incluye todas las dependencias, no requiere Python instalado
- El tamaño del ejecutable es aproximadamente 49.5 MB
- Los usuarios pueden ejecutarlo directamente sin instalación adicional

