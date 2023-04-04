import pickle
from module_other.coordinates import *

try:
    file = open('data/save_data.sav', 'rb')
except:
    input('ERROR: Press any key to quit.')
    exit()
data = pickle.load(file)

for pos in POS_RANGE:
    print(POS_STR[pos], ':', (data[pos].x, data[pos].y))

input('Press any key to quit.')