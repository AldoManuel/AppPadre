import flet as ft

class AppColors:
    AZUL_EDUCATIVO = "#2563EB"
    AZUL_CLARO = "#3B82F6"
    AZUL_OSCURO = "#1D4ED8"
    VERDE_ACADEMICO = "#10B981"
    VERDE_CLARO = "#34D399"
    BLANCO = "#FFFFFF"
    GRIS_CLARO = "#F3F4F6"
    GRIS_MEDIO = "#D1D5DB"
    GRIS_OSCURO = "#1F2937"
    GRIS_TEXTO = "#6B7280"
    ROJO = "#EF4444"
    NARANJA = "#F59E0B"
    AMARILLO = "#FBBF24"
    AZUL_FONDO = "#EFF6FF"
    VERDE_FONDO = "#ECFDF5"
    ROJO_FONDO = "#FEF2F2"
    NARANJA_FONDO = "#FFFBEB"

    @staticmethod
    def status_color(status: str) -> str:
        colors = {
            "presente": AppColors.VERDE_ACADEMICO,
            "ausente": AppColors.ROJO,
            "retardo": AppColors.NARANJA,
            "pendiente": AppColors.NARANJA,
            "entregada": AppColors.VERDE_ACADEMICO,
            "retrasada": AppColors.ROJO,
            "leido": AppColors.GRIS_TEXTO,
            "no_leido": AppColors.AZUL_EDUCATIVO,
            "proximo": AppColors.AZUL_EDUCATIVO,
            "finalizado": AppColors.VERDE_ACADEMICO,
            "cancelado": AppColors.GRIS_MEDIO,
        }
        return colors.get(status.lower(), AppColors.GRIS_TEXTO)

    @staticmethod
    def status_bg_color(status: str) -> str:
        bgs = {
            "presente": AppColors.VERDE_FONDO,
            "ausente": AppColors.ROJO_FONDO,
            "retardo": AppColors.NARANJA_FONDO,
            "pendiente": AppColors.NARANJA_FONDO,
            "entregada": AppColors.VERDE_FONDO,
            "retrasada": AppColors.ROJO_FONDO,
            "leido": AppColors.GRIS_CLARO,
            "no_leido": AppColors.AZUL_FONDO,
        }
        return bgs.get(status.lower(), AppColors.GRIS_CLARO)
