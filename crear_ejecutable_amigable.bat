@echo off
echo ========================================
echo Creando Ejecutable Amigable
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
echo Creando ejecutable sin consola (modo ventana)...
echo.

REM Crear ejecutable sin consola que abre el navegador automáticamente
pyinstaller --name SistemaGestionAmbiental ^
    --onefile ^
    --windowed ^
    --noconsole ^
    --add-data "templates;templates" ^
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
    launcher.py

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
echo CARACTERISTICAS:
echo   - Sin ventana de consola visible
echo   - Abre el navegador automaticamente
echo   - Listo para usar con doble clic
echo.
pause

