import pickle
from module_other.coordinates import *

file = open('data/save_data.sav', 'rb')
data = pickle.load(file)

for pos in POS_RANGE:
    print(POS_STR[pos], ':', (data[pos].x, data[pos].y))

input('Press any key to quit.')