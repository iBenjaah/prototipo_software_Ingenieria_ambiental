"""
Sistema Informático de Gestión Ambiental
Para el seguimiento de variables críticas en la producción y ciclo de vida
de baterías zinc-aire tipo botón
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, timedelta
from sqlalchemy import func, and_
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sistema-gestion-ambiental-zinc-aire-2025'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestion_ambiental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos de base de datos
class Produccion(db.Model):
    """Registro de producción de baterías"""
    __tablename__ = 'produccion'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    cantidad_producida = db.Column(db.Integer, nullable=False)
    cantidad_rechazada = db.Column(db.Integer, default=0)
    lote = db.Column(db.String(50))
    observaciones = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

class ConsumoRecursos(db.Model):
    """Registro de consumos de recursos (agua, energía, materiales)"""
    __tablename__ = 'consumo_recursos'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    tipo_recurso = db.Column(db.String(50), nullable=False)  # agua, energia, zinc, KOH, etc.
    cantidad = db.Column(db.Float, nullable=False)
    unidad = db.Column(db.String(20), nullable=False)  # L, kWh, kg, etc.
    costo = db.Column(db.Float)
    observaciones = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

class GestionResiduos(db.Model):
    """Registro de generación y gestión de residuos"""
    __tablename__ = 'gestion_residuos'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    tipo_residuo = db.Column(db.String(50), nullable=False)  # pilas_usadas, pilas_rechazadas, efluentes, etc.
    cantidad = db.Column(db.Float, nullable=False)
    unidad = db.Column(db.String(20), nullable=False)
    destino = db.Column(db.String(100))  # reciclaje, disposicion_final, reproceso
    gestor = db.Column(db.String(100))  # empresa gestora
    observaciones = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

class Reciclaje(db.Model):
    """Registro de materiales recuperados mediante reciclaje"""
    __tablename__ = 'reciclaje'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    material_recuperado = db.Column(db.String(50), nullable=False)  # zinc, acero, KOH, etc.
    cantidad = db.Column(db.Float, nullable=False)
    unidad = db.Column(db.String(20), nullable=False)
    origen = db.Column(db.String(100))  # pilas_usadas, pilas_rechazadas, etc.
    valor_estimado = db.Column(db.Float)
    observaciones = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

class IndicadorAmbiental(db.Model):
    """Registro histórico de indicadores ambientales calculados"""
    __tablename__ = 'indicadores_ambientales'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    indicador = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    unidad = db.Column(db.String(20))
    meta = db.Column(db.Float)  # meta u objetivo
    observaciones = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

# Rutas principales
@app.route('/')
def index():
    """Dashboard principal"""
    # Calcular indicadores actuales
    indicadores = calcular_indicadores_actuales()
    
    # Obtener datos recientes
    produccion_reciente = Produccion.query.order_by(Produccion.fecha.desc()).limit(5).all()
    consumos_recientes = ConsumoRecursos.query.order_by(ConsumoRecursos.fecha.desc()).limit(5).all()
    residuos_recientes = GestionResiduos.query.order_by(GestionResiduos.fecha.desc()).limit(5).all()
    
    return render_template('dashboard.html',
                         indicadores=indicadores,
                         produccion_reciente=produccion_reciente,
                         consumos_recientes=consumos_recientes,
                         residuos_recientes=residuos_recientes)

@app.route('/produccion', methods=['GET', 'POST'])
def produccion():
    """Gestión de producción"""
    if request.method == 'POST':
        try:
            prod = Produccion(
                fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d').date(),
                cantidad_producida=int(request.form['cantidad_producida']),
                cantidad_rechazada=int(request.form.get('cantidad_rechazada', 0)),
                lote=request.form.get('lote', ''),
                observaciones=request.form.get('observaciones', '')
            )
            db.session.add(prod)
            db.session.commit()
            flash('Registro de producción guardado exitosamente', 'success')
            return redirect(url_for('produccion'))
        except Exception as e:
            flash(f'Error al guardar: {str(e)}', 'error')
            db.session.rollback()
    
    # Obtener registros
    registros = Produccion.query.order_by(Produccion.fecha.desc()).all()
    return render_template('produccion.html', registros=registros)

@app.route('/consumos', methods=['GET', 'POST'])
def consumos():
    """Gestión de consumos de recursos"""
    if request.method == 'POST':
        try:
            consumo = ConsumoRecursos(
                fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d').date(),
                tipo_recurso=request.form['tipo_recurso'],
                cantidad=float(request.form['cantidad']),
                unidad=request.form['unidad'],
                costo=float(request.form.get('costo', 0)) if request.form.get('costo') else None,
                observaciones=request.form.get('observaciones', '')
            )
            db.session.add(consumo)
            db.session.commit()
            flash('Registro de consumo guardado exitosamente', 'success')
            return redirect(url_for('consumos'))
        except Exception as e:
            flash(f'Error al guardar: {str(e)}', 'error')
            db.session.rollback()
    
    registros = ConsumoRecursos.query.order_by(ConsumoRecursos.fecha.desc()).all()
    tipos_recursos = db.session.query(ConsumoRecursos.tipo_recurso).distinct().all()
    return render_template('consumos.html', registros=registros, tipos_recursos=tipos_recursos)

@app.route('/residuos', methods=['GET', 'POST'])
def residuos():
    """Gestión de residuos"""
    if request.method == 'POST':
        try:
            residuo = GestionResiduos(
                fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d').date(),
                tipo_residuo=request.form['tipo_residuo'],
                cantidad=float(request.form['cantidad']),
                unidad=request.form['unidad'],
                destino=request.form.get('destino', ''),
                gestor=request.form.get('gestor', ''),
                observaciones=request.form.get('observaciones', '')
            )
            db.session.add(residuo)
            db.session.commit()
            flash('Registro de residuo guardado exitosamente', 'success')
            return redirect(url_for('residuos'))
        except Exception as e:
            flash(f'Error al guardar: {str(e)}', 'error')
            db.session.rollback()
    
    registros = GestionResiduos.query.order_by(GestionResiduos.fecha.desc()).all()
    tipos_residuos = db.session.query(GestionResiduos.tipo_residuo).distinct().all()
    return render_template('residuos.html', registros=registros, tipos_residuos=tipos_residuos)

@app.route('/reciclaje', methods=['GET', 'POST'])
def reciclaje():
    """Gestión de reciclaje y recuperación de materiales"""
    if request.method == 'POST':
        try:
            rec = Reciclaje(
                fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d').date(),
                material_recuperado=request.form['material_recuperado'],
                cantidad=float(request.form['cantidad']),
                unidad=request.form['unidad'],
                origen=request.form.get('origen', ''),
                valor_estimado=float(request.form.get('valor_estimado', 0)) if request.form.get('valor_estimado') else None,
                observaciones=request.form.get('observaciones', '')
            )
            db.session.add(rec)
            db.session.commit()
            flash('Registro de reciclaje guardado exitosamente', 'success')
            return redirect(url_for('reciclaje'))
        except Exception as e:
            flash(f'Error al guardar: {str(e)}', 'error')
            db.session.rollback()
    
    registros = Reciclaje.query.order_by(Reciclaje.fecha.desc()).all()
    materiales = db.session.query(Reciclaje.material_recuperado).distinct().all()
    return render_template('reciclaje.html', registros=registros, materiales=materiales)

@app.route('/indicadores')
def indicadores():
    """Visualización de indicadores ambientales"""
    indicadores_actuales = calcular_indicadores_actuales()
    indicadores_historicos = IndicadorAmbiental.query.order_by(IndicadorAmbiental.fecha.desc()).limit(50).all()
    return render_template('indicadores.html', 
                         indicadores=indicadores_actuales,
                         historicos=indicadores_historicos)

@app.route('/reportes')
def reportes():
    """Generación de reportes"""
    fecha_inicio = request.args.get('fecha_inicio', (date.today().replace(day=1)).isoformat())
    fecha_fin = request.args.get('fecha_fin', date.today().isoformat())
    
    # Obtener datos del período
    produccion_periodo = Produccion.query.filter(
        and_(Produccion.fecha >= fecha_inicio, Produccion.fecha <= fecha_fin)
    ).all()
    
    consumos_periodo = ConsumoRecursos.query.filter(
        and_(ConsumoRecursos.fecha >= fecha_inicio, ConsumoRecursos.fecha <= fecha_fin)
    ).all()
    
    residuos_periodo = GestionResiduos.query.filter(
        and_(GestionResiduos.fecha >= fecha_inicio, GestionResiduos.fecha <= fecha_fin)
    ).all()
    
    reciclaje_periodo = Reciclaje.query.filter(
        and_(Reciclaje.fecha >= fecha_inicio, Reciclaje.fecha <= fecha_fin)
    ).all()
    
    # Calcular resúmenes
    total_producido = sum(p.cantidad_producida for p in produccion_periodo)
    total_rechazado = sum(p.cantidad_rechazada for p in produccion_periodo)
    
    return render_template('reportes.html',
                         fecha_inicio=fecha_inicio,
                         fecha_fin=fecha_fin,
                         produccion_periodo=produccion_periodo,
                         consumos_periodo=consumos_periodo,
                         residuos_periodo=residuos_periodo,
                         reciclaje_periodo=reciclaje_periodo,
                         total_producido=total_producido,
                         total_rechazado=total_rechazado)

@app.route('/escenarios')
def escenarios():
    """Evaluación de escenarios de mejora"""
    return render_template('escenarios.html')

# Funciones auxiliares
def calcular_indicadores_actuales():
    """Calcula los indicadores ambientales actuales"""
    indicadores = {}
    
    # Obtener datos de los últimos 30 días
    fecha_fin = date.today()
    fecha_inicio = fecha_fin - timedelta(days=30)
    
    # Producción total del mes
    produccion_mes = Produccion.query.filter(
        and_(Produccion.fecha >= fecha_inicio, Produccion.fecha <= fecha_fin)
    ).all()
    
    total_producido = sum(p.cantidad_producida for p in produccion_mes)
    total_rechazado = sum(p.cantidad_rechazada for p in produccion_mes)
    
    if total_producido > 0:
        indicadores['tasa_rechazo'] = {
            'valor': (total_rechazado / total_producido) * 100,
            'unidad': '%',
            'descripcion': 'Tasa de rechazo de producción'
        }
    
    # Consumos del mes
    consumos_mes = ConsumoRecursos.query.filter(
        and_(ConsumoRecursos.fecha >= fecha_inicio, ConsumoRecursos.fecha <= fecha_fin)
    ).all()
    
    consumo_agua = sum(c.cantidad for c in consumos_mes if c.tipo_recurso == 'agua')
    consumo_energia = sum(c.cantidad for c in consumos_mes if c.tipo_recurso == 'energia')
    consumo_zinc = sum(c.cantidad for c in consumos_mes if c.tipo_recurso == 'zinc')
    consumo_koh = sum(c.cantidad for c in consumos_mes if c.tipo_recurso == 'KOH')
    
    if total_producido > 0:
        indicadores['consumo_agua_unidad'] = {
            'valor': consumo_agua / total_producido,
            'unidad': 'L/unidad',
            'descripcion': 'Consumo de agua por unidad producida'
        }
        indicadores['consumo_energia_unidad'] = {
            'valor': consumo_energia / total_producido,
            'unidad': 'kWh/unidad',
            'descripcion': 'Consumo de energía por unidad producida'
        }
        indicadores['consumo_zinc_unidad'] = {
            'valor': consumo_zinc / total_producido,
            'unidad': 'kg/unidad',
            'descripcion': 'Consumo de zinc por unidad producida'
        }
    
    # Residuos del mes
    residuos_mes = GestionResiduos.query.filter(
        and_(GestionResiduos.fecha >= fecha_inicio, GestionResiduos.fecha <= fecha_fin)
    ).all()
    
    pilas_usadas = sum(r.cantidad for r in residuos_mes if r.tipo_residuo == 'pilas_usadas')
    pilas_rechazadas = sum(r.cantidad for r in residuos_mes if r.tipo_residuo == 'pilas_rechazadas')
    efluentes = sum(r.cantidad for r in residuos_mes if r.tipo_residuo == 'efluentes_alcalinos')
    
    if total_producido > 0:
        indicadores['residuos_unidad'] = {
            'valor': (pilas_usadas + pilas_rechazadas) / total_producido,
            'unidad': 'unidades/unidad producida',
            'descripcion': 'Residuos generados por unidad producida'
        }
    
    # Reciclaje del mes
    reciclaje_mes = Reciclaje.query.filter(
        and_(Reciclaje.fecha >= fecha_inicio, Reciclaje.fecha <= fecha_fin)
    ).all()
    
    zinc_recuperado = sum(r.cantidad for r in reciclaje_mes if r.material_recuperado == 'zinc')
    acero_recuperado = sum(r.cantidad for r in reciclaje_mes if r.material_recuperado == 'acero')
    
    if consumo_zinc > 0:
        indicadores['tasa_recuperacion_zinc'] = {
            'valor': (zinc_recuperado / consumo_zinc) * 100,
            'unidad': '%',
            'descripcion': 'Tasa de recuperación de zinc'
        }
    
    # Tasa de reciclaje
    total_residuos = pilas_usadas + pilas_rechazadas
    if total_residuos > 0:
        indicadores['tasa_reciclaje'] = {
            'valor': ((zinc_recuperado + acero_recuperado) / total_residuos) * 100 if total_residuos > 0 else 0,
            'unidad': '%',
            'descripcion': 'Tasa de reciclaje general'
        }
    
    return indicadores

# API endpoints para gráficos
@app.route('/api/consumos_mensuales')
def api_consumos_mensuales():
    """API para obtener consumos mensuales"""
    meses = []
    agua = []
    energia = []
    zinc = []
    
    # Últimos 12 meses
    for i in range(11, -1, -1):
        fecha = date.today().replace(day=1)
        for _ in range(i):
            if fecha.month == 1:
                fecha = fecha.replace(year=fecha.year - 1, month=12)
            else:
                fecha = fecha.replace(month=fecha.month - 1)
        
        fecha_fin = fecha
        if fecha.month == 12:
            fecha_inicio = fecha.replace(year=fecha.year + 1, month=1, day=1)
        else:
            fecha_inicio = fecha.replace(month=fecha.month + 1, day=1)
        
        consumos = ConsumoRecursos.query.filter(
            and_(ConsumoRecursos.fecha >= fecha, ConsumoRecursos.fecha < fecha_inicio)
        ).all()
        
        meses.append(fecha.strftime('%Y-%m'))
        agua.append(sum(c.cantidad for c in consumos if c.tipo_recurso == 'agua'))
        energia.append(sum(c.cantidad for c in consumos if c.tipo_recurso == 'energia'))
        zinc.append(sum(c.cantidad for c in consumos if c.tipo_recurso == 'zinc'))
    
    return jsonify({
        'meses': meses,
        'agua': agua,
        'energia': energia,
        'zinc': zinc
    })

@app.route('/api/produccion_mensual')
def api_produccion_mensual():
    """API para obtener producción mensual"""
    meses = []
    produccion = []
    rechazos = []
    
    for i in range(11, -1, -1):
        fecha = date.today().replace(day=1)
        for _ in range(i):
            if fecha.month == 1:
                fecha = fecha.replace(year=fecha.year - 1, month=12)
            else:
                fecha = fecha.replace(month=fecha.month - 1)
        
        if fecha.month == 12:
            fecha_inicio = fecha.replace(year=fecha.year + 1, month=1, day=1)
        else:
            fecha_inicio = fecha.replace(month=fecha.month + 1, day=1)
        
        prod = Produccion.query.filter(
            and_(Produccion.fecha >= fecha, Produccion.fecha < fecha_inicio)
        ).all()
        
        meses.append(fecha.strftime('%Y-%m'))
        produccion.append(sum(p.cantidad_producida for p in prod))
        rechazos.append(sum(p.cantidad_rechazada for p in prod))
    
    return jsonify({
        'meses': meses,
        'produccion': produccion,
        'rechazos': rechazos
    })

@app.route('/api/produccion_vs_reciclaje')
def api_produccion_vs_reciclaje():
    """API para obtener producción vs reciclaje mensual (pilas producidas vs pilas recicladas)"""
    meses = []
    produccion_total = []
    reciclaje_total = []
    
    for i in range(11, -1, -1):
        fecha = date.today().replace(day=1)
        for _ in range(i):
            if fecha.month == 1:
                fecha = fecha.replace(year=fecha.year - 1, month=12)
            else:
                fecha = fecha.replace(month=fecha.month - 1)
        
        if fecha.month == 12:
            fecha_inicio = fecha.replace(year=fecha.year + 1, month=1, day=1)
        else:
            fecha_inicio = fecha.replace(month=fecha.month + 1, day=1)
        
        # Producción del mes (pilas producidas)
        prod = Produccion.query.filter(
            and_(Produccion.fecha >= fecha, Produccion.fecha < fecha_inicio)
        ).all()
        total_producido = sum(p.cantidad_producida for p in prod)
        
        # Residuos reciclados del mes (pilas usadas y rechazadas que fueron a reciclaje)
        residuos_reciclados = GestionResiduos.query.filter(
            and_(
                GestionResiduos.fecha >= fecha,
                GestionResiduos.fecha < fecha_inicio,
                GestionResiduos.destino == 'reciclaje',
                GestionResiduos.unidad == 'unidades'
            )
        ).all()
        # Sumar pilas recicladas
        pilas_recicladas = sum(int(r.cantidad) for r in residuos_reciclados)
        
        meses.append(fecha.strftime('%Y-%m'))
        produccion_total.append(total_producido)
        reciclaje_total.append(pilas_recicladas)
    
    return jsonify({
        'meses': meses,
        'produccion': produccion_total,
        'reciclaje': reciclaje_total
    })

# Inicializar base de datos
def init_db():
    """Inicializa la base de datos"""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()
    
    # Abrir navegador automáticamente
    import webbrowser
    import threading
    import time
    
    def open_browser():
        """Abre el navegador después de un breve delay"""
        time.sleep(1.5)  # Esperar a que el servidor inicie
        webbrowser.open('http://127.0.0.1:5000')
    
    # Iniciar el navegador en un thread separado
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Ejecutar servidor (sin debug en producción)
    app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)

