import flet as ft
from styles.colors import AppColors


class BarChart(ft.Container):
    def __init__(self, data: list, height: int = 160, width: int = None):
        max_val = max(d["value"] for d in data) if data else 1
        bar_width = max(30, min(50, (width or 300) // len(data) - 8)) if data else 30

        bars = []
        for item in data:
            pct = item["value"] / max_val
            color = item.get("color", AppColors.AZUL_EDUCATIVO)
            bars.append(
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                str(item["value"]),
                                size=10,
                                color=AppColors.GRIS_TEXTO,
                                weight=ft.FontWeight.W_500,
                            ),
                            alignment=ft.alignment.Alignment(0.0, 1.0),
                        ),
                        ft.Container(
                            height=max(4, int(height * 0.7 * pct)),
                            width=bar_width,
                            bgcolor=color,
                            border_radius=ft.BorderRadius(
                                top_left=6,
                                top_right=6,
                                bottom_left=0,
                                bottom_right=0,
                            ),
                            animate=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE_OUT),
                        ),
                        ft.Container(
                            content=ft.Text(
                                item["label"],
                                size=9,
                                color=AppColors.GRIS_TEXTO,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            width=bar_width + 10,
                            alignment=ft.alignment.Alignment(0.0, 0.0),
                        ),
                    ],
                    spacing=4,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.END,
                )
            )

        super().__init__(
            content=ft.Container(
                content=ft.Row(
                    controls=bars,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                ),
                padding=ft.Padding(top=10, left=4, right=4, bottom=4),
            ),
            bgcolor=AppColors.BLANCO,
            border_radius=16,
            padding=12,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=6,
                color="rgba(0,0,0,0.04)",
                offset=ft.Offset(0, 1),
            ),
            border=ft.Border(
                left=ft.BorderSide(1, AppColors.GRIS_CLARO),
                right=ft.BorderSide(1, AppColors.GRIS_CLARO),
                top=ft.BorderSide(1, AppColors.GRIS_CLARO),
                bottom=ft.BorderSide(1, AppColors.GRIS_CLARO),
            ),
            width=width,
        )


class DonutChart(ft.Container):
    def __init__(self, percentage: float, label: str, color: str = AppColors.VERDE_ACADEMICO, size: int = 100):
        super().__init__(
            content=ft.Stack(
                controls=[
                    ft.Container(
                        width=size,
                        height=size,
                        border_radius=size // 2,
                        bgcolor=AppColors.GRIS_CLARO,
                    ),
                    ft.Container(
                        width=size,
                        height=size,
                        border_radius=size // 2,
                        gradient=ft.RadialGradient(
                            center=ft.alignment.Alignment(0.0, 0.0),
                            radius=0.9,
                            colors=[color, color],
                            stops=[percentage, percentage],
                        ),
                    ),
                    ft.Container(
                        width=size - 20,
                        height=size - 20,
                        border_radius=(size - 20) // 2,
                        bgcolor=AppColors.BLANCO,
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    f"{percentage:.0%}",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=color,
                                ),
                                ft.Text(
                                    label,
                                    size=9,
                                    color=AppColors.GRIS_TEXTO,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=0,
                        ),
                        alignment=ft.alignment.Alignment(0.0, 0.0),
                    ),
                ],
                width=size,
                height=size,
            ),
        )


class SimpleProgressBar(ft.Container):
    def __init__(self, value: float, color: str = AppColors.AZUL_EDUCATIVO, height: int = 12, width: int = None):
        super().__init__(
            content=ft.Stack(
                controls=[
                    ft.Container(height=height, bgcolor=AppColors.GRIS_CLARO, border_radius=height // 2),
                    ft.Container(
                        height=height,
                        width=max(height, int((width or 200) * value)),
                        bgcolor=color,
                        border_radius=height // 2,
                        animate=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE_OUT),
                    ),
                ],
            ),
            width=width,
        )
