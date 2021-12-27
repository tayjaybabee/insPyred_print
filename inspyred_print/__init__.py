"""

A module containing a selection of variables containing ANSI Escape codes. This module contains three classes and
their attributes:

Color
  green,
  black,
  red,
  light_red,
  yellow,
  blue,
  magenta,
  cyan,
  white

Format
  bold,
  end_mod,


Effects
  blink

You can use these kinda like markup language tags. Here's an example:

.. code-block:: python
      import inspyred_print

      import inspyred_print as pallet

      c = pallet.Color()
      f = pallet.Format()
      fx = pallet.Effects()

      print(f'{fx.blink}{c.light_red} Hi there! Welcome to InsPyRed-Print!{f.end_mod}')

"""
from pypattyrn.behavioral.null import Null
from inspyred_print.version import Version

__version__ = str(Version())

class __Color(object):
    green = '\033[92m'
    black = '\u001b[30'
    red = '\033[0;31m'
    light_red = '\033[1;31m'
    yellow = '\033[0;33m'
    blue = '\033[0;34m'
    magenta = '\033[0;35m'
    cyan = '\033[0;36m'
    white = '\033[0;37m'


def Color(return_null=False):
    if return_null:
        return Null()
    else:
        return __Color


class __Format:
    bold = '\033[0;1m'
    end_mod = '\033[0m'


def Format(return_null=False):
    if return_null:
        return Null()
    else:
        return __Format()


class __Effects:
    blink = '\033[0;5m'


def Effects(return_null=False):
    if return_null:
        return Null()
    else:
        return __Effects()


class Pallet(object):
    def __init__(self, nullify=False):
        """
        
        A class containing all string formatting codes contained within inspyRed-print.
        
        Attributes:
            
            self.color:
                An object containing all the colors available in inspyRed-print.
            
            self.format:
                An object containing all the formatting codes available from inspyRed-print.
                
            self.effects:
                An object containing all the string effect codes available from inspyRed-print.
        
        Arguments:
            nullify:
                Return nullified properties for instances in which you don't want ascii formatting.
        """
        self._color = Color(nullify)
        self._format = Format(nullify)
        self._effects = Effects(nullify)
        
    @property
    def color(self):
        return self._color
    
    @property
    def format(self):
        return self._format
    
    @property
    def effects(self):
        return self._effects