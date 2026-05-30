import flet as ft
from services.logger import get_logger
from services.tarea_service import get_tareas, TareaError
from styles.colors import AppColors
from styles.responsive import Responsive
from components.cards import TaskCard
from components.widgets import SectionHeader, FiltroTareas, EmptyState
from components.dialogs import show_alert

logger = get_logger("tareas_view")


def _build_resumen(tareas):
    pendientes = sum(1 for t in tareas if t["estado"] == "pendiente")
    entregadas = sum(1 for t in tareas if t["estado"] == "entregada")
    retrasadas = sum(1 for t in tareas if t["estado"] == "retrasada")

    return ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Pendientes", size=12, color=AppColors.GRIS_TEXTO),
                            ft.Text(str(pendientes), size=24, weight=ft.FontWeight.BOLD, color=AppColors.NARANJA),
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
                            ft.Text(str(entregadas), size=24, weight=ft.FontWeight.BOLD, color=AppColors.VERDE_ACADEMICO),
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
                            ft.Text(str(retrasadas), size=24, weight=ft.FontWeight.BOLD, color=AppColors.ROJO),
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


def create_tareas_view(page: ft.Page, selected_child: dict | None = None):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    resumen = ft.Container(content=ft.ProgressRing(), padding=20)
    tareas_list = ft.Container(content=ft.ProgressRing(), padding=20)
    child_header = ft.Container()

    async def load_tareas():
        if not selected_child:
            child_header.content = ft.Container()
            resumen.content = EmptyState(
                icon=ft.Icons.PERSON_OFF,
                title="Sin hijo seleccionado",
                subtitle="Selecciona un hijo desde el inicio",
            )
            tareas_list.content = ft.Container()
            page.update()
            return

        id_alumno = selected_child.get("id_alumno") or selected_child.get("id_usuario")
        child_name = selected_child.get("nombre_completo", "Sin nombre")

        child_header.content = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.PERSON, size=16, color=AppColors.AZUL_EDUCATIVO),
                    ft.Text(
                        f"Tareas de: {child_name}",
                        size=13,
                        weight=ft.FontWeight.W_500,
                        color=AppColors.AZUL_EDUCATIVO,
                    ),
                ],
                spacing=6,
            ),
            bgcolor=AppColors.AZUL_FONDO,
            border_radius=10,
            padding=ft.Padding(left=12, right=12, top=8, bottom=8),
        )

        try:
            tareas = await get_tareas(id_alumno)
            logger.debug("Tareas cargadas para %s: %s", id_alumno, len(tareas))

            resumen.content = _build_resumen(tareas)

            if not tareas:
                tareas_list.content = EmptyState(
                    icon=ft.Icons.ASSIGNMENT,
                    title="Sin tareas",
                    subtitle="No hay tareas asignadas para este alumno",
                )
            else:
                tareas_list.content = ft.Column(
                    controls=[TaskCard(**{k: v for k, v in t.items() if k != 'id_tarea'}, width=w - pad * 2) for t in tareas],
                    spacing=8,
                )
        except TareaError as e:
            logger.error("Error cargando tareas: %s", e.mensaje)
            show_alert(page, "Error", e.mensaje, ft.Icons.ERROR_OUTLINE)
            resumen.content = ft.Text("Error al cargar tareas")
            tareas_list.content = ft.Container()
        finally:
            page.update()

    page.run_task(load_tareas)

    contenido = ft.ListView(
        controls=[
            child_header,
            ft.Container(height=8),
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
