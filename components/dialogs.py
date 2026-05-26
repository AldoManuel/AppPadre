import flet as ft
from styles.colors import AppColors

def show_snackbar(page: ft.Page, message: str, color: str = AppColors.VERDE_ACADEMICO):
    page.snack_bar = ft.SnackBar(
        content=ft.Text(message, color=AppColors.BLANCO, size=14),
        bgcolor=color,
        behavior=ft.SnackBarBehavior.FLOATING,
        duration=2500,
        shape=ft.RoundedRectangleBorder(radius=10),
    )
    page.snack_bar.open = True
    page.update()


def show_alert(page: ft.Page, title: str, message: str, icon: ft.Icons = ft.Icons.INFO):
    dialog = ft.AlertDialog(
        title=ft.Row(
            controls=[
                ft.Icon(icon, color=AppColors.AZUL_EDUCATIVO, size=24),
                ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=AppColors.GRIS_OSCURO),
            ],
            spacing=8,
        ),
        content=ft.Text(message, size=14, color=AppColors.GRIS_TEXTO),
        actions=[
            ft.TextButton(
                content="Entendido",
                style=ft.ButtonStyle(
                    color=AppColors.AZUL_EDUCATIVO,
                    text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                ),
                on_click=lambda e: close_dialog(page),
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape=ft.RoundedRectangleBorder(radius=16),
    )
    page.dialog = dialog
    dialog.open = True
    page.update()


def close_dialog(page: ft.Page):
    if page.dialog:
        page.dialog.open = False
        page.update()
