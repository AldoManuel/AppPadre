import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive

class SectionHeader(ft.Container):
    def __init__(self, title: str, action_text: str = None, on_action: callable = None, width: int = None):
        controls = [
            ft.Text(
                title,
                size=16,
                weight=ft.FontWeight.BOLD,
                color=AppColors.GRIS_OSCURO,
            ),
        ]

        if action_text:
            controls.append(
                ft.TextButton(
                    content=action_text,
                    style=ft.ButtonStyle(
                        color=AppColors.AZUL_EDUCATIVO,
                        text_style=ft.TextStyle(size=13, weight=ft.FontWeight.W_500),
                    ),
                    on_click=on_action,
                ),
            )

        super().__init__(
            content=ft.Row(
                controls=controls,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=ft.Padding(left=0, right=0, top=0, bottom=4),
            width=width,
        )


class EmptyState(ft.Container):
    def __init__(self, icon: ft.Icons, title: str, subtitle: str = "", width: int = None):
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Container(height=40),
                    ft.Icon(icon, size=56, color=AppColors.GRIS_MEDIO),
                    ft.Container(height=10),
                    ft.Text(
                        title,
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=AppColors.GRIS_TEXTO,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        subtitle,
                        size=13,
                        color=AppColors.GRIS_MEDIO,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=40),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=width,
        )


class ProgressIndicator(ft.Container):
    def __init__(self, label: str, value: float, color: str = AppColors.AZUL_EDUCATIVO, bg_color: str = AppColors.GRIS_CLARO):
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(label, size=13, color=AppColors.GRIS_OSCURO, expand=True),
                            ft.Text(f"{value:.0%}", size=12, weight=ft.FontWeight.W_500, color=color),
                        ],
                    ),
                    ft.Stack(
                        controls=[
                            ft.Container(
                                height=8,
                                bgcolor=bg_color,
                                border_radius=4,
                            ),
                            ft.Container(
                                height=8,
                                bgcolor=color,
                                border_radius=4,
                                width=max(1, int(200 * value)),
                            ),
                        ],
                    ),
                ],
                spacing=4,
            ),
        )


class QuickAccessButton(ft.Container):
    def __init__(self, icon: ft.Icons, label: str, color: str, on_click: callable = None):
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Icon(icon, size=24, color=color),
                        bgcolor=f"{color}15",
                        border_radius=14,
                        padding=14,
                    ),
                    ft.Text(
                        label,
                        size=11,
                        color=AppColors.GRIS_TEXTO,
                        weight=ft.FontWeight.W_500,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=on_click,
            ink=True,
            border_radius=14,
        )


class FiltroTareas(ft.Container):
    def __init__(self, on_change: callable = None):
        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text("Todas", size=12, color=AppColors.AZUL_EDUCATIVO, weight=ft.FontWeight.W_500),
                        bgcolor=AppColors.AZUL_FONDO,
                        border_radius=12,
                        padding=ft.Padding(left=12, right=12, top=5, bottom=5),
                    ),
                    ft.Container(
                        content=ft.Text("Pendientes", size=12, color=AppColors.NARANJA, weight=ft.FontWeight.W_500),
                        bgcolor=AppColors.NARANJA_FONDO,
                        border_radius=12,
                        padding=ft.Padding(left=12, right=12, top=5, bottom=5),
                    ),
                    ft.Container(
                        content=ft.Text("Entregadas", size=12, color=AppColors.VERDE_ACADEMICO, weight=ft.FontWeight.W_500),
                        bgcolor=AppColors.VERDE_FONDO,
                        border_radius=12,
                        padding=ft.Padding(left=12, right=12, top=5, bottom=5),
                    ),
                    ft.Container(
                        content=ft.Text("Retrasadas", size=12, color=AppColors.ROJO, weight=ft.FontWeight.W_500),
                        bgcolor=AppColors.ROJO_FONDO,
                        border_radius=12,
                        padding=ft.Padding(left=12, right=12, top=5, bottom=5),
                    ),
                ],
                spacing=6,
                scroll=ft.ScrollMode.AUTO,
            ),
        )
