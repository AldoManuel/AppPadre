import flet as ft
from styles.colors import AppColors

class StatCard(ft.Container):
    def __init__(self, title: str, value: str, icon: ft.Icons, color: str, width: int = None):
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Icon(icon, size=20, color=AppColors.BLANCO),
                                bgcolor=color,
                                border_radius=10,
                                padding=8,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value,
                                        size=22,
                                        weight=ft.FontWeight.BOLD,
                                        color=AppColors.GRIS_OSCURO,
                                    ),
                                    ft.Text(
                                        title,
                                        size=12,
                                        color=AppColors.GRIS_TEXTO,
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                        ],
                        spacing=12,
                    ),
                ],
            ),
            bgcolor=AppColors.BLANCO,
            border_radius=16,
            padding=16,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=8,
                color="rgba(37,99,235,0.08)",
                offset=ft.Offset(0, 2),
            ),
            border=ft.Border(
                left=ft.BorderSide(1, AppColors.GRIS_CLARO),
                right=ft.BorderSide(1, AppColors.GRIS_CLARO),
                top=ft.BorderSide(1, AppColors.GRIS_CLARO),
                bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
            ),
            width=width,
            ink=True,
        )


class TaskCard(ft.Container):
    def __init__(self, materia: str, descripcion: str, fecha: str, estado: str, width: int = None):
        color_estado = AppColors.status_color(estado)
        bg_estado = AppColors.status_bg_color(estado)

        icono_estado = {
            "pendiente": ft.Icons.HOURGLASS_EMPTY,
            "entregada": ft.Icons.CHECK_CIRCLE,
            "retrasada": ft.Icons.ERROR_OUTLINE,
        }.get(estado.lower(), ft.Icons.HELP_OUTLINE)

        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Icon(icono_estado, size=18, color=color_estado),
                                bgcolor=bg_estado,
                                border_radius=8,
                                padding=6,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        materia,
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                        color=AppColors.GRIS_OSCURO,
                                    ),
                                    ft.Text(
                                        descripcion,
                                        size=12,
                                        color=AppColors.GRIS_TEXTO,
                                        max_lines=2,
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                        ],
                        spacing=10,
                    ),
                    ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.CALENDAR_TODAY, size=12, color=AppColors.GRIS_TEXTO),
                                    ft.Text(fecha, size=11, color=AppColors.GRIS_TEXTO),
                                ],
                                spacing=4,
                            ),
                            ft.Container(
                                content=ft.Text(
                                    estado.capitalize(),
                                    size=11,
                                    weight=ft.FontWeight.W_500,
                                    color=color_estado,
                                ),
                                bgcolor=bg_estado,
                                border_radius=12,
                                padding=ft.Padding(left=10, right=10, top=3, bottom=3),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                spacing=8,
            ),
            bgcolor=AppColors.BLANCO,
            border_radius=14,
            padding=14,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=6,
                color="rgba(0,0,0,0.04)",
                offset=ft.Offset(0, 1),
            ),
            border=ft.Border(
                left=ft.BorderSide(1, AppColors.GRIS_CLARO),
                right=ft.BorderSide(1, AppColors.GRIS_CLARO),
                top=ft.BorderSide(1, AppColors.GRIS_CLARO),
                bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
            ),
            width=width,
            ink=True,
        )


class EventCard(ft.Container):
    def __init__(self, titulo: str, fecha: str, hora: str, descripcion: str, tipo: str = "proximo", width: int = None):
        color_tipo = AppColors.status_color(tipo)
        bg_tipo = AppColors.status_bg_color(tipo)

        iconos = {
            "proximo": ft.Icons.STAR,
            "finalizado": ft.Icons.CHECK,
            "cancelado": ft.Icons.CANCEL,
        }

        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Icon(
                                    iconos.get(tipo, ft.Icons.EVENT),
                                    size=18,
                                    color=color_tipo,
                                ),
                                bgcolor=bg_tipo,
                                border_radius=10,
                                padding=8,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        titulo,
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                        color=AppColors.GRIS_OSCURO,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.Icons.CALENDAR_TODAY, size=11, color=AppColors.GRIS_TEXTO),
                                            ft.Text(fecha, size=11, color=AppColors.GRIS_TEXTO),
                                            ft.Text("|", size=11, color=AppColors.GRIS_MEDIO),
                                            ft.Icon(ft.Icons.SCHEDULE, size=11, color=AppColors.GRIS_TEXTO),
                                            ft.Text(hora, size=11, color=AppColors.GRIS_TEXTO),
                                        ],
                                        spacing=3,
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                        ],
                        spacing=10,
                    ),
                    ft.Text(
                        descripcion,
                        size=12,
                        color=AppColors.GRIS_TEXTO,
                        max_lines=2,
                    ),
                ],
                spacing=6,
            ),
            bgcolor=AppColors.BLANCO,
            border_radius=14,
            padding=14,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=6,
                color="rgba(0,0,0,0.04)",
                offset=ft.Offset(0, 1),
            ),
            border=ft.Border(
                left=ft.BorderSide(1, AppColors.GRIS_CLARO),
                right=ft.BorderSide(1, AppColors.GRIS_CLARO),
                top=ft.BorderSide(1, AppColors.GRIS_CLARO),
                bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
            ),
            width=width,
            ink=True,
        )


