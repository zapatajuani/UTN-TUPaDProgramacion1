HEADER_HEIGHT = 3
FOOTER_HEIGHT = 4
MAIN_MENU_HEIGHT_CORRECTION = 4


def lineas_disponibles(height: int) -> int:
    """
    Calcula las líneas disponibles en la pantalla para mostrar contenido.
    
    Args:
        height: Altura total de la pantalla
        
    Returns:
        Número de líneas disponibles para contenido
    """
    return height - (HEADER_HEIGHT + FOOTER_HEIGHT) - MAIN_MENU_HEIGHT_CORRECTION
