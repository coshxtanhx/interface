from pico2d import *
from module_other.coordinates import *
from module_system.event_table import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw
import module_system.opencv_manager as om
from module_object.background import Background
from module_object.quiz import Quiz
from module_object.gazecursor import GazeCursor
import module_system.main_stage_manager as msm
import module_system.data_collector as dc

def handle_events():
    events = get_events()
    for raw_event in events:
        event = convert_event(raw_event)
        if event == QUIT:
            gf.change_state('', None)
        elif event == KESCD:
            gf.change_state('', None)

def enter():
    dc.register_pos()
    om.GAZE_DETECT_TIMER = 0.03
    sv.background = Background()
    sv.cursor = GazeCursor()
    gw.add_object(sv.background, 'bg')
    gw.add_object(sv.cursor, 'ui')
    msm.STAGE.start()

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
    # msm.STAGE.check_end()