from math import *
from random import *

CAL_ADD = '+'
CAL_SUB = '-'
CAL_MUL = '*'
CAL_DIV = '//'

CAL_SQRT = 'isqrt('
CAL_SQRT_END = ' )'
CAL_SQUARE = 'square('
CAL_SQUARE_END = ') '

CAL_SPECIAL_LIST = [CAL_SQRT, CAL_SQRT_END, CAL_SQUARE, CAL_SQUARE_END]

CAL_PARENTHESE_OPEN = '('
CAL_PARENTHESE_CLOSE = ')'

WORD_KOREAN, WORD_MATH = 0, 1

def isqrt(n):
    return int(sqrt(n))

def square(n):
    return n**2

def sign_to_string(sign):
    lang = randint(WORD_KOREAN, WORD_MATH)
    if sign == CAL_ADD:
        if lang == WORD_MATH:
            return ' + '
        return ' 더하기 '
    elif sign == CAL_SUB:
        if lang == WORD_MATH:
            return ' - '
        return ' 빼기 '
    elif sign == CAL_MUL:
        if lang == WORD_MATH:
            return ' × '
        return ' 곱하기 '
    elif sign == CAL_DIV:
        if lang == WORD_MATH:
            return ' ÷ '
        return ' 나누기 '
    elif sign == CAL_PARENTHESE_OPEN:
        if lang == WORD_MATH:
            return '('
        return '괄호 열고 '
    elif sign == CAL_PARENTHESE_CLOSE:
        if lang == WORD_MATH:
            return ')'
        return ' 괄호 닫고'
    elif sign == CAL_SQRT:
        return '루트 '
    elif sign == CAL_SQUARE_END:
        return '의 제곱'
    elif sign == CAL_SQRT_END:
        return ''
    elif sign == CAL_SQUARE:
        return ''