from pickle import *

UI_WIDTH, UI_HEIGHT = 1120, 640

EXTRA_PIXEL = 70

POS_RANGE = range(1, 10)
LEFT_TOP, TOP, RIGHT_TOP, LEFT, CENTER, RIGHT, LEFT_BOTTOM, \
    BOTTOM, RIGHT_BOTTOM, CENTER_LEFT, CENTER_RIGHT = range(1, 12)

POS_WITHOUT_CENTER_TUPLE = (LEFT_TOP, TOP, RIGHT_TOP, LEFT,
                            RIGHT, LEFT_BOTTOM, BOTTOM, RIGHT_BOTTOM)

POS_STR = {
    CENTER: '중앙',
    LEFT_TOP: '좌측 상단',
    LEFT_BOTTOM: '좌측 하단',
    LEFT: '좌측',
    RIGHT_TOP: '우측 상단',
    RIGHT_BOTTOM: '우측 하단',
    RIGHT: '우측',
    TOP: '상단',
    BOTTOM: '하단',
}

POS_NUMBER = {
    CENTER: (UI_WIDTH // 2, UI_HEIGHT // 2),
    LEFT_TOP: (EXTRA_PIXEL, UI_HEIGHT - EXTRA_PIXEL),
    LEFT_BOTTOM: (EXTRA_PIXEL, EXTRA_PIXEL),
    LEFT: (EXTRA_PIXEL, UI_HEIGHT // 2),
    RIGHT_TOP: (UI_WIDTH - EXTRA_PIXEL, UI_HEIGHT - EXTRA_PIXEL),
    RIGHT_BOTTOM: (UI_WIDTH - EXTRA_PIXEL, EXTRA_PIXEL),
    RIGHT: (UI_WIDTH - EXTRA_PIXEL, UI_HEIGHT // 2),
    TOP: (UI_WIDTH // 2, UI_HEIGHT - EXTRA_PIXEL),
    BOTTOM: (UI_WIDTH // 2, EXTRA_PIXEL),
    CENTER_LEFT: (UI_WIDTH // 2 - 200, UI_HEIGHT // 2),
    CENTER_RIGHT: (UI_WIDTH // 2 + 200, UI_HEIGHT // 2),
}

VECTOR_IN_CANVAS = {
    LEFT_TOP: (-UI_WIDTH // 2, UI_HEIGHT // 2),
    LEFT_BOTTOM: (-UI_WIDTH // 2, -UI_HEIGHT // 2),
    LEFT: (-UI_WIDTH // 2, 0),
    RIGHT_TOP: (UI_WIDTH // 2, UI_HEIGHT // 2),
    RIGHT_BOTTOM: (UI_WIDTH // 2, -UI_HEIGHT // 2),
    RIGHT: (UI_WIDTH // 2, 0),
    TOP: (0, UI_HEIGHT // 2),
    BOTTOM: (0, UI_HEIGHT // -2),
}

def correct_pos(original_pos, length, lang='아라비아'):
    if lang == '아라비아':
        original_pos[0] -= 12 * length
    else:
        original_pos[0] -= 13 * length

def convert_pos_to_vector(pos_xy):
    import module_system.data_collector as dc
    x, y = pos_xy
    vector_x = x - dc.user_gaze_data[CENTER][0]
    vector_y = y - dc.user_gaze_data[CENTER][1]
    return vector_x, vector_y

def convert_pos(x, y):
    import module_system.data_collector as dc
    gaze_vector_x, gaze_vector_y = convert_pos_to_vector((x, y))
    rate_a, rate_b = None, None
    for a, b in ((TOP, RIGHT_TOP), (RIGHT_TOP, RIGHT), (RIGHT, RIGHT_BOTTOM),
                (RIGHT_BOTTOM, BOTTOM), (BOTTOM, LEFT_BOTTOM), (LEFT_BOTTOM, LEFT),
                (LEFT, LEFT_TOP), (LEFT_TOP, TOP)):
        vector_a = convert_pos_to_vector(dc.user_gaze_data[a])
        vector_b = convert_pos_to_vector(dc.user_gaze_data[b])

        if (vector_b[1] * vector_a[0] - vector_b[0] * vector_a[1]) == 0.0:
            break

        rate_a = (gaze_vector_x * vector_b[1] - gaze_vector_y * vector_b[0]) \
            / (vector_b[1] * vector_a[0] - vector_b[0] * vector_a[1])
        rate_b = (gaze_vector_x * vector_a[1] - gaze_vector_y * vector_a[0]) \
            / (-vector_b[1] * vector_a[0] + vector_b[0] * vector_a[1])

        if rate_a >= 0 and rate_b >= 0:
            #print(rate_a, rate_b)
            converted_gaze_x = rate_a * VECTOR_IN_CANVAS[a][0] \
                + rate_b * VECTOR_IN_CANVAS[b][0] + UI_WIDTH // 2
            converted_gaze_y = rate_a * VECTOR_IN_CANVAS[a][1] \
                + rate_b * VECTOR_IN_CANVAS[b][1] + UI_HEIGHT // 2
            
            return (converted_gaze_x, converted_gaze_y)
        
    return (0, 0)