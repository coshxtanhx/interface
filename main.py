import pico2d
import cv2 as cv
from module_other.coordinates import *
import module_system.game_framework as gf
import module_system.opencv_manager as om
from module_object.quiz import Quiz

Quiz(7)

exit()

om.activate_opencv()
pico2d.open_canvas(UI_WIDTH, UI_HEIGHT)

gf.activate_game_framework('gaze_check_state')

om.capture.release()
pico2d.close_canvas()
cv.destroyAllWindows()