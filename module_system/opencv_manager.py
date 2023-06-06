import cv2 as cv
import numpy as np
import mediapipe as mp
from collections import deque
from random import choice

LEFT_EYE = [ 362,382,381,380,374,373,390,249,263,466,388,387,386,385,384,398 ]
RIGHT_EYE = [ 33,7,163,144,145,153,154,155,133,173,157,158,159,160,161,246 ]

LEFT_IRIS = [ 474,475,476,477 ]
RIGHT_IRIS = [ 469,470,471,472 ]

capture = None
mp_face_mesh = None

GAZE_TIMER = 2.0
GAZE_DETECT_TIMER = 0.1
DEQUE_SIZE = int(GAZE_TIMER * 10)
WHOLE_DEQUE_SIZE = 2000

PRECISION_X = 30.0
PRECISION_Y = 3.15

gaze_x_deque = deque([], maxlen=DEQUE_SIZE)
gaze_y_deque = deque([], maxlen=DEQUE_SIZE)

whole_gaze_x_deque = deque([], maxlen=WHOLE_DEQUE_SIZE)
whole_gaze_y_deque = deque([], maxlen=WHOLE_DEQUE_SIZE)

accumulated_time = 0.0

average_x = 0
average_y = 0

def activate_opencv():
    global capture, mp_face_mesh
    capture = cv.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh

def add_gaze_to_deque(x, y, t):
    global accumulated_time
    accumulated_time += t
    if accumulated_time >= GAZE_DETECT_TIMER:
        accumulated_time -= GAZE_DETECT_TIMER
        gaze_x_deque.append(x)
        gaze_y_deque.append(y)

        whole_gaze_x_deque.append(x)
        whole_gaze_y_deque.append(y)

def clear_gaze_deque():
    global accumulated_time, gaze_x_deque, gaze_y_deque
    accumulated_time = 0.0
    gaze_x_deque = deque([], maxlen=DEQUE_SIZE)
    gaze_y_deque = deque([], maxlen=DEQUE_SIZE)

def check_gaze():
    global average_x, average_y
    if len(gaze_x_deque) != DEQUE_SIZE:
        return False
    average_x = sum(gaze_x_deque) / DEQUE_SIZE
    average_y = sum(gaze_y_deque) / DEQUE_SIZE

    v = 0
    for gaze in gaze_x_deque:
        v += (gaze - average_x) ** 2
    v /= DEQUE_SIZE
    if v > PRECISION_X:
        return False
    
    for gaze in gaze_y_deque:
        v += (gaze - average_y) ** 2
    v /= DEQUE_SIZE
    if v > PRECISION_Y:
        return False
    
    return True