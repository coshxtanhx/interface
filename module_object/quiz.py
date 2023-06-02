from pico2d import *
from module_other.coordinates import *
from random import *
from collections import deque
from module_other.calculation import *
from module_object.number import int_to_string, LANG_LIST

QUIZ_TYPE = {
    1: (int, CAL_ADD, int),
    2: (int, CAL_MUL, int, CAL_SUB, int),
    3: (int, CAL_DIV, int, CAL_ADD, int),
    4: (int, CAL_SUB, int, CAL_MUL, CAL_SQRT, int, CAL_SQRT_END),
    5: (CAL_SQUARE, int, CAL_SQUARE_END, CAL_ADD, int),
    6: (CAL_SQRT, CAL_PARENTHESE_OPEN, int, CAL_ADD, int, CAL_PARENTHESE_CLOSE, CAL_SQRT_END),
    7: (int, CAL_MUL, CAL_PARENTHESE_OPEN, int, CAL_SUB, CAL_SQRT, int,\
        CAL_SQRT_END, CAL_PARENTHESE_CLOSE),
    8: (CAL_SQUARE, int, CAL_SQUARE_END, CAL_SUB, int, CAL_SUB, int),
    9: (CAL_SQUARE, CAL_PARENTHESE_OPEN, int, CAL_MUL, int, CAL_PARENTHESE_CLOSE,
        CAL_SQUARE_END, CAL_ADD, int, CAL_SUB, int),
    10:(CAL_PARENTHESE_OPEN, int, CAL_SUB, CAL_SQRT, int, CAL_SQRT_END,
        CAL_PARENTHESE_CLOSE, CAL_MUL, CAL_PARENTHESE_OPEN, int, CAL_SUB, CAL_SQRT,
        int, CAL_SQRT_END, CAL_PARENTHESE_CLOSE)
}

QUIZ_NUMBER = {
    1: (randint(10,42), randint(30,56)),
    2: (randint(2,3), randint(11,16), randint(4,16)),
    3: (12*choice([1,2,3,4,6]), choice([3,4,6,12]), randint(10,70)),
    4: (randint(65,99), randint(2,8), randint(3,8)**2),
    5: (randint(3,5), randint(14,74)),
    6: choice([(56,35), (30,19), (98,98), (12,24), (77,4), (72,97), (88,33)]),
    7: (randint(12,18), randint(10,11), randint(6,9)**2),
    8: (randint(14,16), randint(85,96), randint(83,99)),
    9: (randint(2,3), randint(2,3), randint(87,98), randint(86,99)),
    10:(randint(1,6), randint(7,9)**2, randint(1,6), randint(7,9)**2),
}

COLOR_WHITE = (255,255,255)

class Quiz:
    font = None
    font_size = 26
    def __init__(self, stage_num):
        self.stage_num = stage_num
        self.string = ''
        self.answer = 0
        self.get_string_and_answer()
        self.string_length = len(self.string)
        if self.string_length >= 20:
            self.insert_newline()
        self.pos = [UI_WIDTH // 2, UI_HEIGHT // 2]
        if not Quiz.font:
            self.font = load_font('font/MaruBuri-Bold.ttf', Quiz.font_size)

    def draw(self):
        if self.string_length < 20:
            self.font.draw(*self.pos, self.string + ' = ?', COLOR_WHITE, 'c')
        else:
            self.font.draw(self.pos[0], self.pos[1] + 17,
                           self.string.split('\n')[0], COLOR_WHITE, 'c')
            self.font.draw(self.pos[0], self.pos[1] - 17,
                           self.string.split('\n')[1] + ' = ?', COLOR_WHITE, 'c')

    def update(self):
        pass

    def insert_newline(self):
        splited = self.string.split()
        n_splited = len(splited)
        cnt = 0
        self.string = ''
        for word in splited:
            self.string += word + ' '
            if cnt == n_splited // 2 - 1:
                self.string += '\n'
            cnt += 1

    def get_string_and_answer(self):
        number_deque = deque(QUIZ_NUMBER[self.stage_num])
        type_deque = deque(QUIZ_TYPE[self.stage_num])
        formula = ''
        for type in type_deque:
            if type == int:
                number = number_deque.popleft()
                self.string += int_to_string(number, LANG_LIST[choice([0,2])])
                formula += str(number)
                self.string 
            else:
                formula += type
                self.string += sign_to_string(type)
        self.answer = round(eval(formula))