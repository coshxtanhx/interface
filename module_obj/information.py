from pico2d import *
from module_other.coordinates import *
import module_system.server as sv

class Information:
    image = None
    def __init__(self):
        if Information.image == None:
            Information.image = load_image('images/information.png')
    def draw(self):
        self.image.draw(UI_WIDTH//2, UI_HEIGHT//2 + 160)
    def update(self):
        pass
    def delete_from_server(self):
        sv.information = None