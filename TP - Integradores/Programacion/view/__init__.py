"""
Módulos de vista para el sistema de gestión de países.

Este paquete contiene todas las funciones relacionadas con la interfaz de usuario
y la presentación visual usando la librería curses:

Componentes de interfaz:
- main_header: Encabezado principal de la aplicación
- main_footer: Pie de página con controles
- main_menu: Menú principal con lista de países
- search_menu: Interfaz de búsqueda
- add_menu: Formulario para agregar países
- update_menu: Formulario para actualizar países
- filters_menu: Interfaz de filtros interactiva
- menu_estadisticas: Reporte de estadísticas

Layouts completos:
- main_layout: Layout principal de la aplicación
- search_layout: Layout de búsqueda
- add_layout: Layout para agregar países
- update_layout: Layout para actualizar países
"""

from .main_header import main_header
from .main_footer import main_footer
from .main_menu import main_menu
from .search_menu import search_menu
from .add_menu import add_menu
from .update_menu import update_menu
from .filters_menu import filters_menu
from .menu_estadisticas import menu_estadisticas
from .main_layout import main_layout
from .search_layout import search_layout
from .add_layout import add_layout
from .update_layout import update_layout

__all__ = [
    # Componentes de interfaz
    'main_header',
    'main_footer', 
    'main_menu',
    'search_menu',
    'add_menu',
    'update_menu',
    'filters_menu',
    'menu_estadisticas',
    # Layouts completos
    'main_layout',
    'search_layout',
    'add_layout',
    'update_layout'
]
