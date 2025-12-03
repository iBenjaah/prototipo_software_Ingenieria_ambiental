# Guía de Distribución - Sistema de Gestión Ambiental

## Crear Paquete de Distribución

### Método 1: Paquete Simple (Recomendado)

Ejecutar el script:
```batch
crear_paquete.bat
```

Esto creará una carpeta `distribucion\SistemaGestionAmbiental\` con todos los archivos necesarios.

### Método 2: Paquete Completo con Ejecutable

Ejecutar el script:
```batch
crear_paquete_completo.bat
```

Esto creará:
- Carpeta de distribución
- Ejecutable (si se desea)
- Archivo ZIP comprimido

### Método 3: Crear Instalador (Requiere Inno Setup)

1. **Instalar Inno Setup** desde: https://jrsoftware.org/isinfo.php
2. **Abrir** el archivo `crear_instalador.iss` en Inno Setup
3. **Compilar** el instalador (Build > Compile)
4. El instalador se creará en: `instalador\SistemaGestionAmbiental_Instalador.exe`

## Estructura del Paquete de Distribución

```
SistemaGestionAmbiental/
├── app.py                      # Aplicación principal
├── requirements.txt            # Dependencias Python
├── datos_ejemplo.py            # Script para generar datos
├── instalar.bat                # Script de instalación
├── iniciar.bat                 # Script para iniciar
├── generar_datos.bat           # Script para datos de ejemplo
├── README.md                   # Documentación principal
├── INSTALACION.md              # Guía de instalación
├── templates/                  # Plantillas HTML
│   ├── base.html
│   ├── dashboard.html
│   ├── produccion.html
│   ├── consumos.html
│   ├── residuos.html
│   ├── reciclaje.html
│   ├── indicadores.html
│   ├── reportes.html
│   └── escenarios.html
└── (Opcional) SistemaGestionAmbiental.exe  # Ejecutable
```

## Archivos para Distribuir

### Versión Mínima (Sin Ejecutable)
- Todos los archivos `.py`
- Carpeta `templates/`
- Archivos `.bat` (instalar, iniciar, generar_datos)
- `requirements.txt`
- `README.md` y `INSTALACION.md`

### Versión Completa (Con Ejecutable)
- Todo lo anterior +
- `SistemaGestionAmbiental.exe`

### Versión con Instalador
- `SistemaGestionAmbiental_Instalador.exe` (creado con Inno Setup)

## Notas Importantes

1. **Base de datos**: El archivo `gestion_ambiental.db` se crea automáticamente al ejecutar, no debe incluirse en la distribución.

2. **Datos de ejemplo**: Los usuarios pueden ejecutar `generar_datos.bat` para crear datos ficticios.

3. **Requisitos**: El usuario debe tener Python 3.8+ instalado (excepto si usa el ejecutable).

4. **Puerto**: El sistema usa el puerto 5000 por defecto. Si está ocupado, modificar `app.py`.

## Verificación del Paquete

Antes de distribuir, verificar:
- [ ] Todos los archivos están presentes
- [ ] Los scripts `.bat` funcionan correctamente
- [ ] El ejecutable (si existe) inicia correctamente
- [ ] La documentación está completa
- [ ] Los datos de ejemplo se generan correctamente

## Distribución

1. **Comprimir** la carpeta `SistemaGestionAmbiental` en un ZIP
2. **O usar** el instalador creado con Inno Setup
3. **Incluir** la guía de instalación (`INSTALACION.md`)

---

**Versión**: 1.0.0  
**Fecha**: Diciembre 2025

