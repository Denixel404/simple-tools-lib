import re
import sys
import os
from math import sqrt
from expressions import *

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root not in sys.path:
    sys.path.append(root)
from Config.tokens import _tokenize


def quad(a: float, b: float, c: float) -> list:
     """
    Поиск 
    Args: 
      a (float): коэффициени a
      b (float): коэффициени b
      c (float): коэффициени c
    Returns: 
      list[float]: список корней x
      float[d]: дискриминант d
    """
     d = b**2 - 4 * a * c
     print(d)
     x = []
     if d > 0:
         x.append((-b - sqrt(d)) / (2 * a))
         x.append((-b + sqrt(d)) / (2 * a))
         
     elif d == 0: 
         x.append(-b / (2 * a))
     return x, d
     
def linear(var: str, equa: str): 
    if len(var) > 1 or var.isdigit():
         raise ValueError("Variable must be a single letter")
    equation = norm_expr(equa)
    var = var.lower()
    parts = equation.split("=")
    left = parts[0]
    right = parts[1]
    
    print(_tokenize(left))
    
    
    print(equation)
    print(parts)
    
        
