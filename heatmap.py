import matplotlib.pyplot as plt
import numpy as np
import interface.module_system.opencv_manager as om

# x, y 값 지정
x = om.gaze_x_deque
y = om.gaze_y_deque

# x, y 값에 해당하는 히트맵 데이터 생성
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(5, 5))

# 히트맵 그리기
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='coolwarm')
plt.colorbar()
plt.show()