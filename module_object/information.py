from pico2d import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw
from module_object.number import Number

debug_mode = 0

class Information:
    image = dict()
    def __init__(self, type):
        if not Information.image:
            Information.image['play'] = load_image('images/information_how_to_play.png')
            Information.image['exit'] = load_image('images/information_how_to_exit.png')
            Information.image['start'] = \
                [load_image('images/information_auto_start_%d.png' % i) for i in range(1, 6)]
        self.type = type
        self.image = Information.image[self.type]
        self.time_remain = 0.1 if debug_mode else 4.999
    def draw(self):
        if self.type == 'play':
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 + 160)
        elif self.type == 'exit':
            self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 - 160)
        elif self.type == 'start':
            self.image[int(self.time_remain)].draw(UI_WIDTH//2, UI_HEIGHT//2)
    def update(self):
        if self.type == 'start':
            if self.time_remain > 0.0:
                self.time_remain -= gf.elapsed_time
            elif self.time_remain <= 0.0:
                gw.remove_object(self)
                gw.add_object(Number(5, '아라비아'), 'number')
    def delete_from_server(self):
        sv.information = None