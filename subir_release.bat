@echo off
echo ========================================
echo Subir Release a GitHub
echo Sistema de Gestion Ambiental
echo ========================================
echo.

REM Verificar que el ejecutable existe
if not exist "dist\SistemaGestionAmbiental.exe" (
    echo ERROR: No se encuentra el ejecutable en dist\SistemaGestionAmbiental.exe
    echo.
    echo Creando ejecutable...
    call crear_ejecutable.bat
    if errorlevel 1 (
        echo ERROR: No se pudo crear el ejecutable
        pause
        exit /b 1
    )
)

echo Ejecutable encontrado: dist\SistemaGestionAmbiental.exe
echo.

REM Verificar si GitHub CLI está instalado
where gh >nul 2>&1
if %errorlevel% equ 0 (
    echo GitHub CLI detectado. ¿Desea crear el release automáticamente? (S/N)
    set /p usar_cli=
    if /i "%usar_cli%"=="S" (
        echo.
        echo Ingrese la version del release (ej: v1.0.0):
        set /p version=
        echo.
        echo Creando release %version%...
        gh release create %version% dist\SistemaGestionAmbiental.exe --title "Sistema de Gestión Ambiental %version%" --notes "Sistema completo de gestión ambiental para baterías zinc-aire. Ejecutable standalone que incluye todas las dependencias."
        if errorlevel 1 (
            echo ERROR: No se pudo crear el release
            pause
            exit /b 1
        )
        echo.
        echo ========================================
        echo Release creado exitosamente!
        echo ========================================
        pause
        exit /b 0
    )
)

echo.
echo ========================================
echo INSTRUCCIONES MANUALES
echo ========================================
echo.
echo 1. Abrir el navegador y ir a:
echo    https://github.com/iBenjaah/prototipo_software_Ingenieria_ambiental/releases/new
echo.
echo 2. Completar:
echo    - Tag version: v1.0.0
echo    - Release title: Sistema de Gestión Ambiental v1.0.0
echo    - Description: (ver CREAR_RELEASE.md)
echo.
echo 3. Arrastrar el archivo: dist\SistemaGestionAmbiental.exe
echo.
echo 4. Click en "Publish release"
echo.
echo ========================================
echo.
echo El ejecutable está listo en: dist\SistemaGestionAmbiental.exe
echo Tamaño: 
for %%A in ("dist\SistemaGestionAmbiental.exe") do echo   %%~zA bytes
echo.
pause

