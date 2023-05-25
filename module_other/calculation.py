from math import *

CAL_ADD = '+'
CAL_SUB = '-'
CAL_MUL = '*'
CAL_DIV = '//'

CAL_SQRT = 'isqrt('
CAL_SQRT_END = ' )'
CAL_SQUARE = 'square'
CAL_SQUARE_END = ' )'

CAL_PARENTHESE_OPEN = '('
CAL_PARENTHESE_CLOSE = ')'

def isqrt(n):
    return int(sqrt(n))

def square(n):
    return n**2