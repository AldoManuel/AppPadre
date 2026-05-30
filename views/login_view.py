import re
import flet as ft
from services.logger import get_logger
from styles.colors import AppColors
from styles.responsive import Responsive
from components.dialogs import show_alert
from services.supabase_service import login as supabase_login, LoginError

logger = get_logger("login_view")


def create_login_view(page: ft.Page, on_login_success):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    COLOR_ERROR = "#D32F2F"

    error_ui = ft.Text(
        value="",
        visible=False,
        color=COLOR_ERROR,
        size=12,
        text_align=ft.TextAlign.CENTER,
    )

    def mostrar_error(mensaje: str):
        error_ui.value = mensaje
        error_ui.visible = True

    def limpiar_errores(e=None):
        correo_field.border_color = AppColors.GRIS_MEDIO
        correo_field.error_text = None
        contrasena_field.border_color = AppColors.GRIS_MEDIO
        contrasena_field.error_text = None
        error_ui.visible = False
        if e:
            page.update()

    correo_field = ft.TextField(
        label="Correo electrónico",
        hint_text="ejemplo@correo.com",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        border=ft.InputBorder.OUTLINE,
        border_color=AppColors.GRIS_MEDIO,
        focused_border_color=AppColors.AZUL_EDUCATIVO,
        focused_border_width=2,
        border_radius=12,
        bgcolor=AppColors.BLANCO,
        filled=True,
        fill_color=AppColors.GRIS_CLARO,
        text_size=14,
        label_style=ft.TextStyle(size=13, color=AppColors.GRIS_TEXTO),
        on_focus=limpiar_errores,
        on_change=limpiar_errores,
    )
    contrasena_field = ft.TextField(
        label="Contraseña",
        hint_text="••••••••",
        prefix_icon=ft.Icons.LOCK_OUTLINED,
        password=True,
        can_reveal_password=True,
        border=ft.InputBorder.OUTLINE,
        border_color=AppColors.GRIS_MEDIO,
        focused_border_color=AppColors.AZUL_EDUCATIVO,
        focused_border_width=2,
        border_radius=12,
        bgcolor=AppColors.BLANCO,
        filled=True,
        fill_color=AppColors.GRIS_CLARO,
        text_size=14,
        label_style=ft.TextStyle(size=13, color=AppColors.GRIS_TEXTO),
        on_focus=limpiar_errores,
        on_change=limpiar_errores,
    )

    login_btn = ft.Button(
        content=ft.Text("Iniciar Sesión", size=15, weight=ft.FontWeight.BOLD),
        style=ft.ButtonStyle(
            color=AppColors.BLANCO,
            bgcolor=AppColors.AZUL_EDUCATIVO,
            padding=ft.Padding(left=0, right=0, top=16, bottom=16),
            shape=ft.RoundedRectangleBorder(radius=14),
        ),
        width=w > 600 and 400 or None,
    )

    img_src = ft.Icon(
        ft.Icons.SCHOOL,
        size=Responsive.avatar_size(w) + 20,
        color=AppColors.AZUL_EDUCATIVO,
    )

    async def handle_login(e):
        correo = correo_field.value.strip() if correo_field.value else ""
        contrasena = contrasena_field.value if contrasena_field.value else ""

        if not correo or not contrasena:
            logger.warning("Intento de login con campos vacíos")
            if not correo:
                correo_field.border_color = COLOR_ERROR
                correo_field.error_text = "Campo obligatorio"
            if not contrasena:
                contrasena_field.border_color = COLOR_ERROR
                contrasena_field.error_text = "Campo obligatorio"
            mostrar_error("Todos los campos son obligatorios")
            show_alert(page, "Campos vacíos", "Todos los campos son obligatorios", ft.Icons.WARNING)
            page.update()
            return

        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", correo):
            logger.warning("Intento de login con correo inválido: %s", correo)
            correo_field.border_color = COLOR_ERROR
            correo_field.error_text = "Correo inválido"
            contrasena_field.border_color = COLOR_ERROR
            contrasena_field.error_text = None
            mostrar_error("El correo electrónico no tiene un formato válido")
            show_alert(page, "Correo inválido", "El correo electrónico no tiene un formato válido", ft.Icons.WARNING)
            page.update()
            return

        logger.info("Usuario presionó login: correo=%s", correo)

        login_btn.disabled = True
        login_btn.content = ft.ProgressRing(width=20, height=20, color=AppColors.BLANCO)
        page.update()

        try:
            user_data = await supabase_login(correo, contrasena)
            logger.info("Login exitoso desde la UI, redirigiendo...")
            show_alert(page, "Bienvenido", f"Inicio de sesión exitoso. Redirigiendo...", ft.Icons.CHECK_CIRCLE)
            on_login_success(user_data)
        except LoginError as err:
            logger.warning("Login rechazado para %s: %s", correo, err.mensaje)
            correo_field.border_color = COLOR_ERROR
            correo_field.error_text = err.mensaje
            contrasena_field.border_color = COLOR_ERROR
            contrasena_field.error_text = None
            mostrar_error(err.mensaje)
            show_alert(page, "Error al iniciar sesión", err.mensaje, ft.Icons.ERROR_OUTLINE)
            page.update()
        except Exception as exc:
            logger.error("Error no controlado en login para %s: %s", correo, exc)
            mostrar_error("Ocurrió un error inesperado. Intenta de nuevo")
            show_alert(page, "Error inesperado", "Ocurrió un error. Intenta de nuevo", ft.Icons.ERROR_OUTLINE)
            page.update()
        finally:
            login_btn.disabled = False
            login_btn.content = ft.Text("Iniciar Sesión", size=15, weight=ft.FontWeight.BOLD)
            page.update()

    login_btn.on_click = handle_login

    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=40),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=img_src,
                                bgcolor=AppColors.AZUL_FONDO,
                                border_radius=30,
                                padding=16,
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                "App Padre",
                                size=Responsive.font_size_lg(w) + 4,
                                weight=ft.FontWeight.BOLD,
                                color=AppColors.GRIS_OSCURO,
                            ),
                            ft.Text(
                                "Seguimiento Escolar",
                                size=Responsive.font_size_sm(w),
                                color=AppColors.GRIS_TEXTO,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(height=30),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            correo_field,
                            ft.Container(height=10),
                            contrasena_field,
                            ft.Container(height=6),
                            error_ui,
                            ft.Container(height=14),
                            login_btn,
                            ft.Container(height=10),
                            ft.TextButton(
                                content="¿Olvidaste tu contraseña?",
                                style=ft.ButtonStyle(
                                    color=AppColors.AZUL_EDUCATIVO,
                                    text_style=ft.TextStyle(size=13),
                                ),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=w > 600 and 420 or None,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        gradient=ft.LinearGradient(
            begin=ft.alignment.Alignment(0.0, -1.0),
            end=ft.alignment.Alignment(0.0, 1.0),
            colors=[AppColors.BLANCO, AppColors.GRIS_CLARO],
        ),
        expand=True,
    )

    return ft.View(
        route="/login",
        controls=[container],
        padding=pad,
        bgcolor=AppColors.BLANCO,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
