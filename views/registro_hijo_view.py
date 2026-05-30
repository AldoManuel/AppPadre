import flet as ft
from services.logger import get_logger
from services.registro_service import registrar_hijo, RegistroError
from styles.colors import AppColors
from styles.responsive import Responsive
from components.dialogs import show_snackbar

logger = get_logger("registro_hijo_view")


def create_registro_hijo_view(page: ft.Page, id_padre: str, on_success=None, on_cancel=None):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    loading = ft.ProgressRing(width=20, height=20, visible=False)
    error_text = ft.Text("", size=13, color=AppColors.ROJO, visible=False)
    success_text = ft.Text("", size=14, color=AppColors.VERDE_ACADEMICO, visible=False)

    nombre = ft.TextField(
        label="Nombre(s)",
        hint_text="Ej: Carlos",
        prefix_icon=ft.Icons.PERSON,
        text_size=14,
        border_radius=10,
        dense=True,
    )
    ap_paterno = ft.TextField(
        label="Apellido Paterno",
        hint_text="Ej: Martínez",
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        text_size=14,
        border_radius=10,
        dense=True,
    )
    ap_materno = ft.TextField(
        label="Apellido Materno (opcional)",
        hint_text="Ej: López",
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        text_size=14,
        border_radius=10,
        dense=True,
    )
    correo = ft.TextField(
        label="Correo (opcional)",
        hint_text="alumno@ejemplo.com",
        prefix_icon=ft.Icons.EMAIL,
        text_size=14,
        border_radius=10,
        dense=True,
    )
    grupo_dd = ft.Dropdown(
        label="Grupo",
        value="1",
        options=[
            ft.dropdown.Option("1", "Grupo A"),
            ft.dropdown.Option("2", "Grupo B"),
            ft.dropdown.Option("3", "Grupo C"),
        ],
        text_size=14,
        border_radius=10,
        dense=True,
    )
    parentesco_dd = ft.Dropdown(
        label="Parentesco",
        value="TUTOR",
        options=[
            ft.dropdown.Option("MADRE", "Madre"),
            ft.dropdown.Option("PADRE", "Padre"),
            ft.dropdown.Option("TUTOR", "Tutor"),
        ],
        text_size=14,
        border_radius=10,
        dense=True,
    )

    async def submit_async(e):
        nombre_val = nombre.value.strip()
        if not nombre_val:
            error_text.value = "El nombre es obligatorio"
            error_text.visible = True
            success_text.visible = False
            page.update()
            return
        ap_val = ap_paterno.value.strip()
        if not ap_val:
            error_text.value = "El apellido paterno es obligatorio"
            error_text.visible = True
            success_text.visible = False
            page.update()
            return

        error_text.visible = False
        success_text.visible = False
        loading.visible = True
        page.update()

        try:
            result = await registrar_hijo(
                id_padre=id_padre,
                nombre=nombre_val,
                apellido_paterno=ap_val,
                apellido_materno=ap_materno.value.strip() or None,
                correo=correo.value.strip() or None,
                id_grupo=int(grupo_dd.value),
                parentesco=parentesco_dd.value,
            )
            loading.visible = False
            success_text.value = f"{result.get('nombre_completo', 'Hijo')} registrado correctamente"
            success_text.visible = True
            page.update()

            show_snackbar(page, "Hijo registrado con éxito")

            if on_success:
                on_success()
        except RegistroError as exc:
            loading.visible = False
            error_text.value = exc.mensaje
            error_text.visible = True
            logger.error("Error registrando hijo: %s", exc.mensaje)
            page.update()

    def submit(e):
        page.run_task(submit_async, e)

    def cancel(e):
        if on_cancel:
            on_cancel()

    form_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.PERSON_ADD, size=28, color=AppColors.AZUL_EDUCATIVO),
                        ft.Text(
                            "Registrar Hijo",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=AppColors.GRIS_OSCURO,
                        ),
                    ],
                    spacing=10,
                ),
                ft.Text(
                    "Completa los datos para registrar a un nuevo hijo",
                    size=13,
                    color=AppColors.GRIS_TEXTO,
                ),
                ft.Divider(height=1, color=AppColors.GRIS_CLARO),
                ft.Container(height=4),
                error_text,
                success_text,
                nombre,
                ap_paterno,
                ap_materno,
                correo,
                ft.Row(
                    controls=[
                        ft.Container(grupo_dd, expand=True),
                        ft.Container(parentesco_dd, expand=True),
                    ],
                    spacing=10,
                ),
                ft.Container(height=8),
                ft.Row(
                    controls=[
                        ft.OutlinedButton(
                            content="Cancelar",
                            style=ft.ButtonStyle(
                                color=AppColors.GRIS_TEXTO,
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                            on_click=cancel,
                        ),
                        ft.FilledButton(
                            content=ft.Row(
                                controls=[
                                    loading,
                                    ft.Text("Registrar", size=14),
                                ],
                                spacing=6,
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=AppColors.AZUL_EDUCATIVO,
                                color=AppColors.BLANCO,
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                            on_click=submit,
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            spacing=8,
        ),
        bgcolor=AppColors.BLANCO,
        border_radius=16,
        padding=20,
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

    contenido = ft.ListView(
        controls=[
            ft.Container(height=8),
            form_card,
        ],
        spacing=0,
        padding=pad,
    )

    return contenido
