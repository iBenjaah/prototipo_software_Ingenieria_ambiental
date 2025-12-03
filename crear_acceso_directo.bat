@echo off
echo ========================================
echo Crear Acceso Directo en el Escritorio
echo Sistema de Gestion Ambiental
echo ========================================
echo.

set "TARGET=%~dp0dist\SistemaGestionAmbiental.exe"
set "DESKTOP=%USERPROFILE%\Desktop"
set "LINK=%DESKTOP%\Sistema Gestion Ambiental.lnk"

echo Creando acceso directo en el escritorio...
echo.

REM Crear acceso directo usando PowerShell
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%LINK%'); $Shortcut.TargetPath = '%TARGET%'; $Shortcut.WorkingDirectory = '%~dp0dist'; $Shortcut.Description = 'Sistema de Gestión Ambiental - Baterías Zinc-Aire'; $Shortcut.Save()"

if exist "%LINK%" (
    echo.
    echo ========================================
    echo Acceso directo creado exitosamente!
    echo ========================================
    echo.
    echo Ubicacion: %LINK%
    echo.
    echo Ahora puedes ejecutar el sistema desde el escritorio.
    echo.
) else (
    echo.
    echo ERROR: No se pudo crear el acceso directo.
    echo.
    echo Puedes crearlo manualmente:
    echo 1. Clic derecho en dist\SistemaGestionAmbiental.exe
    echo 2. Enviar a ^> Escritorio (crear acceso directo)
    echo.
)

pause

