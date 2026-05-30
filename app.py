import flet as ft
from services.logger import get_logger
from styles.colors import AppColors
from styles.theme import AppTheme
from styles.responsive import Responsive
from components.appbar import ModernAppBar
from components.navbar import AppNavBar, AppDrawer
from components.dialogs import show_alert
from views.login_view import create_login_view
from views.dashboard_view import create_dashboard_view
from views.tareas_view import create_tareas_view
from views.asistencia_view import create_asistencia_view
from views.puntualidad_view import create_puntualidad_view
from views.eventos_view import create_eventos_view
from views.progreso_view import create_progreso_view
from views.notificaciones_view import create_notificaciones_view
from views.registro_hijo_view import create_registro_hijo_view

logger = get_logger("app")


VIEWS = ["dashboard", "tareas", "asistencia", "puntualidad", "eventos", "progreso", "notificaciones"]
VIEW_TITLES = {
    "dashboard": "Inicio",
    "tareas": "Tareas",
    "asistencia": "Asistencia",
    "puntualidad": "Puntualidad",
    "eventos": "Eventos",
    "progreso": "Progreso",
    "notificaciones": "Notificaciones",
}


class AppPadre:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_view = "dashboard"
        self._authenticated = False
        self.user_data = None
        self._hijos: list = []
        self._selected_child: dict | None = None
        logger.info("Inicializando AppPadre (page=%s)", id(page))
        self._setup_page()
        self._show_login()

    def _setup_page(self):
        self.page.title = "App Padre - Seguimiento Escolar"
        self.page.theme = AppTheme.light_theme()
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor = AppColors.GRIS_CLARO
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window.min_width = 320
        self.page.window.min_height = 480
        self.page.on_resize = self._on_resize
        logger.debug("Página configurada: theme=light, min=%sx%s", 320, 480)

    def _on_resize(self, e):
        if self._authenticated:
            self._update_view()

    def _show_login(self):
        logger.info("Mostrando pantalla de login")
        self.page.views.clear()
        login_view = create_login_view(self.page, self._on_login_success)
        self.page.views.append(login_view)
        self.page.update()

    def _on_login_success(self, user_data: dict):
        self._authenticated = True
        self.user_data = user_data
        self._hijos = []
        self._selected_child = None
        logger.info("Login exitoso: id_usuario=%s rol=%s nombre=%s",
                     user_data.get("id_usuario"),
                     user_data.get("rol"),
                     user_data.get("nombre"))
        self._setup_main_ui()

    def _setup_main_ui(self):
        self.nav_bar = AppNavBar(on_change=self._on_nav_change)
        self.drawer = AppDrawer(self.page, self._on_drawer_change)

        self._update_view()

    def _on_hijos_loaded(self, hijos: list):
        self._hijos = hijos
        if hijos and self._selected_child is None:
            self._selected_child = hijos[0]
            logger.info("Hijos cargados: %s, seleccionado: %s",
                         len(hijos), self._selected_child.get("nombre_completo"))
        elif not hijos:
            self._selected_child = None

    def select_child(self, index: int):
        if 0 <= index < len(self._hijos):
            self._selected_child = self._hijos[index]
            logger.info("Hijo seleccionado: %s", self._selected_child.get("nombre_completo"))
            self._update_view()

    def _go_to_registro_hijo(self):
        logger.debug("Navegando a registro de hijo")
        self.current_view = "registro_hijo"
        self._update_view()

    def _on_registro_exitoso(self):
        logger.info("Registro exitoso, volviendo al dashboard")
        self.current_view = "dashboard"
        self._hijos = []
        self._selected_child = None
        self._update_view()

    def _on_registro_cancelado(self):
        logger.debug("Registro cancelado, volviendo al dashboard")
        self.current_view = "dashboard"
        self._update_view()

    def _get_view_content(self, view_name: str):
        creators = {
            "dashboard": create_dashboard_view,
            "tareas": create_tareas_view,
            "asistencia": create_asistencia_view,
            "puntualidad": create_puntualidad_view,
            "eventos": create_eventos_view,
            "progreso": create_progreso_view,
            "notificaciones": create_notificaciones_view,
            "registro_hijo": create_registro_hijo_view,
        }
        if view_name == "registro_hijo":
            id_padre = (self.user_data or {}).get("id_usuario", "")
            return create_registro_hijo_view(
                self.page,
                id_padre,
                on_success=self._on_registro_exitoso,
                on_cancel=self._on_registro_cancelado,
            )
        creator = creators.get(view_name)
        if view_name == "dashboard":
            return creator(
                self.page,
                self.user_data or {},
                self._on_nav_change,
                selected_child=self._selected_child,
                on_hijos_loaded=self._on_hijos_loaded,
                on_child_selected=self.select_child,
                on_nuevo_hijo=self._go_to_registro_hijo,
            )
        if view_name == "tareas":
            return creator(self.page, selected_child=self._selected_child)
        return creator(self.page)

    def _build_main_view(self):
        title = VIEW_TITLES.get(self.current_view, "App Padre")
        content = self._get_view_content(self.current_view)

        if self.current_view == "registro_hijo":
            appbar = ft.AppBar(
                title=ft.Text("Registrar Hijo", size=18, weight=ft.FontWeight.BOLD, color=AppColors.GRIS_OSCURO),
                bgcolor=AppColors.BLANCO,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=AppColors.AZUL_EDUCATIVO,
                    on_click=lambda e: self._on_registro_cancelado(),
                ),
                center_title=False,
                elevation=0,
            )
            return ft.View(
                route="/registro_hijo",
                controls=[content],
                appbar=appbar,
                bgcolor=AppColors.GRIS_CLARO,
                padding=0,
                scroll=ft.ScrollMode.AUTO,
            )

        appbar = ModernAppBar(self.page, title=title)

        return ft.View(
            route=f"/{self.current_view}",
            controls=[content],
            appbar=appbar,
            bgcolor=AppColors.GRIS_CLARO,
            padding=0,
            scroll=ft.ScrollMode.AUTO,
            navigation_bar=self.nav_bar,
            drawer=getattr(self, 'drawer', None),
        )

    def _update_view(self):
        self.page.views.clear()
        main_view = self._build_main_view()
        self.page.views.append(main_view)
        self.page.update()

    def _on_nav_change(self, e):
        if isinstance(e, int):
            index = e
        elif hasattr(e, "control"):
            index = e.control.selected_index
        else:
            index = e.selected_index if hasattr(e, "selected_index") else 0

        if 0 <= index < len(VIEWS):
            self.current_view = VIEWS[index]
            self.nav_bar.selected_index = index
            logger.info("Navegación (navbar): %s (index=%s)", self.current_view, index)
            self._update_view()

    async def _on_drawer_change(self, e):
        if hasattr(e, "control") and hasattr(e.control, "selected_index"):
            index = e.control.selected_index
        else:
            index = e.selected_index if hasattr(e, "selected_index") else 0

        await self.page.close_drawer()

        drawer_destinations = ["dashboard", "tareas", "asistencia", "puntualidad", "eventos", "progreso", "notificaciones", "logout"]

        if index < len(drawer_destinations):
            dest = drawer_destinations[index]
            if dest == "logout":
                logger.info("Navegación (drawer): logout solicitado")
                self._handle_logout()
            else:
                self.current_view = dest
                nav_index = VIEWS.index(dest) if dest in VIEWS else 0
                self.nav_bar.selected_index = nav_index
                logger.info("Navegación (drawer): %s (index=%s)", self.current_view, index)
                self._update_view()
        self.page.update()

    def _handle_logout(self):
        logger.info("Cerrando sesión: user_data limpiado, redirigiendo a login")
        self._authenticated = False
        self.user_data = None
        self._hijos = []
        self._selected_child = None
        self._show_login()
