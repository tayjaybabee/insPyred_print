"""

A module containing a selection of variables containing ANSI Escape codes. This module contains two classes:

Color
Format

"""


class Color:
    green = '\033[92m'
    black = '\u001b[30'
    red = '\033[0;31m'
    light_red = '\033[1;31m'
    yellow = '\033[0;33m'
    blue = '\033[0;34m'
    magenta = '\033[0;35m'
    cyan = '\033[0;36m'
    white = '\033[0;37m'


class Format:
    bold = '\033[0;1m'
    end_mod = '\033[0m'


class Effects:
    blink = '\033[0;5m'