class NotificationCard(ft.Container):
    def __init__(self, titulo: str, mensaje: str, tiempo: str, leido: bool = False, width: int = None):
        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(
                            ft.Icons.CIRCLE if not leido else ft.Icons.CHECK_CIRCLE_OUTLINE,
                            size=10 if not leido else 18,
                            color=AppColors.AZUL_EDUCATIVO if not leido else AppColors.GRIS_MEDIO,
                        ),
                        border_radius=12,
                        padding=ft.Padding(left=leido and 4 or 0, right=leido and 4 or 0, top=leido and 4 or 0, bottom=leido and 4 or 0),
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                titulo,
                                size=14,
                                weight=ft.FontWeight.BOLD if not leido else ft.FontWeight.W_400,
                                color=AppColors.GRIS_OSCURO if not leido else AppColors.GRIS_TEXTO,
                            ),
                            ft.Text(
                                mensaje,
                                size=12,
                                color=AppColors.GRIS_TEXTO,
                                max_lines=2,
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.ACCESS_TIME, size=10, color=AppColors.GRIS_MEDIO),
                                    ft.Text(tiempo, size=10, color=AppColors.GRIS_MEDIO),
                                ],
                                spacing=3,
                            ),
                        ],
                        spacing=3,
                        expand=True,
                    ),
                ],
                spacing=10,
            ),
            bgcolor=AppColors.BLANCO if not leido else AppColors.GRIS_CLARO,
            border_radius=12,
            padding=12,
            border=ft.Border(
                left=ft.BorderSide(1, AppColors.GRIS_CLARO),
                right=ft.BorderSide(1, AppColors.GRIS_CLARO),
                top=ft.BorderSide(1, AppColors.GRIS_CLARO),
                bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
            ) if not leido else None,
            width=width,
            ink=True,
        )


class AsistenciaCard(ft.Container):
    def __init__(self, fecha: str, materia: str, estado: str, width: int = None):
        color = AppColors.status_color(estado)
        bg = AppColors.status_bg_color(estado)
        iconos = {
            "presente": ft.Icons.CHECK_CIRCLE,
            "ausente": ft.Icons.CANCEL,
            "retardo": ft.Icons.SCHEDULE,
        }

        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(
                            iconos.get(estado, ft.Icons.HELP),
                            size=22,
                            color=color,
                        ),
                        bgcolor=bg,
                        border_radius=10,
                        padding=8,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(materia, size=14, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                            ft.Text(fecha, size=11, color=AppColors.GRIS_TEXTO),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.Container(
                        content=ft.Text(
                            estado.capitalize(),
                            size=11,
                            weight=ft.FontWeight.W_500,
                            color=color,
                        ),
                        bgcolor=bg,
                        border_radius=12,
                        padding=ft.Padding(left=10, right=10, top=3, bottom=3),
                    ),
                ],
                spacing=10,
            ),
            bgcolor=AppColors.BLANCO,
            border_radius=14,
            padding=14,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=6,
                color="rgba(0,0,0,0.04)",
                offset=ft.Offset(0, 1),
            ),
            border=ft.Border(
                left=ft.BorderSide(1, AppColors.GRIS_CLARO),
                right=ft.BorderSide(1, AppColors.GRIS_CLARO),
                top=ft.BorderSide(1, AppColors.GRIS_CLARO),
                bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
            ),
            width=width,
            ink=True,
        )
