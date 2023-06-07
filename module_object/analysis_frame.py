from pico2d import *
from module_other.coordinates import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw

class AnalysisFrame:
    image = None
    def __init__(self):
        if not AnalysisFrame.image:
            AnalysisFrame.image = load_image('images/cursor.png')
    def draw(self):
        self.image.draw(UI_WIDTH//2, UI_HEIGHT//2)
    def update(self):
        pass
    def delete_from_server(self):
        sv.analysis_frame = None