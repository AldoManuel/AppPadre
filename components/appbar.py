import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive

class ModernAppBar(ft.AppBar):
    def __init__(self, page: ft.Page, title: str = "App Padre", actions: list = None):
        w = page.window.width if page.window else 600

        super().__init__(
            title=ft.Text(
                title,
                size=Responsive.font_size_md(w),
                weight=ft.FontWeight.BOLD,
                color=AppColors.BLANCO,
            ),
            bgcolor=AppColors.AZUL_EDUCATIVO,
            leading=ft.IconButton(
                icon=ft.Icons.MENU,
                icon_color=AppColors.BLANCO,
                icon_size=24,
                on_click=self._toggle_drawer,
            ),
            actions=actions or [
                ft.IconButton(
                    icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                    icon_color=AppColors.BLANCO,
                    icon_size=22,
                ),
                ft.IconButton(
                    icon=ft.Icons.ACCOUNT_CIRCLE_OUTLINED,
                    icon_color=AppColors.BLANCO,
                    icon_size=22,
                ),
            ],
            center_title=False,
            toolbar_height=w > 600 and 64 or 56,
        )

    async def _toggle_drawer(self, e):
        if self.page:
            await self.page.show_drawer()
