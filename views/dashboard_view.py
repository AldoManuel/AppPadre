import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.appbar import ModernAppBar
from components.navbar import AppNavBar, AppDrawer
from components.cards import StatCard
from components.widgets import SectionHeader, QuickAccessButton
from components.dialogs import show_alert


def create_dashboard_view(page: ft.Page, on_nav_change):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    stats = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=StatCard(
                    title="Tareas Pendientes",
                    value="4",
                    icon=ft.Icons.ASSIGNMENT,
                    color=AppColors.AZUL_EDUCATIVO,
                ),
                col={"xs": 12, "sm": 6, "md": 4},
                padding=4,
            ),
            ft.Container(
                content=StatCard(
                    title="Asistencia",
                    value="95%",
                    icon=ft.Icons.CHECK_CIRCLE,
                    color=AppColors.VERDE_ACADEMICO,
                ),
                col={"xs": 12, "sm": 6, "md": 4},
                padding=4,
            ),
            ft.Container(
                content=StatCard(
                    title="Próximo Evento",
                    value="2 días",
                    icon=ft.Icons.EVENT,
                    color=AppColors.NARANJA,
                ),
                col={"xs": 12, "sm": 6, "md": 4},
                padding=4,
            ),
        ],
    )

    alumno_info = ft.Container(
        content=ft.Row(
            controls=[
                ft.CircleAvatar(
                    content=ft.Icon(ft.Icons.PERSON, size=30, color=AppColors.BLANCO),
                    bgcolor=AppColors.AZUL_EDUCATIVO,
                    radius=Responsive.avatar_size(w) // 2,
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            "Carlos Pérez López",
                            size=Responsive.font_size_md(w),
                            weight=ft.FontWeight.BOLD,
                            color=AppColors.GRIS_OSCURO,
                        ),
                        ft.Text(
                            "3er Grado • Grupo B",
                            size=Responsive.font_size_sm(w),
                            color=AppColors.GRIS_TEXTO,
                        ),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.SYNC_ALT, size=20, color=AppColors.AZUL_EDUCATIVO),
                    bgcolor=AppColors.AZUL_FONDO,
                    border_radius=10,
                    padding=8,
                    on_click=lambda e: print("Cambiar hijo"),
                ),
            ],
            spacing=12,
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
    )

    accesos = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=QuickAccessButton(
                    icon=ft.Icons.ASSIGNMENT,
                    label="Tareas",
                    color=AppColors.AZUL_EDUCATIVO,
                    on_click=lambda e: on_nav_change(1),
                ),
                col={"xs": 4, "sm": 3, "md": 2},
            ),
            ft.Container(
                content=QuickAccessButton(
                    icon=ft.Icons.CHECK_CIRCLE,
                    label="Asistencia",
                    color=AppColors.VERDE_ACADEMICO,
                    on_click=lambda e: on_nav_change(2),
                ),
                col={"xs": 4, "sm": 3, "md": 2},
            ),
            ft.Container(
                content=QuickAccessButton(
                    icon=ft.Icons.SCHEDULE,
                    label="Puntualidad",
                    color=AppColors.NARANJA,
                    on_click=lambda e: on_nav_change(3),
                ),
                col={"xs": 4, "sm": 3, "md": 2},
            ),
            ft.Container(
                content=QuickAccessButton(
                    icon=ft.Icons.EVENT,
                    label="Eventos",
                    color=AppColors.ROJO,
                    on_click=lambda e: on_nav_change(4),
                ),
                col={"xs": 4, "sm": 3, "md": 2},
            ),
            ft.Container(
                content=QuickAccessButton(
                    icon=ft.Icons.BAR_CHART,
                    label="Progreso",
                    color=AppColors.GRIS_OSCURO,
                    on_click=lambda e: on_nav_change(5),
                ),
                col={"xs": 4, "sm": 3, "md": 2},
            ),
        ],
    )

    actividad_reciente = ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.Icons.ASSIGNMENT, size=16, color=AppColors.NARANJA),
                            bgcolor=AppColors.NARANJA_FONDO,
                            border_radius=8,
                            padding=6,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Tarea asignada: Matemáticas", size=13, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text("Hace 2 horas", size=11, color=AppColors.GRIS_TEXTO),
                            ],
                            spacing=1,
                            expand=True,
                        ),
                    ],
                    spacing=8,
                ),
                padding=ft.Padding(left=0, right=0, top=8, bottom=8),
            ),
            ft.Divider(height=1, color=AppColors.GRIS_CLARO),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.Icons.CHECK_CIRCLE, size=16, color=AppColors.VERDE_ACADEMICO),
                            bgcolor=AppColors.VERDE_FONDO,
                            border_radius=8,
                            padding=6,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Asistencia confirmada: Hoy", size=13, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text("Hace 5 horas", size=11, color=AppColors.GRIS_TEXTO),
                            ],
                            spacing=1,
                            expand=True,
                        ),
                    ],
                    spacing=8,
                ),
                padding=ft.Padding(left=0, right=0, top=8, bottom=8),
            ),
            ft.Divider(height=1, color=AppColors.GRIS_CLARO),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.Icons.EVENT, size=16, color=AppColors.AZUL_EDUCATIVO),
                            bgcolor=AppColors.AZUL_FONDO,
                            border_radius=8,
                            padding=6,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Evento próximo: Junta de padres", size=13, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text("En 2 días", size=11, color=AppColors.GRIS_TEXTO),
                            ],
                            spacing=1,
                            expand=True,
                        ),
                    ],
                    spacing=8,
                ),
                padding=ft.Padding(left=0, right=0, top=8, bottom=8),
            ),
        ],
    )

    contenido = ft.ListView(
        controls=[
            alumno_info,
            ft.Container(height=16),
            stats,
            ft.Container(height=16),
            SectionHeader(title="Accesos Rápidos"),
            ft.Container(height=8),
            accesos,
            ft.Container(height=16),
            SectionHeader(title="Actividad Reciente"),
            ft.Container(height=4),
            ft.Container(
                content=actividad_reciente,
                bgcolor=AppColors.BLANCO,
                border_radius=14,
                padding=12,
                border=ft.Border(
            left=ft.BorderSide(1, AppColors.GRIS_CLARO),
            right=ft.BorderSide(1, AppColors.GRIS_CLARO),
            top=ft.BorderSide(1, AppColors.GRIS_CLARO),
            bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
        ),
            ),
            ft.Container(height=16),
            SectionHeader(title="Próximos Eventos", action_text="Ver todos"),
            ft.Container(height=4),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text("25", size=18, weight=ft.FontWeight.BOLD, color=AppColors.AZUL_EDUCATIVO),
                                                ft.Text("MAY", size=9, color=AppColors.AZUL_EDUCATIVO),
                                            ],
                                            spacing=0,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        bgcolor=AppColors.AZUL_FONDO,
                                        border_radius=10,
                                        padding=ft.Padding(left=8, right=8, top=8, bottom=8),
                                        width=50,
                                        height=50,
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Junta de Padres", size=14, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                            ft.Text("8:00 AM - Salon de Actos", size=11, color=AppColors.GRIS_TEXTO),
                                        ],
                                        spacing=2,
                                        expand=True,
                                    ),
                                    ft.Icon(ft.Icons.CHEVRON_RIGHT, size=18, color=AppColors.GRIS_MEDIO),
                                ],
                                spacing=10,
                            ),
                            padding=ft.Padding(left=0, right=0, top=6, bottom=6),
                        ),
                        ft.Divider(height=1, color=AppColors.GRIS_CLARO),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text("28", size=18, weight=ft.FontWeight.BOLD, color=AppColors.VERDE_ACADEMICO),
                                                ft.Text("MAY", size=9, color=AppColors.VERDE_ACADEMICO),
                                            ],
                                            spacing=0,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        bgcolor=AppColors.VERDE_FONDO,
                                        border_radius=10,
                                        padding=ft.Padding(left=8, right=8, top=8, bottom=8),
                                        width=50,
                                        height=50,
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Entrega de Calificaciones", size=14, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                            ft.Text("10:00 AM - Plataforma", size=11, color=AppColors.GRIS_TEXTO),
                                        ],
                                        spacing=2,
                                        expand=True,
                                    ),
                                    ft.Icon(ft.Icons.CHEVRON_RIGHT, size=18, color=AppColors.GRIS_MEDIO),
                                ],
                                spacing=10,
                            ),
                            padding=ft.Padding(left=0, right=0, top=6, bottom=6),
                        ),
                    ],
                ),
                bgcolor=AppColors.BLANCO,
                border_radius=14,
                padding=12,
                border=ft.Border(
            left=ft.BorderSide(1, AppColors.GRIS_CLARO),
            right=ft.BorderSide(1, AppColors.GRIS_CLARO),
            top=ft.BorderSide(1, AppColors.GRIS_CLARO),
            bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
        ),
            ),
            ft.Container(height=20),
        ],
        spacing=0,
        padding=pad,
    )

    return contenido
