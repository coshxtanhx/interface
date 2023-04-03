from pico2d import *
from module_other.coordinates import *
from random import *
import module_system.server as sv

COLOR_YELLOW = (255, 255, 0)

LANG_LIST = ['아라비아', '순우리말', '한자어']

class Number:
    font = None
    font_size = { '아라비아': 50, '한자어': 25, '순우리말': 25 }
    def __init__(self, number = None, lang = None, pos = None):
        self.number = number if number else randint(1, 99)
        self.lang = lang if lang else choice(LANG_LIST)
        self.pos = list(POS_NUMBER[pos]) if pos else list(POS_NUMBER[choice(POS_RANGE)])
        self.number_string = int_to_string(self.number, self.lang)
        self.length = len(self.number_string)
        correct_pos(self.pos, self.length, self.lang)
        if not Number.font:
            self.font = load_font('font/MaruBuri-Bold.ttf', Number.font_size[self.lang])
    def update(self):
        pass
    def draw(self):
        self.font.draw(*self.pos, self.number_string, COLOR_YELLOW)
    def delete_from_server(self):
        sv.numbers.remove(self)

def int_to_string(n, lang):
    result = ''
    if lang == '아라비아':
        result = str(n)
        return result
    elif lang == '한자어':
        digits = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
        ten_digit_number = n // 10
        if ten_digit_number == 0:
            pass
        elif ten_digit_number == 1:
            result += '십'
        else:
            result += digits[ten_digit_number]
            result += '십'
        result += digits[n % 10]
        return result
    elif lang == '순우리말':
        digits = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']
        tens = ['', '열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
        ten_digit_number = n // 10
        if ten_digit_number == 0:
            pass
        else:
            result += tens[ten_digit_number]
        result += digits[n % 10]
        return result