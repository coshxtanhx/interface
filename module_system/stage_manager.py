from random import *
from module_object.number import Number
from module_other.coordinates import *
from module_system.debug_manager import *
import module_system.server as sv
import module_system.game_world as gw
import module_system.opencv_manager as om
import module_system.game_framework as gf
import module_system.data_collector as dc

TUTORIAL_ANSWER_IS_CENTER = [
    [randint(8,9), '아라비아', CENTER],
    [randint(1,2), '아라비아', CENTER_RIGHT],
    [randint(3,4), '아라비아', CENTER_LEFT]
]

TUTORIAL_ANSWER_IS_RIGHT = [
    [randint(28,59), '아라비아', RIGHT],
    [randint(4,7), '아라비아', CENTER],
    [randint(8,14), '아라비아', LEFT]
]

TUTORIAL_ANSWER_IS_LEFT = [
    [randint(81,94), '아라비아', LEFT],
    [randint(2,6), '아라비아', CENTER],
    [randint(12,19), '아라비아', RIGHT]
]

TUTORIAL_ANSWER_IS_TOP = [
    [randint(32,52), '아라비아', TOP],
    [randint(1,7), '아라비아', BOTTOM],
    [randint(9,15), '아라비아', LEFT]
]

TUTORIAL_ANSWER_IS_BOTTOM = [
    [randint(71,84), '아라비아', BOTTOM],
    [randint(5,11), '아라비아', TOP],
    [randint(12,27), '아라비아', RIGHT]
]

TUTORIAL_ANSWER_IS_RIGHT_BOTTOM = [
    [randint(72,97), '아라비아', RIGHT_BOTTOM],
    [randint(5,11), '아라비아', TOP],
    [randint(1,4), '아라비아', BOTTOM]
]

TUTORIAL_ANSWER_IS_LEFT_BOTTOM = [
    [randint(65,81), '아라비아', LEFT_BOTTOM],
    [randint(2,9), '아라비아', RIGHT_TOP],
    [randint(10,21), '아라비아', BOTTOM]
]

TUTORIAL_ANSWER_IS_RIGHT_TOP = [
    [randint(95,99), '아라비아', RIGHT_TOP],
    [randint(3,12), '아라비아', LEFT_BOTTOM],
    [randint(13,20), '아라비아', BOTTOM]
]

TUTORIAL_ANSWER_IS_LEFT_TOP = [
    [randint(82,99), '아라비아', LEFT_TOP],
    [randint(4,9), '아라비아', RIGHT],
    [randint(12,17), '아라비아', LEFT_BOTTOM]
]

locations = list(POS_RANGE)

LAST_STAGE = 20

stages = [
    None,
    TUTORIAL_ANSWER_IS_CENTER,
    TUTORIAL_ANSWER_IS_RIGHT,
    TUTORIAL_ANSWER_IS_LEFT,
    TUTORIAL_ANSWER_IS_TOP,
    TUTORIAL_ANSWER_IS_BOTTOM,
    TUTORIAL_ANSWER_IS_RIGHT_BOTTOM,
    TUTORIAL_ANSWER_IS_LEFT_BOTTOM,
    TUTORIAL_ANSWER_IS_RIGHT_TOP,
    TUTORIAL_ANSWER_IS_LEFT_TOP
]

lang_type = ['아라비아', '한자어', '순우리말']

def randlang(n=3):
    return choice(lang_type[0:n])

class STAGE:
    started = False
    current_level = 1
    answer_of_tutorial = None
    def get_answer_of_current_level():
        return stages[STAGE.current_level][0][2]
    def shuffle_stage():
        for a, b in ((2,3), (4,5), (6,7), (6,8), (6,9), (7,8), (7,9), (8,9)):
            if randint(0,1):
                stages[a], stages[b], stages[b], stages[a]
    def add_stage():
        number_list = list(range(1,100))
        pos_list = list(POS_RANGE)
        shuffle(number_list)
        shuffle(pos_list)
        if STAGE.current_level <= 11:
            n_select = 5
            stages.append(
                [[number_list[i], '아라비아', pos_list[i]] for i in range(n_select)]
            )
        elif STAGE.current_level <= 14:
            n_select = 5
            stages.append(
                [[number_list[i], randlang(2), pos_list[i]] for i in range(n_select)]
            )
        elif STAGE.current_level <= 16:
            n_select = 7
            stages.append(
                [[number_list[i], randlang(2), pos_list[i]] for i in range(n_select)]
            )
        elif STAGE.current_level <= LAST_STAGE:
            n_select = 7
            stages.append(
                [[number_list[i], randlang(3), pos_list[i]] for i in range(n_select)]
            )
    def start():
        om.clear_gaze_deque()
        STAGE.started = True
        if STAGE.current_level <= 9:
            STAGE.answer_of_tutorial = STAGE.get_answer_of_current_level()
        else:
            STAGE.answer_of_tutorial = None
        for attribute in stages[STAGE.current_level]:
            sv.numbers.append(Number(*attribute))
        gw.add_objects(sv.numbers, 'number')
    def check_end():
        if STAGE.started and om.check_gaze():
            current_gaze = STAGE.answer_of_tutorial
            dc.add_gaze_data((om.average_x, om.average_y), current_gaze)
            STAGE.end()
    def end():
        for number in sv.numbers.copy():
            gw.remove_object(number)
        sv.cursor.save_time()
        sv.cursor.reset_time()
        STAGE.current_level += 1
        if STAGE.current_level >= 10:
            STAGE.add_stage()
        if STAGE.current_level > LAST_STAGE:
            dc.save_data()
            gf.change_state('gaze_check_state', None)
        else:
            STAGE.start()