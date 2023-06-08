from random import *
from math import *
from module_other.coordinates import *
import module_system.soundfile_manager as sfm
import module_system.opencv_manager as om
import pickle

class GazePosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def __add__(self, other):
        return GazePosition(self.x + other.x, self.y + other.y)
    def __floordiv__(self, n):
        return GazePosition(int(self.x // n), int(self.y // n))

gaze_dict = {
    CENTER: [],
    LEFT_TOP: [],
    LEFT_BOTTOM: [],
    LEFT: [],
    RIGHT_TOP: [],
    RIGHT_BOTTOM: [],
    RIGHT: [],
    TOP: [],
    BOTTOM: []
}

user_gaze_data = {
    CENTER: None,
    LEFT_TOP: None,
    LEFT_BOTTOM: None,
    LEFT: None,
    RIGHT_TOP: None,
    RIGHT_BOTTOM: None,
    RIGHT: None,
    TOP: None,
    BOTTOM: None
}

user_cursor_time_data = {
    '정답여부': [None] * 10,
    '암산시간':[None] * 10,
    '필산시간': [None] * 10,
    '입력시간': [None] * 10
}

def register_pos():
    try:
        file = open('data/eight_direction.sav', 'rb')
    except:
        print('ERROR')
        exit()
    data = load(file)
    file.close()
    for pos in POS_RANGE:
        user_gaze_data[pos] = (data[pos].x, data[pos].y)

def save_data():
    for pos in POS_RANGE:
        sum_of_data = GazePosition(0, 0)
        data_len = len(gaze_dict[pos])
        for data in gaze_dict[pos]:
            sum_of_data += data
        user_gaze_data[pos] = sum_of_data // data_len
        gaze_dict[pos] = []

    file = open('data/eight_direction.sav', 'wb')
    pickle.dump(user_gaze_data, file)
    file.close()

    file = open('data/gaze_list.sav', 'wb')
    pickle.dump((list(om.whole_gaze_x_deque), list(om.whole_gaze_y_deque)), file)
    file.close()

    sfm.sound_effect.play(sfm.SE_COMPLETED)

def guess_gaze(xy_pos):
    min_distance = float('inf')
    closest_pos = None
    gaze = GazePosition(*xy_pos)
    for pos in POS_RANGE:
        distance = gaze.get_distance(gaze_dict[pos][0])
        if distance < min_distance:
            min_distance = distance
            closest_pos = pos
    return closest_pos

def add_gaze_data(xy_pos, pos = None):
    if not pos:
        pos = guess_gaze(xy_pos)
    data = GazePosition(xy_pos[0], xy_pos[1])
    gaze_dict[pos].append(data)

def save_cursor_time(level, is_correct, in_screen_center_time,
                     in_screen_time, out_screen_time):
    user_cursor_time_data['정답여부'][level-1] = is_correct
    user_cursor_time_data['암산시간'][level-1] = in_screen_center_time
    user_cursor_time_data['입력시간'][level-1] = in_screen_time
    user_cursor_time_data['필산시간'][level-1] = out_screen_time