from typing import Any, Dict

FILTRO_CONTINENTE = ['Todos', 'America del Sur', 'America del Norte',
                     'Europa', 'Asia', 'Africa', 'Oceania']


def filtrar_paises(
    user_input: str,
    filters_obj: Dict[str, Any],
    filter_selector: tuple[int, int]
) -> tuple[Dict[str, Any], tuple[int, int]]:
    """
    Maneja la navegación y aplicación de filtros para países.
    
    Args:
        user_input: Input del usuario
        filters_obj: Objeto con filtros actuales
        filter_selector: Posición actual del selector (fila, columna)
        
    Returns:
        Tupla con filtros actualizados y posición del selector
    """
    match user_input:
        case 'KEY_UP':
            filter_selector = (
                max(0, filter_selector[0] - 1),
                filter_selector[1]
            )
        case 'KEY_DOWN':
            filter_selector = (
                min(8, filter_selector[0] + 1),
                filter_selector[1]
            )
        case 'KEY_LEFT':
            if filter_selector[0] == 0:
                filter_selector = (
                    filter_selector[0],
                    max(0, filter_selector[1] - 1)
                )
        case 'KEY_RIGHT':
            if filter_selector[0] == 0:
                filter_selector = (
                    filter_selector[0],
                    min(len(FILTRO_CONTINENTE) - 1, filter_selector[1] + 1)
                )

    # Aplicar filtros según la selección
    match filter_selector[0]:
        case 0:
            filters_obj['continente'] = FILTRO_CONTINENTE[filter_selector[1]]
        case 1:
            if user_input.isdigit():
                filters_obj['rango_poblacion'] = (
                    filters_obj['rango_poblacion'][0] + user_input,
                    filters_obj['rango_poblacion'][1]
                )

            if user_input == "KEY_BACKSPACE":
                filters_obj['rango_poblacion'] = (
                    filters_obj['rango_poblacion'][0][:-1],
                    filters_obj['rango_poblacion'][1]
                )
        case 2:
            if user_input.isdigit():
                filters_obj['rango_poblacion'] = (
                    filters_obj['rango_poblacion'][0],
                    filters_obj['rango_poblacion'][1] + user_input
                )

            if user_input == "KEY_BACKSPACE":
                filters_obj['rango_poblacion'] = (
                    filters_obj['rango_poblacion'][0],
                    filters_obj['rango_poblacion'][1][:-1]
                )
        case 3:
            if user_input == '\n':
                filters_obj['poblacion_orden'] = 'desc' if filters_obj['poblacion_orden'] != 'desc' else None
                filters_obj['superficie_orden'] = None
        case 4:
            if user_input == '\n':
                filters_obj['poblacion_orden'] = 'asc' if filters_obj['poblacion_orden'] != 'asc' else None
                filters_obj['superficie_orden'] = None
        case 5:
            if user_input.isdigit():
                filters_obj['rango_superficie'] = (
                    filters_obj['rango_superficie'][0] + user_input,
                    filters_obj['rango_superficie'][1]
                )

            if user_input == "KEY_BACKSPACE":
                filters_obj['rango_superficie'] = (
                    filters_obj['rango_superficie'][0][:-1],
                    filters_obj['rango_superficie'][1]
                )
        case 6:
            if user_input.isdigit():
                filters_obj['rango_superficie'] = (
                    filters_obj['rango_superficie'][0],
                    filters_obj['rango_superficie'][1] + user_input
                )

            if user_input == "KEY_BACKSPACE":
                filters_obj['rango_superficie'] = (
                    filters_obj['rango_superficie'][0],
                    filters_obj['rango_superficie'][1][:-1]
                )
        case 7:
            if user_input == '\n':
                filters_obj['superficie_orden'] = 'desc' if filters_obj['superficie_orden'] != 'desc' else None
                filters_obj['poblacion_orden'] = None
        case 8:
            if user_input == '\n':
                filters_obj['superficie_orden'] = 'asc' if filters_obj['superficie_orden'] != 'asc' else None
                filters_obj['poblacion_orden'] = None

        case _:
            pass

    return filters_obj, filter_selector
