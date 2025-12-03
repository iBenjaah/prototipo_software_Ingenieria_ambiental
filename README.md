# Sistema Informático de Gestión Ambiental
## Seguimiento de Variables Críticas en la Producción y Ciclo de Vida de Baterías Zinc-Aire

### Descripción

Sistema informático desarrollado para el seguimiento y gestión de variables ambientales críticas asociadas al ciclo de vida y desempeño ambiental de las baterías zinc-aire tipo botón. El sistema permite monitorear, registrar y analizar datos relacionados con la producción, consumos de recursos, generación de residuos, reciclaje y recuperación de materiales.

### Características Principales

- **Gestión de Producción**: Registro de producción diaria, lotes y tasa de rechazo
- **Monitoreo de Consumos**: Seguimiento de consumo de agua, energía, zinc, KOH y otros materiales
- **Gestión de Residuos**: Registro de pilas usadas, rechazadas, efluentes alcalinos y su destino
- **Reciclaje y Recuperación**: Seguimiento de materiales recuperados (zinc, acero, KOH)
- **Indicadores Ambientales**: Cálculo automático de indicadores clave de desempeño ambiental
- **Reportes**: Generación de reportes por período con análisis de tendencias
- **Evaluación de Escenarios**: Herramienta para evaluar mejoras basadas en economía circular
- **Dashboard Interactivo**: Visualización de datos con gráficos y métricas en tiempo real

### Requisitos del Sistema

- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Edge, Safari)

### Instalación

#### Opción 1: Instalación Rápida (Recomendada)

1. **Extraer el archivo ZIP** del sistema en una carpeta
2. **Ejecutar `instalar.bat`** para instalar dependencias
3. **Ejecutar `iniciar.bat`** para iniciar el sistema
4. **Abrir en el navegador**: `http://127.0.0.1:5000`

#### Opción 2: Instalación Manual

1. **Instalar Python 3.8+** desde https://www.python.org/downloads/
2. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación**:
```bash
python app.py
```

4. **Abrir en el navegador**:
   - Navegar a: `http://127.0.0.1:5000`

#### Opción 3: Usar Ejecutable

Si se incluye el ejecutable `SistemaGestionAmbiental.exe`:
1. **Doble clic** en `SistemaGestionAmbiental.exe`
2. **Abrir en el navegador**: `http://127.0.0.1:5000`

#### Generar Datos de Ejemplo

Para ver el sistema con datos de ejemplo:
```bash
python datos_ejemplo.py
```
O ejecutar: `generar_datos.bat`

### Estructura del Proyecto

```
.
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── README.md             # Este archivo
├── gestion_ambiental.db  # Base de datos SQLite (se crea automáticamente)
├── templates/            # Plantillas HTML
│   ├── base.html
│   ├── dashboard.html
│   ├── produccion.html
│   ├── consumos.html
│   ├── residuos.html
│   ├── reciclaje.html
│   ├── indicadores.html
│   ├── reportes.html
│   └── escenarios.html
└── static/               # Archivos estáticos (CSS, JS, imágenes)
```

### Módulos del Sistema

#### 1. Dashboard
Vista principal con indicadores clave, gráficos de tendencias y registros recientes.

#### 2. Producción
Registro y seguimiento de la producción diaria de baterías, incluyendo lotes y unidades rechazadas.

#### 3. Consumos
Monitoreo de consumo de recursos críticos:
- Agua (L)
- Energía (kWh)
- Zinc (kg)
- Hidróxido de Potasio - KOH (kg)
- Otros materiales

#### 4. Residuos
Gestión de residuos generados:
- Pilas usadas
- Pilas rechazadas
- Efluentes alcalinos
- Residuos sólidos

#### 5. Reciclaje
Seguimiento de materiales recuperados mediante procesos de reciclaje y reproceso.

#### 6. Indicadores Ambientales
Cálculo automático de indicadores como:
- Tasa de rechazo
- Consumo de recursos por unidad producida
- Tasa de reciclaje
- Tasa de recuperación de materiales
- Generación de residuos por unidad

#### 7. Reportes
Generación de reportes por período con análisis detallado de producción, consumos, residuos y reciclaje.

#### 8. Escenarios
Herramienta para evaluar escenarios de mejora basados en estrategias de economía circular.

### Variables Críticas Monitoreadas

1. **Consumo de Agua**: Litros consumidos en el proceso
2. **Consumo de Energía**: kWh utilizados
3. **Consumo de Zinc**: Kilogramos de zinc utilizados
4. **Consumo de KOH**: Kilogramos de hidróxido de potasio
5. **Pilas Usadas**: Unidades de pilas agotadas
6. **Pilas Rechazadas**: Unidades rechazadas en producción
7. **Efluentes Alcalinos**: Volumen de efluentes generados
8. **Material Recuperado**: Cantidad de materiales recuperados mediante reciclaje

### Relación con Objetivos de Desarrollo Sostenible (ODS)

El sistema contribuye al seguimiento de:
- **ODS 6**: Agua Limpia y Saneamiento
- **ODS 7**: Energía Asequible y No Contaminante
- **ODS 12**: Producción y Consumo Responsables
- **ODS 13**: Acción por el Clima

### Base de Datos

El sistema utiliza SQLite como base de datos local. La base de datos se crea automáticamente al ejecutar la aplicación por primera vez. Los datos se almacenan en el archivo `gestion_ambiental.db` en el directorio raíz del proyecto.

### Notas Importantes

- Este es un sistema de **uso local** (no requiere conexión a internet ni servicios en la nube)
- Todos los datos se almacenan localmente en SQLite
- La aplicación se ejecuta en `http://127.0.0.1:5000` por defecto
- Para producción, se recomienda usar un servidor WSGI como Gunicorn

### Soporte

Para consultas o problemas, revisar la documentación del proyecto o contactar al equipo de desarrollo.

### Licencia

Este software fue desarrollado como parte de un proyecto académico de Ingeniería Ambiental.

---

**Versión**: 1.0.0  
**Fecha**: Diciembre 2025

