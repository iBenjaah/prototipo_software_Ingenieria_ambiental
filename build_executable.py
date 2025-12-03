"""
Script para crear ejecutable usando PyInstaller
"""

import PyInstaller.__main__
import os
import shutil

# Configuración
app_name = "SistemaGestionAmbiental"
main_script = "app.py"
icon_path = None  # Puedes agregar un icono .ico si lo tienes

# Limpiar builds anteriores
if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('dist'):
    shutil.rmtree('dist')
if os.path.exists(f'{app_name}.spec'):
    os.remove(f'{app_name}.spec')

# Opciones de PyInstaller
options = [
    main_script,
    '--name', app_name,
    '--onefile',  # Un solo archivo ejecutable
    '--windowed',  # Sin consola (ocultar ventana de consola)
    '--add-data', 'templates;templates',  # Incluir templates
    '--hidden-import', 'flask',
    '--hidden-import', 'flask_sqlalchemy',
    '--hidden-import', 'werkzeug',
    '--hidden-import', 'sqlalchemy',
    '--hidden-import', 'jinja2',
    '--collect-all', 'flask',
    '--collect-all', 'werkzeug',
]

# Si hay icono, agregarlo
if icon_path and os.path.exists(icon_path):
    options.extend(['--icon', icon_path])

print("Creando ejecutable...")
PyInstaller.__main__.run(options)

print(f"\n✅ Ejecutable creado en: dist/{app_name}.exe")

