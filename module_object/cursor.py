from pico2d import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.opencv_manager as om

class Cursor:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if not Cursor.image:
            Cursor.image = load_image('images/cursor.png')
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        if om.gaze_x_deque:
            self.x, self.y = convert_pos(om.average_x, om.average_y)
            self.x, self.y = int(self.x), int(self.y)
    def delete_from_server(self):
        sv.background = None