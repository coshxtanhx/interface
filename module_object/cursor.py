from pico2d import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.opencv_manager as om

class Cursor:
    image = None
    def __init__(self):
        self.x = -1
        self.y = -1
        if not Cursor.image:
            Cursor.image = load_image('images/cursor.png')
    def draw(self):
        self.image.draw(self.x + 12, self.y - 20)
    def update(self):
        if om.gaze_x_deque:
            self.x, self.y = convert_pos(om.average_x, om.average_y)
            self.x, self.y = round(self.x), round(self.y)
    def delete_from_server(self):
        sv.cursor = None

    def reset_time(self):
        self.in_screen_time = 0
        self.out_screen_time = 0
        self.in_screen_center_time = 0