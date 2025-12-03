@echo off
echo ========================================
echo Creando Paquete de Instalacion
echo Sistema de Gestion Ambiental
echo ========================================
echo.

REM Crear directorio de distribucion
if exist "distribucion" rmdir /s /q "distribucion"
mkdir "distribucion"
mkdir "distribucion\SistemaGestionAmbiental"

echo Copiando archivos...
copy "app.py" "distribucion\SistemaGestionAmbiental\"
copy "requirements.txt" "distribucion\SistemaGestionAmbiental\"
copy "datos_ejemplo.py" "distribucion\SistemaGestionAmbiental\"
copy "README.md" "distribucion\SistemaGestionAmbiental\"
xcopy /E /I "templates" "distribucion\SistemaGestionAmbiental\templates"
if exist "static" xcopy /E /I "static" "distribucion\SistemaGestionAmbiental\static"

echo.
echo Creando script de instalacion...
(
echo @echo off
echo echo ========================================
echo echo Instalacion del Sistema de Gestion Ambiental
echo echo ========================================
echo echo.
echo echo Instalando dependencias de Python...
echo python -m pip install --upgrade pip
echo python -m pip install -r requirements.txt
echo echo.
echo echo ========================================
echo echo Instalacion completada!
echo echo ========================================
echo echo.
echo echo Para iniciar el sistema, ejecute: iniciar.bat
echo echo.
echo pause
) > "distribucion\SistemaGestionAmbiental\instalar.bat"

echo Creando script de inicio...
(
echo @echo off
echo echo ========================================
echo echo Sistema de Gestion Ambiental
echo echo Baterias Zinc-Aire
echo echo ========================================
echo echo.
echo echo Iniciando servidor...
echo echo.
echo echo El sistema estara disponible en:
echo echo http://127.0.0.1:5000
echo echo.
echo echo Presione Ctrl+C para detener el servidor
echo echo.
echo python app.py
echo pause
) > "distribucion\SistemaGestionAmbiental\iniciar.bat"

echo Creando script de datos de ejemplo...
(
echo @echo off
echo echo Generando datos ficticios de ejemplo...
echo python datos_ejemplo.py
echo echo.
echo echo Datos generados exitosamente!
echo pause
) > "distribucion\SistemaGestionAmbiental\generar_datos.bat"

echo.
echo ========================================
echo Paquete creado en: distribucion\SistemaGestionAmbiental
echo ========================================
echo.
pause

