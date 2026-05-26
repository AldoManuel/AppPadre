import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.widgets import SectionHeader, ProgressIndicator
from components.charts import BarChart


def create_progreso_view(page: ft.Page):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    stats = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Promedio General", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("8.7", size=24, weight=ft.FontWeight.BOLD, color=AppColors.AZUL_EDUCATIVO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.AZUL_FONDO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 6, "sm": 4, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Materias Aprobadas", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("6/8", size=24, weight=ft.FontWeight.BOLD, color=AppColors.VERDE_ACADEMICO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.VERDE_FONDO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 6, "sm": 4, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Rendimiento", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("87%", size=24, weight=ft.FontWeight.BOLD, color=AppColors.GRIS_OSCURO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.GRIS_CLARO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 12, "sm": 4, "md": 4},
                padding=3,
            ),
        ],
    )

    chart_data = [
        {"label": "Mat", "value": 9, "color": AppColors.AZUL_EDUCATIVO},
        {"label": "Esp", "value": 8, "color": AppColors.VERDE_ACADEMICO},
        {"label": "Cien", "value": 9, "color": AppColors.AZUL_CLARO},
        {"label": "His", "value": 7, "color": AppColors.NARANJA},
        {"label": "Geo", "value": 10, "color": AppColors.VERDE_ACADEMICO},
        {"label": "Ing", "value": 8, "color": AppColors.AZUL_EDUCATIVO},
        {"label": "F. Cív", "value": 9, "color": AppColors.AZUL_CLARO},
        {"label": "E. Fís", "value": 10, "color": AppColors.VERDE_ACADEMICO},
    ]

    chart = BarChart(data=chart_data, height=160, width=w - pad * 2)

    materias = [
        ("Matemáticas", 9.0, AppColors.AZUL_EDUCATIVO),
        ("Español", 8.0, AppColors.VERDE_ACADEMICO),
        ("Ciencias Naturales", 9.0, AppColors.AZUL_CLARO),
        ("Historia", 7.0, AppColors.NARANJA),
        ("Geografía", 10.0, AppColors.VERDE_ACADEMICO),
        ("Inglés", 8.0, AppColors.AZUL_EDUCATIVO),
        ("Formación Cívica", 9.0, AppColors.AZUL_CLARO),
        ("Educación Física", 10.0, AppColors.VERDE_ACADEMICO),
    ]

    materias_list = ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ProgressIndicator(materia, calif / 10, color),
                        ft.Container(height=12) if i < len(materias) - 1 else ft.Container(),
                    ],
                ),
            )
            for i, (materia, calif, color) in enumerate(materias)
        ],
        spacing=0,
    )

    materia_detalle = ft.Container(
        content=materias_list,
        bgcolor=AppColors.BLANCO,
        border_radius=14,
        padding=16,
        border=ft.Border(
            left=ft.BorderSide(1, AppColors.GRIS_CLARO),
            right=ft.BorderSide(1, AppColors.GRIS_CLARO),
            top=ft.BorderSide(1, AppColors.GRIS_CLARO),
            bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
        ),
    )

    contenido = ft.ListView(
        controls=[
            SectionHeader(title="Progreso Académico"),
            ft.Container(height=8),
            stats,
            ft.Container(height=16),
            SectionHeader(title="Calificaciones por Materia"),
            ft.Container(height=8),
            chart,
            ft.Container(height=16),
            SectionHeader(title="Detalle por Materia"),
            ft.Container(height=8),
            materia_detalle,
            ft.Container(height=20),
        ],
        spacing=0,
        padding=pad,
    )

    return contenido
