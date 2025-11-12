import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from typing import Any, Dict, List
from model.model import (
    cargar_paises,
    buscar_pais_por_nombre,
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie
)
from .sorting_functions import (
    key_value_for_sorting_poblacion,
    key_value_for_sorting_superficie
)


def proceso_carga_datos(
    nombre: str,
    filters_obj: Dict[str, Any]
) -> List[Dict[str, str]] | tuple[bool, str]:
    """
    Procesa la carga de datos de países aplicando filtros y ordenamiento.
    
    Args:
        nombre: Nombre del país a buscar (opcional)
        filters_obj: Diccionario con filtros a aplicar
        
    Returns:
        Lista de países filtrada o tupla (False, mensaje_error)
    """
    paises = cargar_paises('paises.csv')

    if nombre:
        paises = buscar_pais_por_nombre(nombre, paises)
        if paises[0] is None:
            return False, str(paises[1])

    if filters_obj['continente'] and filters_obj['continente'] != 'Todos':
        paises = filtrar_por_continente(paises, filters_obj['continente'])

    if filters_obj['rango_poblacion'][0] or filters_obj['rango_poblacion'][1]:
        paises = filtrar_por_rango_poblacion(
            paises,
            int(filters_obj['rango_poblacion'][0]
                ) if filters_obj['rango_poblacion'][0] else None,
            int(filters_obj['rango_poblacion'][1]
                ) if filters_obj['rango_poblacion'][1] else None
        )

    if filters_obj['rango_superficie'][0] or filters_obj['rango_superficie'][1]:
        paises = filtrar_por_rango_superficie(
            paises,
            int(filters_obj['rango_superficie'][0]
                ) if filters_obj['rango_superficie'][0] else None,
            int(filters_obj['rango_superficie'][1]
                ) if filters_obj['rango_superficie'][1] else None
        )

    if filters_obj['poblacion_orden']:
        paises.sort(
            key=key_value_for_sorting_poblacion,
            reverse=(filters_obj['poblacion_orden'] == 'desc')
        )

    if filters_obj['superficie_orden']:
        paises.sort(
            key=key_value_for_sorting_superficie,
            reverse=(filters_obj['superficie_orden'] == 'desc')
        )

    return paises
