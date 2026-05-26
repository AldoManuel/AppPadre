import flet as ft
from styles.colors import AppColors

class AppNavBar(ft.NavigationBar):
    def __init__(self, on_change):
        super().__init__(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Inicio",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.ASSIGNMENT_OUTLINED,
                    selected_icon=ft.Icons.ASSIGNMENT,
                    label="Tareas",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.CALENDAR_MONTH_OUTLINED,
                    selected_icon=ft.Icons.CALENDAR_MONTH,
                    label="Eventos",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.BAR_CHART_OUTLINED,
                    selected_icon=ft.Icons.BAR_CHART,
                    label="Progreso",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                    selected_icon=ft.Icons.NOTIFICATIONS,
                    label="Notif.",
                ),
            ],
            on_change=on_change,
            bgcolor=AppColors.BLANCO,
            selected_index=0,
            indicator_color=AppColors.AZUL_FONDO,
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
            height=65,
            border=ft.Border(top=ft.BorderSide(1, AppColors.GRIS_CLARO)),
        )


class AppDrawer(ft.NavigationDrawer):
    def __init__(self, page: ft.Page, on_destination_click):
        w = page.window.width if page.window else 600

        super().__init__(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(height=20),
                            ft.CircleAvatar(
                                content=ft.Icon(
                                    ft.Icons.PERSON,
                                    size=40,
                                    color=AppColors.BLANCO,
                                ),
                                bgcolor=AppColors.AZUL_EDUCATIVO,
                                radius=30,
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                "Familia Pérez",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppColors.GRIS_OSCURO,
                            ),
                            ft.Text(
                                "papelopez@email.com",
                                size=13,
                                color=AppColors.GRIS_TEXTO,
                            ),
                            ft.Text(
                                "Hijos: 2",
                                size=12,
                                color=AppColors.GRIS_MEDIO,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.AZUL_EDUCATIVO,
                    padding=20,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.Alignment(0.0, -1.0),
                        end=ft.alignment.Alignment(0.0, 1.0),
                        colors=[AppColors.AZUL_EDUCATIVO, AppColors.AZUL_OSCURO],
                    ),
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Inicio",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.ASSIGNMENT_OUTLINED,
                    selected_icon=ft.Icons.ASSIGNMENT,
                    label="Tareas",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.CHECK_CIRCLE_OUTLINED,
                    selected_icon=ft.Icons.CHECK_CIRCLE,
                    label="Asistencia",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.SCHEDULE_OUTLINED,
                    selected_icon=ft.Icons.SCHEDULE,
                    label="Puntualidad",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.CALENDAR_MONTH_OUTLINED,
                    selected_icon=ft.Icons.CALENDAR_MONTH,
                    label="Eventos",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.BAR_CHART_OUTLINED,
                    selected_icon=ft.Icons.BAR_CHART,
                    label="Progreso",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                    selected_icon=ft.Icons.NOTIFICATIONS,
                    label="Notificaciones",
                ),
                ft.Divider(height=1, color=AppColors.GRIS_CLARO),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.LOGOUT,
                    selected_icon=ft.Icons.LOGOUT,
                    label="Cerrar Sesión",
                ),
            ],
            on_change=on_destination_click,
            bgcolor=AppColors.BLANCO,
        )
