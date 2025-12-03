@echo off
echo ========================================
echo Creando Ejecutable para Presentacion
echo Sistema de Gestion Ambiental
echo (Incluye datos de ejemplo pre-cargados)
echo ========================================
echo.

REM Verificar que PyInstaller esté instalado
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller no esta instalado. Instalando...
    python -m pip install pyinstaller
)

echo.
echo Creando ejecutable con datos de ejemplo...
echo.

REM Crear ejecutable sin consola que incluye datos de ejemplo
pyinstaller --name SistemaGestionAmbiental_Presentacion ^
    --onefile ^
    --windowed ^
    --noconsole ^
    --add-data "templates;templates" ^
    --add-data "datos_ejemplo.py;." ^
    --hidden-import flask ^
    --hidden-import flask_sqlalchemy ^
    --hidden-import werkzeug ^
    --hidden-import sqlalchemy ^
    --hidden-import jinja2 ^
    --hidden-import webbrowser ^
    --hidden-import threading ^
    --collect-all flask ^
    --collect-all werkzeug ^
    --icon=NONE ^
    launcher_con_datos.py

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo crear el ejecutable
    pause
    exit /b 1
)

echo.
echo ========================================
echo Ejecutable para presentacion creado!
echo ========================================
echo.
echo El ejecutable se encuentra en: dist\SistemaGestionAmbiental_Presentacion.exe
echo.
echo CARACTERISTICAS:
echo   - Sin ventana de consola visible
echo   - Abre el navegador automaticamente
echo   - Incluye datos de ejemplo pre-cargados
echo   - Listo para presentacion en la universidad
echo.
echo NOTA: Este ejecutable es para uso en presentaciones.
echo       Los datos se cargan automaticamente la primera vez.
echo.
pause

