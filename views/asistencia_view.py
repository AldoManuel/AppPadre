import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.cards import AsistenciaCard
from components.widgets import SectionHeader
from components.charts import DonutChart


def create_asistencia_view(page: ft.Page):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    asistencia_mock = [
        {"fecha": "25 May 2026", "materia": "Matemáticas", "estado": "presente"},
        {"fecha": "25 May 2026", "materia": "Español", "estado": "presente"},
        {"fecha": "24 May 2026", "materia": "Ciencias", "estado": "presente"},
        {"fecha": "24 May 2026", "materia": "Historia", "estado": "ausente"},
        {"fecha": "23 May 2026", "materia": "Geografía", "estado": "retardo"},
        {"fecha": "23 May 2026", "materia": "Inglés", "estado": "presente"},
        {"fecha": "22 May 2026", "materia": "Matemáticas", "estado": "presente"},
        {"fecha": "22 May 2026", "materia": "Formación Cívica", "estado": "ausente"},
    ]

    total = len(asistencia_mock)
    presentes = sum(1 for a in asistencia_mock if a["estado"] == "presente")
    ausentes = sum(1 for a in asistencia_mock if a["estado"] == "ausente")
    retardos = sum(1 for a in asistencia_mock if a["estado"] == "retardo")
    pct = presentes / total if total > 0 else 0

    stats = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Presentes", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text(str(presentes), size=22, weight=ft.FontWeight.BOLD, color=AppColors.VERDE_ACADEMICO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.VERDE_FONDO,
                    border_radius=14,
                    padding=14,
                    expand=True,
                ),
                col={"xs": 4, "sm": 4, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Ausentes", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text(str(ausentes), size=22, weight=ft.FontWeight.BOLD, color=AppColors.ROJO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.ROJO_FONDO,
                    border_radius=14,
                    padding=14,
                    expand=True,
                ),
                col={"xs": 4, "sm": 4, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Retardos", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text(str(retardos), size=22, weight=ft.FontWeight.BOLD, color=AppColors.NARANJA),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.NARANJA_FONDO,
                    border_radius=14,
                    padding=14,
                    expand=True,
                ),
                col={"xs": 4, "sm": 4, "md": 4},
                padding=3,
            ),
        ],
    )

    chart_and_stats = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        DonutChart(percentage=pct, label="Asistencia", color=AppColors.VERDE_ACADEMICO, size=110),
                        ft.Container(width=20),
                        ft.Column(
                            controls=[
                                ft.Text(f"{pct:.0%}", size=28, weight=ft.FontWeight.BOLD, color=AppColors.VERDE_ACADEMICO),
                                ft.Text("Porcentaje de Asistencia", size=12, color=AppColors.GRIS_TEXTO),
                                ft.Container(height=6),
                                ft.Row(
                                    controls=[
                                        ft.Container(width=10, height=10, bgcolor=AppColors.VERDE_ACADEMICO, border_radius=2),
                                        ft.Text(f" {presentes} presentes", size=12, color=AppColors.GRIS_TEXTO),
                                    ],
                                    spacing=4,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(width=10, height=10, bgcolor=AppColors.ROJO, border_radius=2),
                                        ft.Text(f" {ausentes} ausentes", size=12, color=AppColors.GRIS_TEXTO),
                                    ],
                                    spacing=4,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(width=10, height=10, bgcolor=AppColors.NARANJA, border_radius=2),
                                        ft.Text(f" {retardos} retardos", size=12, color=AppColors.GRIS_TEXTO),
                                    ],
                                    spacing=4,
                                ),
                            ],
                            spacing=4,
                        ),
                    ],
                ),
            ],
        ),
        bgcolor=AppColors.BLANCO,
        border_radius=16,
        padding=16,
        border=ft.Border(
            left=ft.BorderSide(1, AppColors.GRIS_CLARO),
            right=ft.BorderSide(1, AppColors.GRIS_CLARO),
            top=ft.BorderSide(1, AppColors.GRIS_CLARO),
            bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
        ),
    )

    historial = ft.Column(
        controls=[AsistenciaCard(**a, width=w - pad * 2) for a in asistencia_mock],
        spacing=8,
    )

    contenido = ft.ListView(
        controls=[
            SectionHeader(title="Resumen de Asistencia"),
            ft.Container(height=8),
            stats,
            ft.Container(height=12),
            chart_and_stats,
            ft.Container(height=16),
            SectionHeader(title="Historial Reciente"),
            ft.Container(height=8),
            historial,
            ft.Container(height=20),
        ],
        spacing=0,
        padding=pad,
    )

    return contenido
