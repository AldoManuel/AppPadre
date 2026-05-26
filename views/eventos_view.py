import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.cards import EventCard
from components.widgets import SectionHeader


def create_eventos_view(page: ft.Page):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    eventos_mock = [
        {"titulo": "Junta de Padres de Familia", "fecha": "25 May 2026", "hora": "8:00 AM", "descripcion": "Reuni\u00f3n general con directivos y maestros para revisar el progreso del semestre.", "tipo": "proximo"},
        {"titulo": "Entrega de Calificaciones", "fecha": "28 May 2026", "hora": "10:00 AM", "descripcion": "Publicaci\u00f3n de calificaciones del segundo bimestre en la plataforma.", "tipo": "proximo"},
        {"titulo": "Festival del D\u00eda del Ni\u00f1o", "fecha": "30 Abr 2026", "hora": "9:00 AM", "descripcion": "Evento recreativo con actividades para los estudiantes.", "tipo": "finalizado"},
        {"titulo": "Suspensi\u00f3n de Clases", "fecha": "15 May 2026", "hora": "Todo el d\u00eda", "descripcion": "D\u00eda festivo oficial seg\u00fan el calendario escolar.", "tipo": "cancelado"},
        {"titulo": "Taller de Padres", "fecha": "1 Jun 2026", "hora": "4:00 PM", "descripcion": "Taller sobre c\u00f3mo apoyar a tus hijos en la educaci\u00f3n virtual.", "tipo": "proximo"},
        {"titulo": "Examen Bimestral", "fecha": "5 Jun 2026", "hora": "7:30 AM", "descripcion": "Inicio de ex\u00e1menes del tercer bimestre.", "tipo": "proximo"},
    ]

    eventos_list = ft.Column(
        controls=[EventCard(**e, width=w - pad * 2) for e in eventos_mock],
        spacing=8,
    )

    contenido = ft.ListView(
        controls=[
            SectionHeader(title="Eventos Escolares", action_text="Calendario"),
            ft.Container(height=12),
            ft.Tabs(
                length=3,
                selected_index=0,
                animation_duration=300,
                content=ft.Column(
                    controls=[
                        ft.TabBar(
                            tabs=[
                                ft.Tab(label="Pr\u00f3ximos"),
                                ft.Tab(label="Todos"),
                                ft.Tab(label="Finalizados"),
                            ],
                            tab_alignment=ft.TabAlignment.START,
                            label_color=AppColors.AZUL_EDUCATIVO,
                            unselected_label_color=AppColors.GRIS_TEXTO,
                            indicator_color=AppColors.AZUL_EDUCATIVO,
                        ),
                        ft.TabBarView(
                            expand=True,
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        controls=[EventCard(**e, width=w - pad * 2) for e in eventos_mock if e["tipo"] == "proximo"],
                                        spacing=8,
                                    ),
                                    padding=ft.Padding(left=0, right=0, top=12, bottom=12),
                                ),
                                ft.Container(
                                    content=eventos_list,
                                    padding=ft.Padding(left=0, right=0, top=12, bottom=12),
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[EventCard(**e, width=w - pad * 2) for e in eventos_mock if e["tipo"] != "proximo"],
                                        spacing=8,
                                    ),
                                    padding=ft.Padding(left=0, right=0, top=12, bottom=12),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
            ft.Container(height=20),
        ],
        spacing=0,
        padding=pad,
    )

    return contenido
