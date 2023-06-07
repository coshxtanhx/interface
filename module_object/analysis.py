from pico2d import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.data_collector as dc
from module_system.event_table import *
from module_other.color import *

class Analysis:
    font = None
    font_size = 25
    xl = UI_WIDTH // 2 - 80
    xr = UI_WIDTH // 2 + 80
    y = [UI_HEIGHT // 2 - 60 * i for i in range(-2, 3)]
    def __init__(self):
        self.stage = 1
        if not Analysis.font:
            Analysis.font = load_font('font/MaruBuri-Bold.ttf', Analysis.font_size)
    def draw(self):
        self.font.draw(self.xl, self.y[0],
                       '스테이지', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[0],
                       str(self.stage), COLOR_WHITE)
        self.font.draw(self.xl, self.y[1],
                       '정답 여부', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[1],
                       str(), COLOR_WHITE)
        self.font.draw(self.xl, self.y[2],
                       '암산 시간', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[2],
                       str(), COLOR_WHITE)
        self.font.draw(self.xl, self.y[3],
                       '필산 시간', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[3],
                       str(), COLOR_WHITE)
        self.font.draw(self.xl, self.y[4],
                       '입력 시간', COLOR_YELLOW, 'c')
        self.font.draw(self.xr, self.y[4],
                       str(), COLOR_WHITE)
    def update(self):
        pass
    def handle_events(self, event):
        if event == KAD:
            self.stage -= 1
            if self.stage == 0:
                self.stage = 10
        elif event == KDD:
            self.stage += 1
            if self.stage == 11:
                self.stage = 1
    def delete_from_server(self):
        sv.analysis = None