import flet as ft
from app import AppPadre


def main(page: ft.Page):
    page.window.width = 390
    page.window.height = 844
    AppPadre(page)


if __name__ == "__main__":
    ft.run(main)
