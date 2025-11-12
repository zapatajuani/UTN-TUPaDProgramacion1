import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from model.model import cantidad_de_paises


def paginas(lineas_disponibles: int) -> int:
    """
    Calcula el número total de páginas necesarias para mostrar todos los países.
    
    Args:
        lineas_disponibles: Número de líneas disponibles por página
        
    Returns:
        Número total de páginas
    """
    total_paises = cantidad_de_paises('paises.csv')

    total_paginas = total_paises // lineas_disponibles

    if total_paises % lineas_disponibles != 0:
        total_paginas += 1

    return total_paginas
