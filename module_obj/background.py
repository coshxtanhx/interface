from pico2d import *
from module_other.coordinates import *
import module_system.server as sv

class Background:
    image = None
    def __init__(self):
        if Background.image == None:
            Background.image = load_image('images/background.png')
    def draw(self):
        self.image.draw(UI_WIDTH//2, UI_HEIGHT//2)
    def update(self):
        pass
    def delete_from_server(self):
        sv.background = None