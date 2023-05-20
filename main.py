import pico2d
import cv2 as cv
from module_other.coordinates import *
import module_system.game_framework as gf
import module_system.opencv_manager as om

om.activate_opencv()
pico2d.open_canvas(UI_WIDTH, UI_HEIGHT)

gf.activate_game_framework('play_state')

om.capture.release()
pico2d.close_canvas()
cv.destroyAllWindows()