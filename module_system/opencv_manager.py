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

def run_opencv():
    with mp_face_mesh.FaceMesh(max_num_faces = 1,
        refine_landmarks = True,
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5,
    ) as face_mesh:
        ret, frame = capture.read()
        if not ret:
            return
        if capture.get(cv.CAP_PROP_POS_FRAMES) == capture.get(cv.CAP_PROP_FRAME_COUNT):
            capture.set(cv.CAP_PROP_POS_FRAMES, 0)
        img_h, img_w = frame.shape[:2]
        results = face_mesh.process(frame)
        if results.multi_face_landmarks:
            mesh_points = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int)
                                   for p in results.multi_face_landmarks[0].landmark])
            (l_cx, l_cy), l_rad = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
            (r_cx, r_cy), r_rad = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            l_center = np.array([l_cx, l_cy], dtype=np.int32)
            r_center = np.array([r_cx, r_cy], dtype=np.int32)
            l_and_r_center = (l_center[0] + r_center[0], l_center[1] + r_center[1])
            current_gaze.append(l_and_r_center)

        #cv.imshow('Camera', frame)