from pico2d import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.data_collector as dc
from module_system.event_table import *
from module_other.color import *
import module_system.soundfile_manager as sfm

class Analysis:
    font = None
    font_size = 25
    xl = UI_WIDTH // 2 - 150
    xr = UI_WIDTH // 2 + 80
    y = [UI_HEIGHT // 2 - 64 * i for i in range(-2, 3)]
    def __init__(self):
        self.stage = 1
        if not Analysis.font:
            Analysis.font = load_font('font/MaruBuri-Bold.ttf', Analysis.font_size)
    def draw(self):
        self.font.draw(UI_WIDTH // 2, self.y[0],
                       '스테이지 %d' % self.stage, COLOR_YELLOW, 'c')
        self.font.draw(self.xl, self.y[1],
                       '정답 여부', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[1],
                       'O' if dc.user_cursor_time_data['정답여부'][self.stage-1]
                       else 'X', COLOR_WHITE, 'c')
        self.font.draw(self.xl, self.y[2],
                       '암산 시간', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[2],
                       '%0.2f초' % dc.user_cursor_time_data['암산시간'][self.stage-1],
                       COLOR_WHITE, 'c')
        self.font.draw(self.xl, self.y[3],
                       '필산 시간', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[3],
                       '%0.2f초' % dc.user_cursor_time_data['필산시간'][self.stage-1],
                       COLOR_WHITE, 'c')
        self.font.draw(self.xl, self.y[4],
                       '입력 시간', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[4],
                       '%0.2f초' % dc.user_cursor_time_data['입력시간'][self.stage-1],
                       COLOR_WHITE, 'c')
    def update(self):
        pass
    def handle_events(self, event):
        if event == KAD:
            sfm.sound_effect.play(sfm.SE_NEXT_PAGE)
            self.stage -= 1
            if self.stage == 0:
                self.stage = 10
        elif event == KDD:
            sfm.sound_effect.play(sfm.SE_NEXT_PAGE)
            self.stage += 1
            if self.stage == 11:
                self.stage = 1
    def delete_from_server(self):
        sv.analysis = None