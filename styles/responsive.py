import flet as ft

class ResponsiveSize:
    PHONE_SMALL = 360
    PHONE_MEDIUM = 390
    PHONE_LARGE = 412
    TABLET = 600
    TABLET_LARGE = 768
    DESKTOP = 1024

class Responsive:
    @staticmethod
    def is_phone(width: int) -> bool:
        return width < ResponsiveSize.TABLET

    @staticmethod
    def is_tablet(width: int) -> bool:
        return ResponsiveSize.TABLET <= width < ResponsiveSize.DESKTOP

    @staticmethod
    def is_desktop(width: int) -> bool:
        return width >= ResponsiveSize.DESKTOP

    @staticmethod
    def card_width(width: int) -> int:
        if Responsive.is_desktop(width):
            return 350
        if Responsive.is_tablet(width):
            return 300
        return width - 32

    @staticmethod
    def grid_cross_axis_count(width: int) -> int:
        if Responsive.is_desktop(width):
            return 3
        if Responsive.is_tablet(width):
            return 2
        return 1

    @staticmethod
    def font_size_lg(width: int) -> int:
        if Responsive.is_desktop(width):
            return 24
        if Responsive.is_tablet(width):
            return 22
        return 20

    @staticmethod
    def font_size_md(width: int) -> int:
        if Responsive.is_desktop(width):
            return 18
        if Responsive.is_tablet(width):
            return 16
        return 15

    @staticmethod
    def font_size_sm(width: int) -> int:
        if Responsive.is_desktop(width):
            return 15
        if Responsive.is_tablet(width):
            return 14
        return 13

    @staticmethod
    def font_size_xs(width: int) -> int:
        if Responsive.is_desktop(width):
            return 13
        if Responsive.is_tablet(width):
            return 12
        return 11

    @staticmethod
    def padding(width: int) -> int:
        if Responsive.is_desktop(width):
            return 40
        if Responsive.is_tablet(width):
            return 30
        return 16

    @staticmethod
    def avatar_size(width: int) -> int:
        if Responsive.is_desktop(width):
            return 56
        if Responsive.is_tablet(width):
            return 48
        return 40
