import pickle
from module_other.coordinates import *

try:
    file = open('data/eight_direction.sav', 'rb')
except:
    input('ERROR')
    exit()
data = pickle.load(file)

file.close()

for pos in POS_RANGE:
    print(POS_STR[pos] + ':', (data[pos].x, data[pos].y))