import cv2 as cv
import numpy as np
import mediapipe as mp
from collections import deque

LEFT_EYE = [ 362,382,381,380,374,373,390,249,263,466,388,387,386,385,384,398 ]
RIGHT_EYE = [ 33,7,163,144,145,153,154,155,133,173,157,158,159,160,161,246 ]

LEFT_IRIS = [ 474,475,476,477 ]
RIGHT_IRIS = [ 469,470,471,472 ]

capture = None
mp_face_mesh = None

DEQUE_SIZE = 30
PRECISION_X = 10
PRECISION_Y = 1

gaze_x_deque = deque([], maxlen=DEQUE_SIZE)
gaze_y_deque = deque([], maxlen=DEQUE_SIZE)
accumulated_time = 0.0

def activate_opencv():
    global capture, mp_face_mesh
    capture = cv.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh

def add_gaze_to_deque(x, y, t):
    global accumulated_time
    accumulated_time += t
    if accumulated_time >= 0.1:
        accumulated_time -= 0.1
        gaze_x_deque.append(x)
        gaze_y_deque.append(y)

def clear_gaze_deque():
    global accumulated_time, gaze_x_deque, gaze_y_deque
    accumulated_time = 0.0
    gaze_x_deque = deque([], maxlen=DEQUE_SIZE)
    gaze_y_deque = deque([], maxlen=DEQUE_SIZE)

def check_gaze():
    if len(gaze_x_deque) != DEQUE_SIZE:
        return False
    average_x = sum(gaze_x_deque) / DEQUE_SIZE
    average_y = sum(gaze_y_deque) / DEQUE_SIZE

    v = 0
    for gaze in gaze_x_deque:
        v += (gaze - average_x) ** 2
    v /= DEQUE_SIZE
    if v > PRECISION_X:
        print(v)
        return False
    
    for gaze in gaze_y_deque:
        v += (gaze - average_y) ** 2
    v /= DEQUE_SIZE
    if v > PRECISION_Y:
        print(v)
        return False
    
    clear_gaze_deque()
    return True