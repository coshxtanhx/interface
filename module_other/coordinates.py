UI_WIDTH, UI_HEIGHT = 1120, 640

EXTRA_PIXEL = 50

X, Y = 0, 1

POS_RANGE = range(1, 10)
CENTER, LEFT_TOP, LEFT_BOTTOM, LEFT, RIGHT_TOP, RIGHT_BOTTOM,\
RIGHT, TOP, BOTTOM, CENTER_LEFT, CENTER_RIGHT = range(1, 12)

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

def correct_pos(original_pos, length, lang):
    if lang == '아라비아':
        for i in range(1, 3):
            if length == i:
                original_pos[X] -= 10 * i
    else:
        for i in range(1, 5):
            if length == i:
                original_pos[X] -= 16 * i