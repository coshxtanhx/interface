from pico2d import *
from random import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw
from module_system.debug_manager import *
import module_system.stage_manager as sm

class Information:
    image = dict()
    def __init__(self, type):
        if not Information.image:
            Information.image['play'] = load_image('images/information_how_to_play.png')
            Information.image['exit'] = load_image('images/information_how_to_exit.png')
            Information.image['start'] = \
                [load_image('images/information_auto_start_%d.png' % i) for i in range(1, 6)]
            Information.image['tutorial'] = load_image('images/tutorial.png')
            Information.image['check'] = load_image('images/information_please_check.png')
            Information.image['error'] = load_image('images/information_error.png')
            Information.image['end'] = load_image('images/information_end.png')
            Information.image['result'] = load_image('images/information_result.png')
        self.type = type
        self.image = Information.image[self.type]
        self.time_remain = 0.1 if debug_mode else 4.999
    def draw(self):
        if self.type == 'play':
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 + 160)
            if sm.STAGE.current_level <= 9:
                Information.image['tutorial'].draw(UI_WIDTH // 2, UI_HEIGHT // 2 + 100)
        elif self.type == 'exit':
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 - 160)
        elif self.type == 'start':
            i = int(self.time_remain)
            if i < 0: i = 0
            self.image[i].draw(UI_WIDTH//2, UI_HEIGHT//2)
        elif self.type == 'check':
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 + 90)
        elif self.type == 'error' and not sv.cursor.in_screen and sv.cursor.out_screen_time > 1.5:
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 - 220)
        elif self.type == 'end':
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 - 230)
        elif self.type == 'result':
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 + 230)
    def update(self):
        if self.type == 'start':
            if self.time_remain > 0.0:
                self.time_remain -= gf.elapsed_time
            elif self.time_remain <= 0.0:
                sm.STAGE.start()
                gw.remove_object(self)
    def delete_from_server(self):
        sv.information.remove(self)