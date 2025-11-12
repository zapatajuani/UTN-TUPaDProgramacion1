def buscar_pais(
    screen: str,
    search_query: str,
    user_input: str
) -> tuple[str, str]:
    """
    Maneja la funcionalidad de búsqueda de países.
    
    Args:
        screen: Pantalla actual
        search_query: Query de búsqueda actual
        user_input: Input del usuario
        
    Returns:
        Tupla con pantalla y query de búsqueda actualizada
    """
    if user_input.isalpha():
        search_query += user_input

    elif user_input == "KEY_BACKSPACE" and search_query:
        search_query = search_query[:-1]

    elif user_input == '\n' and search_query:
        # Aquí se procesaría la búsqueda
        screen = 'main'

    return screen, search_query
