import flet as ft
from services.logger import get_logger
from services.dashboard_service import get_dashboard, DashboardError
from styles.colors import AppColors
from styles.responsive import Responsive
from components.cards import StatCard
from components.widgets import SectionHeader, QuickAccessButton, EmptyState
from components.dialogs import show_alert

logger = get_logger("dashboard_view")


def _build_alumno_card(alumno, w, on_switch_child):
    return ft.Container(
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
                            alumno.get("nombre_completo", "Sin nombre"),
                            size=Responsive.font_size_md(w),
                            weight=ft.FontWeight.BOLD,
                            color=AppColors.GRIS_OSCURO,
                        ),
                        ft.Text(
                            f'{alumno.get("grado", "")} • Grupo {alumno.get("grupo", "")}',
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
                    on_click=on_switch_child,
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


def _build_stats(alumno):
    tareas = alumno.get("tareas_pendientes", 0)
    asistencia = alumno.get("asistencia_porcentaje", 0)
    return ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=StatCard(
                    title="Tareas Pendientes",
                    value=str(tareas),
                    icon=ft.Icons.ASSIGNMENT,
                    color=AppColors.AZUL_EDUCATIVO,
                ),
                col={"xs": 12, "sm": 6, "md": 4},
                padding=4,
            ),
            ft.Container(
                content=StatCard(
                    title="Asistencia",
                    value=f"{asistencia}%",
                    icon=ft.Icons.CHECK_CIRCLE,
                    color=AppColors.VERDE_ACADEMICO,
                ),
                col={"xs": 12, "sm": 6, "md": 4},
                padding=4,
            ),
            ft.Container(
                content=StatCard(
                    title="Promedio",
                    value=str(alumno.get("promedio", "N/A")),
                    icon=ft.Icons.SCHOOL,
                    color=AppColors.NARANJA,
                ),
                col={"xs": 12, "sm": 6, "md": 4},
                padding=4,
            ),
        ],
    )


def _build_actividad(data):
    items = data.get("actividad_reciente", [])
    if not items:
        return EmptyState(
            icon=ft.Icons.HISTORY,
            title="Sin actividad reciente",
            subtitle="No hay registros de actividad disponibles",
        )

    controls = []
    for i, act in enumerate(items):
        if i > 0:
            controls.append(ft.Divider(height=1, color=AppColors.GRIS_CLARO))
        controls.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.Icons.NOTIFICATIONS, size=16, color=AppColors.AZUL_EDUCATIVO),
                            bgcolor=AppColors.AZUL_FONDO,
                            border_radius=8,
                            padding=6,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(act.get("accion", ""), size=13, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text(act.get("created_at", "")[:10] if act.get("created_at") else "", size=11, color=AppColors.GRIS_TEXTO),
                            ],
                            spacing=1,
                            expand=True,
                        ),
                    ],
                    spacing=8,
                ),
                padding=ft.Padding(left=0, right=0, top=8, bottom=8),
            )
        )

    return ft.Column(controls=controls)


def _build_eventos(data):
    items = data.get("proximos_eventos", [])
    if not items:
        return EmptyState(
            icon=ft.Icons.EVENT,
            title="Sin eventos próximos",
            subtitle="No hay eventos programados",
        )

    controls = []
    for i, ev in enumerate(items):
        if i > 0:
            controls.append(ft.Divider(height=1, color=AppColors.GRIS_CLARO))
        controls.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(ev.get("fecha", "")[8:10] if ev.get("fecha") else "", size=18, weight=ft.FontWeight.BOLD, color=AppColors.AZUL_EDUCATIVO),
                                    ft.Text((ev.get("fecha", "")[5:7] if ev.get("fecha") else ""), size=9, color=AppColors.AZUL_EDUCATIVO),
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
                                ft.Text(ev.get("titulo", ""), size=14, weight=ft.FontWeight.W_500, color=AppColors.GRIS_OSCURO),
                                ft.Text(
                                    f'{ev.get("hora", "")} - {ev.get("descripcion", "")}' if ev.get("hora") else ev.get("descripcion", ""),
                                    size=11, color=AppColors.GRIS_TEXTO,
                                ),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.Icon(ft.Icons.CHEVRON_RIGHT, size=18, color=AppColors.GRIS_MEDIO),
                    ],
                    spacing=10,
                ),
                padding=ft.Padding(left=0, right=0, top=6, bottom=6),
            )
        )

    return ft.Column(controls=controls)


def create_dashboard_view(page: ft.Page, user_data: dict, on_nav_change):
    w = page.window.width if page.window else 600
    logger.debug("Renderizando dashboard para usuario %s", user_data.get("id_usuario"))
    pad = Responsive.padding(w)

    id_padre = user_data.get("id_usuario")
    alumno_card = ft.Container(content=ft.ProgressRing(), padding=20)
    stats_row = ft.Container(content=ft.ProgressRing(), padding=20)
    actividad_section = ft.Container(content=ft.ProgressRing(), padding=20)
    eventos_section = ft.Container(content=ft.ProgressRing(), padding=20)

    async def load_data():
        try:
            data = await get_dashboard(id_padre)
            hijos = data.get("hijos", [])
            if not hijos:
                alumno_card.content = EmptyState(
                    icon=ft.Icons.PERSON_OFF,
                    title="Sin alumnos vinculados",
                    subtitle="No tienes hijos registrados en el sistema",
                )
                stats_row.content = ft.Text("")
            else:
                alumno = hijos[0]
                alumno_card.content = _build_alumno_card(alumno, w, on_switch_child)
                stats_row.content = _build_stats(alumno)

            actividad_section.content = _build_actividad(data)
            eventos_section.content = _build_eventos(data)
        except DashboardError as e:
            logger.error("Error cargando dashboard: %s", e.mensaje)
            show_alert(page, "Error", e.mensaje, ft.Icons.ERROR_OUTLINE)
            alumno_card.content = ft.Text("Error al cargar datos")
        finally:
            page.update()

    def on_switch_child(e):
        logger.debug("Cambiar hijo presionado")
        show_alert(page, "Info", "Selección de múltiples hijos próximamente", ft.Icons.INFO)

    page.run_task(load_data)

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

    contenido = ft.ListView(
        controls=[
            alumno_card,
            ft.Container(height=16),
            stats_row,
            ft.Container(height=16),
            SectionHeader(title="Accesos Rápidos"),
            ft.Container(height=8),
            accesos,
            ft.Container(height=16),
            SectionHeader(title="Actividad Reciente"),
            ft.Container(height=4),
            ft.Container(
                content=actividad_section,
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
                content=eventos_section,
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
