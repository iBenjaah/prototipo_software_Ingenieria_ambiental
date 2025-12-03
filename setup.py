"""
Script de configuración para empaquetado
"""

from setuptools import setup, find_packages

setup(
    name="SistemaGestionAmbiental",
    version="1.0.0",
    description="Sistema Informático de Gestión Ambiental para Baterías Zinc-Aire",
    author="Equipo 2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.0.0',
        'Flask-SQLAlchemy==3.1.1',
        'Werkzeug==3.0.1',
    ],
    python_requires='>=3.8',
)

