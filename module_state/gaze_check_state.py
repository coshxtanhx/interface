from pico2d import *
from module_system.event_table import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw
from module_object.background import Background
from module_object.gazecursor import GazeCursor
from module_other.coordinates import *
import module_system.opencv_manager as om

def handle_events():
    events = get_events()
    for raw_event in events:
        event = convert_event(raw_event)
        if event == QUIT:
            gf.change_state('', None)
        elif event == KESCD:
            gf.change_state('', None)

def enter():
    register_pos()
    om.GAZE_DETECT_TIMER = 0.03
    sv.background = Background()
    sv.cursor = GazeCursor()
    gw.add_object(sv.background, 'bg')
    gw.add_object(sv.cursor, 'ui')

def exit():
    gw.clear_world()

def draw_all():
    clear_canvas()
    for objs in gw.all_objects():
        objs.draw()
    update_canvas()

def update():
    om.check_gaze()
    for objs in gw.all_objects_copy():
        objs.update()
        # 커서의 화면 안에 있는 시간과 화면 밖에 있는 시간 출력
    print(f'In-screen time: {sv.cursor.in_screen_time:.2f}s')
    print(f'Out-screen time: {sv.cursor.out_screen_time:.2f}s')

    # 화면 안에 있는 시간과 화면 밖에 있는 시간이 임계값을 넘었을 때의 처리
    if sv.cursor.in_screen_time > GazeCursor.IN_SCREEN_TIME_THRESHOLD:
        # 화면 안에 있는 시간이 임계값을 넘었을 때의 처리
        pass

    if sv.cursor.out_screen_time > GazeCursor.OUT_SCREEN_TIME_THRESHOLD:
        # 화면 밖에 있는 시간이 임계값을 넘었을 때의 처리
        pass