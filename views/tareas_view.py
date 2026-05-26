import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.cards import TaskCard
from components.widgets import SectionHeader, FiltroTareas


def create_tareas_view(page: ft.Page):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    tareas_mock = [
        {"materia": "Matemáticas", "descripcion": "Resolver ejercicios del 1 al 20 sobre fracciones", "fecha": "25 May 2026", "estado": "pendiente"},
        {"materia": "Español", "descripcion": "Redactar un ensayo sobre la lectura del libro", "fecha": "24 May 2026", "estado": "entregada"},
        {"materia": "Ciencias Naturales", "descripcion": "Investigación sobre el sistema solar", "fecha": "26 May 2026", "estado": "retrasada"},
        {"materia": "Historia", "descripcion": "Línea del tiempo de la Revolución Mexicana", "fecha": "23 May 2026", "estado": "entregada"},
        {"materia": "Geografía", "descripcion": "Mapa conceptual de continentes y océanos", "fecha": "27 May 2026", "estado": "pendiente"},
        {"materia": "Inglés", "descripcion": "Vocabulary list - Unit 5", "fecha": "22 May 2026", "estado": "entregada"},
        {"materia": "Formación Cívica", "descripcion": "Cartel sobre valores familiares", "fecha": "28 May 2026", "estado": "pendiente"},
        {"materia": "Educación Física", "descripcion": "Rutina de ejercicios en casa", "fecha": "21 May 2026", "estado": "retrasada"},
    ]

    resumen = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Pendientes", size=12, color=AppColors.GRIS_TEXTO),
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
                col={"xs": 4, "sm": 4, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Entregadas", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("3", size=24, weight=ft.FontWeight.BOLD, color=AppColors.VERDE_ACADEMICO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.VERDE_FONDO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 4, "sm": 4, "md": 4},
                padding=3,
            ),
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Retrasadas", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text("2", size=24, weight=ft.FontWeight.BOLD, color=AppColors.ROJO),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=AppColors.ROJO_FONDO,
                    border_radius=14,
                    padding=16,
                    expand=True,
                ),
                col={"xs": 4, "sm": 4, "md": 4},
                padding=3,
            ),
        ],
    )

    tareas_list = ft.Column(
        controls=[TaskCard(**t, width=w - pad * 2) for t in tareas_mock],
        spacing=8,
    )

    contenido = ft.ListView(
        controls=[
            SectionHeader(title="Mis Tareas", action_text="Filtrar"),
            ft.Container(height=4),
            resumen,
            ft.Container(height=12),
            FiltroTareas(),
            ft.Container(height=12),
            tareas_list,
            ft.Container(height=20),
        ],
        spacing=0,
        padding=pad,
    )

    return contenido
