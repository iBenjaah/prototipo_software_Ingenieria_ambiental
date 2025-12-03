@echo off
echo ========================================
echo Creando Paquete Completo de Distribucion
echo Sistema de Gestion Ambiental
echo ========================================
echo.

REM Paso 1: Crear estructura de distribucion
echo [1/4] Creando estructura de distribucion...
call crear_paquete.bat

REM Paso 2: Crear ejecutable (opcional)
echo.
echo [2/4] ¿Desea crear el ejecutable? (S/N)
set /p crear_exe=
if /i "%crear_exe%"=="S" (
    call crear_ejecutable_amigable.bat
    if exist "dist\SistemaGestionAmbiental.exe" (
        copy "dist\SistemaGestionAmbiental.exe" "distribucion\SistemaGestionAmbiental\"
        echo Ejecutable copiado al paquete.
    )
)

REM Paso 3: Crear archivo ZIP
echo.
echo [3/4] Creando archivo ZIP...
if exist "SistemaGestionAmbiental.zip" del "SistemaGestionAmbiental.zip"

cd distribucion
powershell Compress-Archive -Path "SistemaGestionAmbiental\*" -DestinationPath "..\SistemaGestionAmbiental.zip" -Force
cd ..

echo Archivo ZIP creado: SistemaGestionAmbiental.zip

REM Paso 4: Informacion sobre instalador
echo.
echo [4/4] Informacion sobre instalador
echo.
echo Para crear un instalador con Inno Setup:
echo 1. Instalar Inno Setup desde: https://jrsoftware.org/isinfo.php
echo 2. Abrir el archivo: crear_instalador.iss
echo 3. Compilar el instalador desde Inno Setup
echo.
echo El instalador se creara en: instalador\SistemaGestionAmbiental_Instalador.exe
echo.

echo ========================================
echo Paquete completo creado!
echo ========================================
echo.
echo Archivos generados:
echo   - distribucion\SistemaGestionAmbiental\ (carpeta completa)
echo   - SistemaGestionAmbiental.zip (archivo comprimido)
if exist "distribucion\SistemaGestionAmbiental\SistemaGestionAmbiental.exe" (
    echo   - SistemaGestionAmbiental.exe (ejecutable)
)
echo.
pause

