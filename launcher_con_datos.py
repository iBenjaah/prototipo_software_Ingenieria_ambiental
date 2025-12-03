"""
Launcher con datos de ejemplo pre-cargados
Versión para presentación - Incluye datos ficticios automáticamente
"""

import sys
import os
import webbrowser
import threading
import time

def open_browser():
    """Abre el navegador después de que el servidor inicie"""
    time.sleep(2)  # Esperar a que el servidor esté listo
    webbrowser.open('http://127.0.0.1:5000')

def cargar_datos_ejemplo():
    """Carga datos de ejemplo si la base de datos está vacía"""
    try:
        from app import app, db, Produccion, ConsumoRecursos, GestionResiduos, Reciclaje
        
        with app.app_context():
            # Verificar si hay datos
            total_produccion = Produccion.query.count()
            
            if total_produccion == 0:
                print("Cargando datos de ejemplo para la presentación...")
                # Importar y ejecutar el script de datos
                from datos_ejemplo import insertar_datos_ejemplo
                insertar_datos_ejemplo()
                print("✓ Datos de ejemplo cargados exitosamente")
            else:
                print(f"✓ Base de datos ya contiene {total_produccion} registros de producción")
    except Exception as e:
        print(f"Advertencia: No se pudieron cargar datos de ejemplo: {e}")

def main():
    """Función principal del launcher con datos"""
    print("=" * 50)
    print("Sistema de Gestión Ambiental")
    print("Versión para Presentación - Con Datos de Ejemplo")
    print("=" * 50)
    print()
    
    # Cargar datos de ejemplo
    cargar_datos_ejemplo()
    
    print()
    print("Iniciando servidor...")
    print("El navegador se abrirá automáticamente.")
    print("Presione Ctrl+C para cerrar el sistema.")
    print()
    
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

