import flet as ft
from styles.colors import AppColors

class AppTheme:
    @staticmethod
    def light_theme() -> ft.Theme:
        return ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=AppColors.AZUL_EDUCATIVO,
                primary_container=AppColors.AZUL_FONDO,
                secondary=AppColors.VERDE_ACADEMICO,
                secondary_container=AppColors.VERDE_FONDO,
                surface=AppColors.BLANCO,
                surface_container_highest=AppColors.GRIS_CLARO,
                surface_container_lowest=AppColors.BLANCO,
                surface_tint=AppColors.AZUL_EDUCATIVO,
                on_primary=AppColors.BLANCO,
                on_secondary=AppColors.BLANCO,
                on_surface=AppColors.GRIS_OSCURO,
                on_surface_variant=AppColors.GRIS_TEXTO,
                outline=AppColors.GRIS_MEDIO,
                error=AppColors.ROJO,
                error_container=AppColors.ROJO_FONDO,
            ),
            font_family="Segoe UI",
            use_material3=True,
        )

    @staticmethod
    def dark_theme() -> ft.Theme:
        return ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=AppColors.AZUL_CLARO,
                primary_container="#1E3A5F",
                secondary=AppColors.VERDE_CLARO,
                secondary_container="#1A3A30",
                surface=AppColors.GRIS_OSCURO,
                surface_container_highest="#374151",
                surface_container_lowest="#111827",
                surface_tint=AppColors.AZUL_CLARO,
                on_primary=AppColors.BLANCO,
                on_secondary=AppColors.BLANCO,
                on_surface=AppColors.GRIS_CLARO,
                on_surface_variant=AppColors.GRIS_MEDIO,
                outline="#4B5563",
                error=AppColors.ROJO,
                error_container="#3B1A1A",
            ),
            font_family="Segoe UI",
            use_material3=True,
        )
