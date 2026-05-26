import flet as ft
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

    def _on_resize(self, e):
        if self._authenticated:
            self._update_view()

    def _show_login(self):
        self.page.views.clear()
        login_view = create_login_view(self.page, self._on_login_success)
        self.page.views.append(login_view)
        self.page.update()

    def _on_login_success(self):
        self._authenticated = True
        self._setup_main_ui()

    def _setup_main_ui(self):
        self.nav_bar = AppNavBar(on_change=self._on_nav_change)
        self.drawer = AppDrawer(self.page, self._on_drawer_change)

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
        }
        creator = creators.get(view_name)
        if view_name == "dashboard":
            return creator(self.page, self._on_nav_change)
        return creator(self.page)

    def _build_main_view(self):
        title = VIEW_TITLES.get(self.current_view, "App Padre")
        content = self._get_view_content(self.current_view)

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
                self._handle_logout()
            else:
                self.current_view = dest
                nav_index = VIEWS.index(dest) if dest in VIEWS else 0
                self.nav_bar.selected_index = nav_index
                self._update_view()
        self.page.update()

    def _handle_logout(self):
        self._authenticated = False
        self._show_login()
