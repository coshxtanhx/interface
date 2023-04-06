import numpy as np
import matplotlib.pyplot as plt
import module_system.opencv_manager as om
from collections import deque

def handle_events():
    pass

def enter():
    pass

def exit():
    pass

def draw_all():
    x = list(om.gaze_x_deque)
    y = list(om.gaze_y_deque)

    # x, y 값에 해당하는 히트맵 데이터 생성
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=(5, 5))

    # 히트맵 그리기
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='coolwarm')
    plt.colorbar()
    plt.show()

def update():
    pass