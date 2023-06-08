from random import *
from module_object.number import Number
from module_other.coordinates import *
from module_system.debug_manager import *
from module_object.quiz import Quiz
import module_system.server as sv
import module_system.game_world as gw
import module_system.opencv_manager as om
import module_system.game_framework as gf
import module_system.data_collector as dc
import module_system.soundfile_manager as sfm

locations = list(POS_RANGE)

LAST_STAGE = 10

lang_type = ['아라비아', '한자어', '순우리말']

def randlang(n=3):
    return choice(lang_type[0:n])

class STAGE:
    started = False
    current_level = 1
    answer = None
    users_choice = LEFT_BOTTOM # 임의의 초깃값
    def create_quiz_and_numbers():
        pos_list = list(POS_WITHOUT_CENTER_TUPLE)
        pos_list.remove(STAGE.users_choice)
        shuffle(pos_list)
        answer_list = None
        sv.quiz = Quiz(STAGE.current_level)
        STAGE.answer = sv.quiz.answer
        gw.add_object(sv.quiz, 'number')
        if STAGE.answer <= 3:
            answer_list = [1,2,3,4,5]
        elif STAGE.answer >= 97:
            answer_list = [95,96,97,98,99]
        else:
            answer_list = [i for i in range(STAGE.answer - 2, STAGE.answer + 3)]
        for i in range(5):
            sv.numbers.append(Number(answer_list[i], randlang(), pos_list[i],
                              answer_list[i] == STAGE.answer))
        gw.add_objects(sv.numbers, 'number')
    def start():
        om.clear_gaze_deque()
        STAGE.started = True
        om.is_camera_activated = True
        STAGE.create_quiz_and_numbers()
    # def check_end():
    #     if STAGE.started and om.check_gaze():
    #         STAGE.end()
    def end():
        for number in sv.numbers.copy():
            gw.remove_object(number)
        gw.remove_object(sv.quiz)
        sv.cursor.save_time()
        sv.cursor.reset_time()
        STAGE.current_level += 1
        STAGE.started = False
        om.is_camera_activated = False
        sfm.sound_effect.play(choice(sfm.SE_GAZE_CHECK))
        if STAGE.current_level > LAST_STAGE:
            gf.change_state('analysis_check_state', None)
        else:
            STAGE.start()