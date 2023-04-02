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

current_gaze = deque([], maxlen=30)

def activate_opencv():
    global capture, mp_face_mesh
    capture = cv.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh