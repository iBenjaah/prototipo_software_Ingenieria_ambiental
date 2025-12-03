"""
Script para insertar datos ficticios de ejemplo en la base de datos
"""

from app import app, db, Produccion, ConsumoRecursos, GestionResiduos, Reciclaje
from datetime import date, timedelta
import random

def insertar_datos_ejemplo():
    """Inserta datos ficticios de ejemplo"""
    
    with app.app_context():
        # Limpiar datos existentes (opcional - comentar si quieres mantener datos)
        print("Limpiando datos existentes...")
        db.session.query(Reciclaje).delete()
        db.session.query(GestionResiduos).delete()
        db.session.query(ConsumoRecursos).delete()
        db.session.query(Produccion).delete()
        db.session.commit()
        
        print("Insertando datos ficticios...")
        
        # Generar datos de los últimos 12 meses (todo el año)
        fecha_inicio = date.today() - timedelta(days=365)
        
        # 1. Datos de Producción (diarios durante todo el año)
        print("  - Producción...")
        lotes = ['LOTE-2025-001', 'LOTE-2025-002', 'LOTE-2025-003', 'LOTE-2025-004', 
                 'LOTE-2025-005', 'LOTE-2025-006', 'LOTE-2025-007', 'LOTE-2025-008',
                 'LOTE-2025-009', 'LOTE-2025-010', 'LOTE-2025-011', 'LOTE-2025-012']
        lote_idx = 0
        
        # Generar producción para todo el año (días laborables)
        dias_totales = (date.today() - fecha_inicio).days
        for i in range(dias_totales):
            fecha = fecha_inicio + timedelta(days=i)
            # No producir los fines de semana
            if fecha.weekday() < 5:  # 0-4 = lunes a viernes
                # Variación estacional: más producción en meses centrales
                mes = fecha.month
                if mes in [3, 4, 5, 6, 7, 8, 9]:  # Marzo a Septiembre
                    cantidad_producida = random.randint(9000, 13000)
                else:
                    cantidad_producida = random.randint(7000, 11000)
                
                cantidad_rechazada = random.randint(int(cantidad_producida * 0.01), int(cantidad_producida * 0.05))
                lote = f"LOTE-{fecha.year}-{fecha.month:02d}-{lote_idx % 20 + 1:03d}"
                lote_idx += 1
                
                prod = Produccion(
                    fecha=fecha,
                    cantidad_producida=cantidad_producida,
                    cantidad_rechazada=cantidad_rechazada,
                    lote=lote,
                    observaciones=f"Producción normal del día" if cantidad_rechazada < cantidad_producida * 0.03 else "Alta tasa de rechazo detectada"
                )
                db.session.add(prod)
        
        db.session.commit()
        print(f"    ✓ {db.session.query(Produccion).count()} registros de producción insertados")
        
        # 2. Datos de Consumos (diarios durante todo el año)
        print("  - Consumos...")
        tipos_recursos = {
            'agua': {'unidad': 'L', 'rango_base': (40000, 60000), 'costo_rango': (50000, 80000)},
            'energia': {'unidad': 'kWh', 'rango_base': (8000, 12000), 'costo_rango': (1200000, 1800000)},
            'zinc': {'unidad': 'kg', 'rango_base': (4500, 5500), 'costo_rango': (13500, 16500)},
            'KOH': {'unidad': 'kg', 'rango_base': (200, 300), 'costo_rango': (600, 900)},
            'acero': {'unidad': 'kg', 'rango_base': (1000, 1500), 'costo_rango': (3000, 4500)}
        }
        
        # Generar consumos diarios para días laborables
        for i in range(dias_totales):
            fecha = fecha_inicio + timedelta(days=i)
            if fecha.weekday() < 5:  # Solo días laborables
                mes = fecha.month
                # Ajustar rangos según el mes (más consumo en meses de alta producción)
                factor_estacional = 1.2 if mes in [3, 4, 5, 6, 7, 8, 9] else 0.9
                
                # Agua
                rango_agua = (int(tipos_recursos['agua']['rango_base'][0] * factor_estacional),
                             int(tipos_recursos['agua']['rango_base'][1] * factor_estacional))
                consumo = ConsumoRecursos(
                    fecha=fecha,
                    tipo_recurso='agua',
                    cantidad=random.uniform(*rango_agua),
                    unidad=tipos_recursos['agua']['unidad'],
                    costo=random.uniform(*tipos_recursos['agua']['costo_rango']),
                    observaciones="Consumo diario de agua"
                )
                db.session.add(consumo)
                
                # Energía
                rango_energia = (int(tipos_recursos['energia']['rango_base'][0] * factor_estacional),
                               int(tipos_recursos['energia']['rango_base'][1] * factor_estacional))
                consumo = ConsumoRecursos(
                    fecha=fecha,
                    tipo_recurso='energia',
                    cantidad=random.uniform(*rango_energia),
                    unidad=tipos_recursos['energia']['unidad'],
                    costo=random.uniform(*tipos_recursos['energia']['costo_rango']),
                    observaciones="Consumo energético del proceso"
                )
                db.session.add(consumo)
                
                # Zinc
                rango_zinc = (int(tipos_recursos['zinc']['rango_base'][0] * factor_estacional),
                            int(tipos_recursos['zinc']['rango_base'][1] * factor_estacional))
                consumo = ConsumoRecursos(
                    fecha=fecha,
                    tipo_recurso='zinc',
                    cantidad=random.uniform(*rango_zinc),
                    unidad=tipos_recursos['zinc']['unidad'],
                    costo=random.uniform(*tipos_recursos['zinc']['costo_rango']),
                    observaciones="Consumo de zinc para ánodos"
                )
                db.session.add(consumo)
                
                # KOH
                rango_koh = (int(tipos_recursos['KOH']['rango_base'][0] * factor_estacional),
                           int(tipos_recursos['KOH']['rango_base'][1] * factor_estacional))
                consumo = ConsumoRecursos(
                    fecha=fecha,
                    tipo_recurso='KOH',
                    cantidad=random.uniform(*rango_koh),
                    unidad=tipos_recursos['KOH']['unidad'],
                    costo=random.uniform(*tipos_recursos['KOH']['costo_rango']),
                    observaciones="Hidróxido de potasio para electrolito"
                )
                db.session.add(consumo)
                
                # Acero (cada 3 días)
                if i % 3 == 0:
                    consumo = ConsumoRecursos(
                        fecha=fecha,
                        tipo_recurso='acero',
                        cantidad=random.uniform(*tipos_recursos['acero']['rango_base']),
                        unidad=tipos_recursos['acero']['unidad'],
                        costo=random.uniform(*tipos_recursos['acero']['costo_rango']),
                        observaciones="Consumo de acero para carcasas"
                    )
                    db.session.add(consumo)
        
        db.session.commit()
        print(f"    ✓ {db.session.query(ConsumoRecursos).count()} registros de consumos insertados")
        
        # 3. Datos de Residuos (semanal durante todo el año)
        print("  - Residuos...")
        for i in range(0, dias_totales, 7):  # Semanal
            fecha = fecha_inicio + timedelta(days=i)
            
            # Pilas rechazadas (reproceso interno)
            mes = fecha.month
            factor_prod = 1.2 if mes in [3, 4, 5, 6, 7, 8, 9] else 0.8
            cantidad_rechazadas = random.randint(int(200 * factor_prod), int(800 * factor_prod))
            
            residuo = GestionResiduos(
                fecha=fecha,
                tipo_residuo='pilas_rechazadas',
                cantidad=cantidad_rechazadas,
                unidad='unidades',
                destino='reproceso',
                gestor='Planta Interna',
                observaciones="Pilas rechazadas en control de calidad"
            )
            db.session.add(residuo)
            
            # Efluentes alcalinos (semanal)
            residuo = GestionResiduos(
                fecha=fecha,
                tipo_residuo='efluentes_alcalinos',
                cantidad=random.uniform(500 * factor_prod, 1500 * factor_prod),
                unidad='L',
                destino='tratamiento',
                gestor='Planta de Tratamiento ABC',
                observaciones="Efluentes con pH alto, requieren neutralización"
            )
            db.session.add(residuo)
            
            # Pilas usadas (recolección para reciclaje) - cada 2 semanas
            if i % 14 == 0:
                cantidad_pilas = random.randint(int(5000 * factor_prod), int(15000 * factor_prod))
                residuo = GestionResiduos(
                    fecha=fecha,
                    tipo_residuo='pilas_usadas',
                    cantidad=cantidad_pilas,
                    unidad='unidades',
                    destino='reciclaje',
                    gestor='Recicladora XYZ S.A.',
                    observaciones="Pilas recolectadas de puntos de acopio para reciclaje"
                )
                db.session.add(residuo)
                
                # También agregar algunas pilas rechazadas que van a reciclaje
                if random.random() > 0.4:  # 60% de probabilidad
                    residuo_rechazado = GestionResiduos(
                        fecha=fecha,
                        tipo_residuo='pilas_rechazadas',
                        cantidad=random.randint(int(100 * factor_prod), int(500 * factor_prod)),
                        unidad='unidades',
                        destino='reciclaje',
                        gestor='Planta Interna',
                        observaciones="Pilas rechazadas enviadas a reciclaje"
                    )
                    db.session.add(residuo_rechazado)
            
            # Residuos sólidos (ocasionalmente)
            if i % 21 == 0:  # Cada 3 semanas aproximadamente
                residuo = GestionResiduos(
                    fecha=fecha,
                    tipo_residuo='residuos_solidos',
                    cantidad=random.uniform(50, 200),
                    unidad='kg',
                    destino='disposicion_final',
                    gestor='Gestor de Residuos Sólidos',
                    observaciones="Residuos sólidos no reciclables"
                )
                db.session.add(residuo)
        
        db.session.commit()
        print(f"    ✓ {db.session.query(GestionResiduos).count()} registros de residuos insertados")
        
        # 4. Datos de Reciclaje (semanal durante todo el año)
        print("  - Reciclaje...")
        for i in range(0, dias_totales, 7):  # Semanal
            fecha = fecha_inicio + timedelta(days=i)
            mes = fecha.month
            factor_prod = 1.2 if mes in [3, 4, 5, 6, 7, 8, 9] else 0.8
            
            # Zinc recuperado
            reciclaje = Reciclaje(
                fecha=fecha,
                material_recuperado='zinc',
                cantidad=random.uniform(200 * factor_prod, 500 * factor_prod),
                unidad='kg',
                origen='pilas_usadas',
                valor_estimado=random.uniform(600 * factor_prod, 1500 * factor_prod),
                observaciones="Zinc recuperado de proceso de reciclaje"
            )
            db.session.add(reciclaje)
            
            # Acero recuperado
            reciclaje = Reciclaje(
                fecha=fecha,
                material_recuperado='acero',
                cantidad=random.uniform(100 * factor_prod, 300 * factor_prod),
                unidad='kg',
                origen='pilas_rechazadas',
                valor_estimado=random.uniform(50 * factor_prod, 150 * factor_prod),
                observaciones="Acero recuperado de carcasas"
            )
            db.session.add(reciclaje)
            
            # KOH recuperado (ocasional - cada 3 semanas)
            if i % 21 == 0:
                reciclaje = Reciclaje(
                    fecha=fecha,
                    material_recuperado='KOH',
                    cantidad=random.uniform(50 * factor_prod, 150 * factor_prod),
                    unidad='L',
                    origen='reproceso_interno',
                    valor_estimado=random.uniform(150 * factor_prod, 450 * factor_prod),
                    observaciones="KOH recuperado y purificado para reutilización"
                )
                db.session.add(reciclaje)
        
        db.session.commit()
        print(f"    ✓ {db.session.query(Reciclaje).count()} registros de reciclaje insertados")
        
        print("\n✅ ¡Datos ficticios insertados exitosamente!")
        print(f"\nResumen:")
        print(f"  - Producción: {db.session.query(Produccion).count()} registros")
        print(f"  - Consumos: {db.session.query(ConsumoRecursos).count()} registros")
        print(f"  - Residuos: {db.session.query(GestionResiduos).count()} registros")
        print(f"  - Reciclaje: {db.session.query(Reciclaje).count()} registros")

if __name__ == '__main__':
    insertar_datos_ejemplo()

