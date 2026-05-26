import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.cards import NotificationCard
from components.widgets import SectionHeader


def create_notificaciones_view(page: ft.Page):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    notificaciones_mock = [
        {"titulo": "Nueva tarea asignada", "mensaje": "Se ha asignado una nueva tarea de Matemáticas: Resolver ejercicios de fracciones.", "tiempo": "Hace 2 horas", "leido": False},
        {"titulo": "Recordatorio de evento", "mensaje": "Junta de padres programada para el 25 de Mayo a las 8:00 AM.", "tiempo": "Hace 5 horas", "leido": False},
        {"titulo": "Asistencia registrada", "mensaje": "Carlos ha sido registrado como presente el día de hoy.", "tiempo": "Hace 6 horas", "leido": False},
        {"titulo": "Calificación publicada", "mensaje": "La calificación del examen de Ciencias Naturales ya está disponible.", "tiempo": "Ayer", "leido": True},
        {"titulo": "Tarea entregada", "mensaje": "La tarea de Español ha sido marcada como entregada.", "tiempo": "Ayer", "leido": True},
        {"titulo": "Aviso importante", "mensaje": "Suspensión de clases el 15 de Mayo por día festivo oficial.", "tiempo": "Hace 3 días", "leido": True},
        {"titulo": "Recordatorio de puntualidad", "mensaje": "Se recomienda llegar 10 minutos antes del horario de entrada.", "tiempo": "Hace 4 días", "leido": True},
        {"titulo": "Evento próximo", "mensaje": "Festival del Día del Niño - 30 de Abril. ¡No falten!", "tiempo": "Hace 1 semana", "leido": True},
    ]

    no_leidas = sum(1 for n in notificaciones_mock if not n["leido"])

    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Notificaciones", size=16, weight=ft.FontWeight.BOLD, color=AppColors.GRIS_OSCURO),
                ft.Container(
                    content=ft.Text(
                        f"{no_leidas} nuevas",
                        size=12,
                        color=AppColors.BLANCO,
                        weight=ft.FontWeight.W_500,
                    ),
                    bgcolor=AppColors.AZUL_EDUCATIVO,
                    border_radius=12,
                    padding=ft.Padding(left=10, right=10, top=3, bottom=3),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    notificaciones_list = ft.Column(
        controls=[NotificationCard(**n, width=w - pad * 2) for n in notificaciones_mock],
        spacing=6,
    )

    contenido = ft.ListView(
        controls=[
            header,
            ft.Container(height=4),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("Marcar todas como leídas", size=12, color=AppColors.AZUL_EDUCATIVO),
                            ink=True,
                            border_radius=8,
                            padding=ft.Padding(left=8, right=8, top=4, bottom=4),
                        ),
                        ft.Icon(ft.Icons.DONE_ALL, size=16, color=AppColors.AZUL_EDUCATIVO),
                    ],
                    spacing=4,
                ),
                alignment=ft.alignment.Alignment(1.0, 0.0),
            ),
            ft.Container(height=8),
            notificaciones_list,
            ft.Container(height=20),
        ],
        spacing=0,
        padding=pad,
    )

    return contenido
