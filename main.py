import flet as ft
from services.logger import get_logger
from app import AppPadre

logger = get_logger("main")


def main(page: ft.Page):
    logger.info("Iniciando AppPadre (ventana %sx%s)", 390, 844)
    page.window.width = 390
    page.window.height = 844
    AppPadre(page)


if __name__ == "__main__":
    logger.info("=== INICIO DE APLICACIÓN ===")
    logger.debug("Plataforma: Windows | Python | Flet 0.85.2")
    ft.run(main)
    logger.info("=== FIN DE APLICACIÓN ===")
