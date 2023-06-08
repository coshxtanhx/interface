from pico2d import *
from module_other.coordinates import *
import module_system.server as sv

class AnalysisFrame:
    image = None
    image_arrow = [None, None]
    def __init__(self):
        if not AnalysisFrame.image:
            AnalysisFrame.image = load_image('images/graph5x2.png')
            AnalysisFrame.image_arrow[0] = load_image('images/arrow_left.png')
            AnalysisFrame.image_arrow[1] = load_image('images/arrow_right.png')
    def draw(self):
        self.image.draw(UI_WIDTH//2, UI_HEIGHT//2)
        self.image_arrow[0].draw(UI_WIDTH//5, UI_HEIGHT//2)
        self.image_arrow[1].draw(UI_WIDTH//5 * 4, UI_HEIGHT//2)
    def update(self):
        pass
    def delete_from_server(self):
        sv.analysis_frame = None