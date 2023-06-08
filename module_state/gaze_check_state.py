from pico2d import *
from module_system.event_table import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw
from module_object.background import Background
from module_object.gazecursor import GazeCursor
from module_object.information import Information
from module_other.coordinates import *
import module_system.opencv_manager as om
import module_system.data_collector as dc
import module_system.soundfile_manager as sfm

def handle_events():
    events = get_events()
    for raw_event in events:
        event = convert_event(raw_event)
        if event == QUIT:
            gf.change_state('', None)
        elif event == KESCD:
            gf.change_state('', None)
        elif event == KND:
            sfm.sound_effect.play(sfm.SE_RETRY)
            gf.change_state('play_state', None)
        elif event == KYD:
            sfm.sound_effect.play(sfm.SE_RETRY)
            gf.change_state('play_state_2', None)

def enter():
    dc.register_pos()
    om.GAZE_DETECT_TIMER = 0.03
    om.is_camera_activated = True
    sv.background = Background()
    sv.cursor = GazeCursor()
    sv.information.append(Information('error'))
    sv.information.append(Information('check'))
    gw.add_object(sv.background, 'bg')
    gw.add_objects(sv.information, 'ui')
    gw.add_object(sv.cursor, 'ui')

def exit():
    om.is_camera_activated = False
    gw.clear_world()

def draw_all():
    clear_canvas()
    for objs in gw.all_objects():
        objs.draw()
    # 화면 안에 있는 시간과 화면 밖에 있는 시간 표시 - 디버깅
    # font = load_font('font/MaruBuri-Bold.ttf', 20)
    # in_screen_time = sv.cursor.in_screen_time
    # out_screen_time = sv.cursor.out_screen_time
    # font.draw(10, 30, f'In-screen time: {in_screen_time:.2f}s', (255, 255, 255))
    # font.draw(10, 70, f'Out-screen time: {out_screen_time:.2f}s', (255, 255, 255))
    update_canvas()

def update():
    om.check_gaze()
    for objs in gw.all_objects_copy():
        objs.update()
    # 화면 안에 있는 시간과 화면 밖에 있는 시간 출력 - 디버깅
    # in_screen_time = sv.cursor.in_screen_time
    # out_screen_time = sv.cursor.out_screen_time
    # print(f'In-screen time: {in_screen_time:.2f}s')
    # print(f'Out-screen time: {out_screen_time:.2f}s')