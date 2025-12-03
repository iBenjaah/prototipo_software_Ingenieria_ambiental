"""
Launcher amigable para el Sistema de Gestión Ambiental
Abre el navegador automáticamente y oculta la consola
"""

import sys
import os
import webbrowser
import threading
import time
import subprocess

def open_browser():
    """Abre el navegador después de que el servidor inicie"""
    time.sleep(2)  # Esperar a que el servidor esté listo
    webbrowser.open('http://127.0.0.1:5000')

def main():
    """Función principal del launcher"""
    print("Iniciando Sistema de Gestión Ambiental...")
    print("El navegador se abrirá automáticamente.")
    print("Presione Ctrl+C para cerrar el sistema.\n")
    
    # Iniciar el navegador en un thread separado
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Ejecutar la aplicación Flask
    try:
        from app import app, init_db
        init_db()
        app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)
    except KeyboardInterrupt:
        print("\n\nCerrando sistema...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError al iniciar el sistema: {e}")
        input("\nPresione Enter para salir...")
        sys.exit(1)

if __name__ == '__main__':
    main()

