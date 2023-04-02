import pico2d
import cv2 as cv
import numpy as np
import mediapipe as mp
from module_other.coordinates import *
import module_system.game_framework as gf
import module_system.opencv_manager as om

ret, frame = om.capture.read()
cv.imshow('Camera', frame)

pico2d.open_canvas(UI_WIDTH, UI_HEIGHT)
gf.activate_game_framework('play_state')

om.capture.release()
cv.destroyAllWindows()