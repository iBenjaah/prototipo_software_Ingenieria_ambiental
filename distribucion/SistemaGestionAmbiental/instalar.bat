@echo off
echo ========================================
echo Instalacion del Sistema de Gestion Ambiental
echo ========================================
echo.
echo Instalando dependencias de Python...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.
echo ========================================
echo Instalacion completada!
echo ========================================
echo.
echo Para iniciar el sistema, ejecute: iniciar.bat
echo.
pause

