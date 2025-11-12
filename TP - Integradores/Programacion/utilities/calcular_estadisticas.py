from typing import Any, Dict, List
from .sorting_functions import key_value_for_sorting_poblacion, key_value_for_sorting_superficie

FILTRO_CONTINENTE = ['Todos', 'America del Sur', 'America del Norte',
                     'Europa', 'Asia', 'Africa', 'Oceania']


def calcular_estadisticas(
    paises: List[Dict[str, str]] | tuple[bool, str]
) -> Dict[str, Any] | bool:
    """
    Calcula estadísticas de una lista de países.
    
    Args:
        paises: Lista de diccionarios con datos de países o tupla (False, mensaje_error)
        
    Returns:
        Diccionario con estadísticas calculadas o False si hay error
    """
    match paises:

        case (False, _):
            return False

        case list():
            total_paises = len(paises)

            if total_paises == 0:
                return {
                    'total_paises': 0,
                    'promedio_poblacion': 0,
                    'promedio_superficie': 0
                }

            suma_poblacion = sum(int(pais['poblacion']) for pais in paises)
            suma_superficie = sum(int(pais['superficie']) for pais in paises)

            promedio_poblacion = suma_poblacion / total_paises
            promedio_superficie = suma_superficie / total_paises

            estadisticas = {
                'total': {
                    'cant_paises': total_paises,
                    'prom_poblacion': promedio_poblacion,
                    'prom_superficie': promedio_superficie
                }
            }

            for continente in FILTRO_CONTINENTE:
                if continente == 'Todos':
                    continue

                cant_de_paises = sum(
                    1 for pais in paises if pais['continente'] == continente)

                estadisticas[continente.lower().replace(' ', '_')] = {
                    'cant_paises': cant_de_paises,
                    'prom_poblacion': sum(
                        int(pais['poblacion']) for pais in paises if pais['continente'] == continente) / cant_de_paises if cant_de_paises > 0 else 0,
                    'prom_superficie': sum(
                        int(pais['superficie']) for pais in paises if pais['continente'] == continente) / cant_de_paises if cant_de_paises > 0 else 0
                }

            estadisticas['pais_mayor_poblacion'] = sorted(
                paises, key=key_value_for_sorting_poblacion)[-1]
            estadisticas['pais_menor_poblacion'] = sorted(
                paises, key=key_value_for_sorting_poblacion)[0]
            estadisticas['pais_mayor_superficie'] = sorted(
                paises, key=key_value_for_sorting_superficie)[-1]
            estadisticas['pais_menor_superficie'] = sorted(
                paises, key=key_value_for_sorting_superficie)[0]

            return estadisticas

        case _:
            return {
                'total_paises': 0,
                'promedio_poblacion': 0,
                'promedio_superficie': 0
            }
