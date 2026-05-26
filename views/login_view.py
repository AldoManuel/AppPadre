import flet as ft
from styles.colors import AppColors
from styles.responsive import Responsive
from components.dialogs import show_alert


def create_login_view(page: ft.Page, on_login_success):
    w = page.window.width if page.window else 600
    pad = Responsive.padding(w)

    img_src = ft.Icon(
        ft.Icons.SCHOOL,
        size=Responsive.avatar_size(w) + 20,
        color=AppColors.AZUL_EDUCATIVO,
    )

    def handle_login(e):
        show_alert(page, "Bienvenido", "Acceso simulado correctamente")
        on_login_success()

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
                            ft.TextField(
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
                                label_style=ft.TextStyle(
                                    size=13,
                                    color=AppColors.GRIS_TEXTO,
                                ),
                            ),
                            ft.Container(height=10),
                            ft.TextField(
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
                                label_style=ft.TextStyle(
                                    size=13,
                                    color=AppColors.GRIS_TEXTO,
                                ),
                            ),
                            ft.Container(height=20),
                            ft.Button(
                                content="Iniciar Sesión",
                                on_click=handle_login,
                                style=ft.ButtonStyle(
                                    color=AppColors.BLANCO,
                                    bgcolor=AppColors.AZUL_EDUCATIVO,
                                    padding=ft.Padding(left=0, right=0, top=16, bottom=16),
                                    shape=ft.RoundedRectangleBorder(radius=14),
                                    text_style=ft.TextStyle(
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                                width=w > 600 and 400 or None,
                            ),
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
