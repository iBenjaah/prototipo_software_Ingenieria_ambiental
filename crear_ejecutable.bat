@echo off
echo ========================================
echo Creando Ejecutable
echo Sistema de Gestion Ambiental
echo ========================================
echo.

REM Verificar que PyInstaller esté instalado
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller no esta instalado. Instalando...
    python -m pip install pyinstaller
)

echo.
echo Creando ejecutable...
echo.

REM Crear ejecutable con PyInstaller
pyinstaller --name SistemaGestionAmbiental ^
    --onefile ^
    --console ^
    --add-data "templates;templates" ^
    --hidden-import flask ^
    --hidden-import flask_sqlalchemy ^
    --hidden-import werkzeug ^
    --hidden-import sqlalchemy ^
    --hidden-import jinja2 ^
    --collect-all flask ^
    --collect-all werkzeug ^
    app.py

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo crear el ejecutable
    pause
    exit /b 1
)

echo.
echo ========================================
echo Ejecutable creado exitosamente!
echo ========================================
echo.
echo El ejecutable se encuentra en: dist\SistemaGestionAmbiental.exe
echo.
echo NOTA: El ejecutable incluye todas las dependencias.
echo       Solo necesita ejecutarlo para iniciar el sistema.
echo.
pause

