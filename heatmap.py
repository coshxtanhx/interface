import matplotlib.pyplot as plt
import numpy as np
import pickle

try:
    file = open('data/gaze_list.sav', 'rb')
except:
    input('ERROR')
    exit()
data = pickle.load(file)

file.close()

# x, y 값 지정
x = [-i for i in data[0]]
y = [-i for i in data[1]]

# x, y 값에 해당하는 히트맵 데이터 생성
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(5, 5))

# 히트맵 그리기
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='coolwarm')
plt.colorbar()
plt.show()