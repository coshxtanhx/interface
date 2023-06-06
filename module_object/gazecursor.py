from pico2d import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.opencv_manager as om
from module_object.cursor import Cursor
import module_system.main_stage_manager as msm
import module_system.data_collector as dc

# 기존 Cursor 클래스를 상속받은 GazeCursor 클래스 정의
class GazeCursor(Cursor):
    IN_SCREEN_TIME_THRESHOLD = 0.1
    OUT_SCREEN_TIME_THRESHOLD = 0.1

    def __init__(self):
        super().__init__()
        self.in_screen_time = 0  # 화면 안에 있는 시간
        self.out_screen_time = 0  # 화면 밖에 있는 시간
        self.in_screen = False  # 현재 화면 안에 있는지 여부

    def update(self):
        super().update()

        # 커서가 화면 안에 있는지 여부 체크
        if self.is_in_screen():
            self.in_screen = True
            self.in_screen_time += om.GAZE_DETECT_TIMER

        else:
            self.in_screen = False

            self.out_screen_time += om.GAZE_DETECT_TIMER

    def is_in_screen(self):
        # 커서가 화면 안에 있는지 여부 반환
        screen_width, screen_height = get_canvas_width(), get_canvas_height()
        return 0 <= self.x <= screen_width and 0 <= self.y <= screen_height

    def save_time(self):
        # 화면 안에 있는 시간과 화면 밖을 보는 시간 저장
        current_gaze = msm.STAGE.current_level
        dc.save_cursor_time(current_gaze, self.in_screen_time, self.out_screen_time)

