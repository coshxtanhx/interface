from pico2d import *
from module_other.coordinates import *
from random import *
import module_system.server as sv
import module_system.opencv_manager as om
import module_system.stage_manager as sm

COLOR_YELLOW = (255, 255, 0)
COLOR_PINK = (255, 105, 180)

LANG_LIST = ['아라비아', '순우리말', '한자어']

class Number:
    font = None
    font_size = { '아라비아': 30, '한자어': 20, '순우리말': 20 }
    def __init__(self, number = None, lang = None, pos = None, is_answer = None):
        self.is_answer = is_answer # 메인 스테이지에서만 유효한 변수
        self.timer = 2.0 # 메인 스테이지에서만 유효한 변수
        self.number = number if number else randint(1, 99)
        self.lang = lang if lang else choice(LANG_LIST)
        self.pos = list(POS_NUMBER[pos]) if pos else list(POS_NUMBER[choice(POS_RANGE)])
        self.number_string = int_to_string(self.number, self.lang)
        if not Number.font:
            self.font = load_font('font/MaruBuri-Bold.ttf', Number.font_size[self.lang])
    def update(self):
        import module_system.main_stage_manager as msm
        if msm.STAGE.started:
            if self.pos[0] - self.font.image.w // 2 <= sv.cursor.x <= \
                    self.pos[0] + self.font.image.w // 2 and \
                    self.pos[1] - self.font.image.h // 2 <= sv.cursor.y <= \
                    self.pos[1] + self.font.image.h // 2:
                self.timer -= om.accumulated_time
            else:
                self.timer = 2.0
            if self.timer <= 0:
                if self.is_answer:
                    print("good")
                    msm.STAGE.users_answer_list[msm.STAGE.current_level] = 1
                else:
                    msm.STAGE.users_answer_list[msm.STAGE.current_level] = -1
    def draw(self):
        if sm.STAGE.started and sm.STAGE.current_level <= 9:
            max_number = get_max_number()
            if self.number == max_number:
                color = COLOR_PINK
            else:
                color = COLOR_YELLOW
        else:
            color = COLOR_YELLOW
        self.font.draw(*self.pos, self.number_string, color, 'c')


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

def get_max_number():
    max_number = -1
    for number in sv.numbers:
        if number.number > max_number:
            max_number = number.number
    if sm.STAGE.current_level > 9:
        max_number = max(max_number, 9)  # 9스테이지 이후에도 최소값은 9로 설정
    return max_number
