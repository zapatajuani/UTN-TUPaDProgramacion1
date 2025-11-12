from typing import Dict

VALORES_ESQUEMA = ['nombre', 'poblacion', 'superficie', 'continente']


def reset_esquema_and_values() -> tuple[Dict[str, str], str, str]:
    """
    Resetea el esquema de datos y valores para formularios.
    
    Returns:
        Tupla con diccionario vacío, string vacío y primer campo del esquema
    """
    return {
        'nombre': '',
        'poblacion': '',
        'superficie': '',
        'continente': ''
    }, "", VALORES_ESQUEMA[0]
