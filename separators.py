'''
Provide Separator Widgets
'''
from libqtile.widget.textbox import TextBox
from .icons import icons

DEFAULT_FONTSIZE = 35


def left_half_circle(fg_color, bg_color, fontsize=DEFAULT_FONTSIZE):
    '''TextBox with a left_half_circle'''
    return TextBox(
        text=icons['left_half_circle'],
        fontsize=fontsize,
        foreground=fg_color,
        background=bg_color,
        padding=0)


def right_half_circle(fg_color, bg_color, fontsize=DEFAULT_FONTSIZE):
    '''TextBox with a right_half_circle'''
    return TextBox(
        text=icons['right_half_circle'],
        fontsize=fontsize,
        background=bg_color,
        foreground=fg_color,
        padding=0)


def left_arrow(bg_color, fg_color, fontsize=DEFAULT_FONTSIZE):
    '''TextBox with a left_arrow'''
    return TextBox(
        text=icons['left_arrow'],
        padding=0,
        fontsize=fontsize,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color, fontsize=DEFAULT_FONTSIZE):
    '''TextBox with a right_arrow'''
    return TextBox(
        text=icons['right_arrow'],
        padding=0,
        fontsize=fontsize,
        background=bg_color,
        foreground=fg_color)
