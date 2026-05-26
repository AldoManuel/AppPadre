import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.widgets import SectionHeader, ProgressIndicator
from components.charts import BarChart


def create_puntualidad_view(page: ft.Page):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    stats = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Puntualidad", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("92%", size=24, weight=ft.FontWeight.BOLD, color=AppColors.VERDE_ACADEMICO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.VERDE_FONDO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 6, "sm": 6, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Retardos", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("3", size=24, weight=ft.FontWeight.BOLD, color=AppColors.NARANJA),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.NARANJA_FONDO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 6, "sm": 6, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Días a Tiempo", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("35", size=24, weight=ft.FontWeight.BOLD, color=AppColors.AZUL_EDUCATIVO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.AZUL_FONDO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 12, "sm": 12, "md": 4},
                padding=3,
            ),
        ],
    )

    chart_data = [
        {"label": "Lun", "value": 4, "color": AppColors.AZUL_EDUCATIVO},
        {"label": "Mar", "value": 5, "color": AppColors.AZUL_CLARO},
        {"label": "Mié", "value": 3, "color": AppColors.NARANJA},
        {"label": "Jue", "value": 5, "color": AppColors.AZUL_EDUCATIVO},
        {"label": "Vie", "value": 4, "color": AppColors.VERDE_ACADEMICO},
    ]

    chart = BarChart(data=chart_data, height=140, width=w - pad * 2)

    indicadores = ft.Column(
        controls=[
            ProgressIndicator("Llegadas a tiempo", 0.92, AppColors.VERDE_ACADEMICO),
            ft.Container(height=12),
            ProgressIndicator("Retardos menores", 0.06, AppColors.NARANJA),
            ft.Container(height=12),
            ProgressIndicator("Retardos mayores", 0.02, AppColors.ROJO),
        ],
    )

    historial_puntualidad = ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.Icons.CHECK_CIRCLE, size=18, color=AppColors.VERDE_ACADEMICO),
                            bgcolor=AppColors.VERDE_FONDO, border_radius=8, padding=6,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Llegó a tiempo", size=14, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text("25 May 2026 - 7:30 AM", size=11, color=AppColors.GRIS_TEXTO),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.Text("+5 min", size=12, color=AppColors.VERDE_ACADEMICO, weight=ft.FontWeight.W_500),
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
                            content=ft.Icon(ft.Icons.ERROR_OUTLINE, size=18, color=AppColors.NARANJA),
                            bgcolor=AppColors.NARANJA_FONDO, border_radius=8, padding=6,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Retardo de 10 min", size=14, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text("24 May 2026 - 7:45 AM", size=11, color=AppColors.GRIS_TEXTO),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.Text("-10 min", size=12, color=AppColors.NARANJA, weight=ft.FontWeight.W_500),
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
                            content=ft.Icon(ft.Icons.CHECK_CIRCLE, size=18, color=AppColors.VERDE_ACADEMICO),
                            bgcolor=AppColors.VERDE_FONDO, border_radius=8, padding=6,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Llegó a tiempo", size=14, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text("23 May 2026 - 7:25 AM", size=11, color=AppColors.GRIS_TEXTO),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.Text("+10 min", size=12, color=AppColors.VERDE_ACADEMICO, weight=ft.FontWeight.W_500),
                    ],
                    spacing=10,
                ),
                padding=ft.Padding(left=0, right=0, top=6, bottom=6),
            ),
        ],
    )

    contenido = ft.ListView(
        controls=[
            SectionHeader(title="Estadísticas de Puntualidad"),
            ft.Container(height=8),
            stats,
            ft.Container(height=16),
            SectionHeader(title="Registro Semanal"),
            ft.Container(height=8),
            chart,
            ft.Container(height=16),
            SectionHeader(title="Indicadores"),
            ft.Container(height=8),
            ft.Container(
                content=indicadores,
                bgcolor=AppColors.BLANCO,
                border_radius=14,
                padding=16,
                border=ft.Border(
                    left=ft.BorderSide(1, AppColors.GRIS_CLARO),
                    right=ft.BorderSide(1, AppColors.GRIS_CLARO),
                    top=ft.BorderSide(1, AppColors.GRIS_CLARO),
                    bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
                ),
            ),
            ft.Container(height=16),
            SectionHeader(title="Historial"),
            ft.Container(height=8),
            ft.Container(
                content=historial_puntualidad,
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
