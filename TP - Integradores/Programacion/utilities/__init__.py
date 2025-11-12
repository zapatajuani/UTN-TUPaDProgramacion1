"""
Utilidades para el sistema de gestión de países.

Este módulo contiene funciones utilitarias organizadas en archivos separados:
- calcular_estadisticas: Funciones para cálculo de estadísticas
- reset_esquema_and_values: Funciones para resetear formularios
- editar_registrar_pais: Funciones para edición y registro de países
- proceso_carga_datos: Funciones para carga y filtrado de datos
- buscar_pais: Funciones para búsqueda de países
- lineas_disponibles: Funciones para cálculos de interfaz
- paginas: Funciones para paginación
- filtrar_paises: Funciones para filtrado interactivo
- sorting_functions: Funciones de ordenamiento
"""

from .calcular_estadisticas import calcular_estadisticas
from .reset_esquema_and_values import reset_esquema_and_values
from .editar_registrar_pais import editar_registrar_pais
from .proceso_carga_datos import proceso_carga_datos
from .buscar_pais import buscar_pais
from .lineas_disponibles import lineas_disponibles
from .paginas import paginas
from .filtrar_paises import filtrar_paises
from .sorting_functions import (
    key_value_for_sorting_poblacion,
    key_value_for_sorting_superficie
)

__all__ = [
    'calcular_estadisticas',
    'reset_esquema_and_values',
    'editar_registrar_pais',
    'proceso_carga_datos',
    'buscar_pais',
    'lineas_disponibles',
    'paginas',
    'filtrar_paises',
    'key_value_for_sorting_poblacion',
    'key_value_for_sorting_superficie'
]
