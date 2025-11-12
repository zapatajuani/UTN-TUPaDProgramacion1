import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from typing import Dict
from model.model import agregar_pais, actualizar_pais as actualizar_pais_model

VALORES_ESQUEMA = ['nombre', 'poblacion', 'superficie', 'continente']


def editar_registrar_pais(
    screen: str,
    user_input: str,
    campo_actual: str,
    esquema: Dict[str, str],
    edicion: bool = False
) -> tuple[str, Dict[str, str], str, str]:
    """
    Maneja la edición y registro de países en formularios.
    
    Args:
        screen: Pantalla actual
        user_input: Input del usuario
        campo_actual: Campo actualmente seleccionado
        esquema: Diccionario con datos del país
        edicion: True si es edición, False si es registro nuevo
        
    Returns:
        Tupla con pantalla, esquema, mensaje de estado y campo actual
    """
    status_msg = ""

    # --- CAMBIO 1: Lógica de entrada de datos por tipo de campo ---
    if len(user_input) == 1 and user_input.isprintable():
        if campo_actual in ['poblacion', 'superficie']:
            if user_input.isdigit():
                esquema[campo_actual] += user_input
            else:
                status_msg = "Error: Este campo solo acepta números."
        elif campo_actual in ['nombre', 'continente']:
            if user_input.isalpha() or user_input.isspace():
                esquema[campo_actual] += user_input
            else:
                status_msg = "Error: Este campo solo acepta letras y espacios."

    elif user_input == "KEY_BACKSPACE":
        if len(esquema[campo_actual]) == 0 and VALORES_ESQUEMA.index(campo_actual) > 0:
            # Si el campo está vacío, ir al campo anterior
            indice_campo = VALORES_ESQUEMA.index(campo_actual)
            campo_actual = VALORES_ESQUEMA[indice_campo - 1]
        else:
            # Borrar el último carácter del campo actual
            esquema[campo_actual] = esquema[campo_actual][:-1]

    # --- CAMBIO 2: Lógica de Navegación (Enter) ---
    # Se quitó 'and esquema[campo_actual]' para permitir navegar.
    elif user_input == '\n':
        indice_campo = VALORES_ESQUEMA.index(campo_actual)

        if indice_campo < len(VALORES_ESQUEMA) - 1:
            # Navegar al siguiente campo
            campo_actual = VALORES_ESQUEMA[indice_campo + 1]
        else:
            # Es el último campo, intentar SUBMIT (enviar)
            # --- VALIDACIÓN (como pide la consigna) ---
            if not all(esquema.values()):  # Revisa si algún valor es ""
                status_msg = "Error: No se permiten campos vacíos."
            else:
                res = agregar_pais(
                    esquema) if not edicion else actualizar_pais_model(esquema)
                if res[0]:
                    # Éxito: limpiar formulario y volver al main
                    esquema = {key: '' for key in VALORES_ESQUEMA}
                    # Resetear al primer campo
                    campo_actual = VALORES_ESQUEMA[0]
                    screen = 'main'
                else:
                    status_msg = f"Error al {'actualizar' if edicion else 'agregar'} país: {res[1]}"

    return screen, esquema, status_msg, campo_actual
