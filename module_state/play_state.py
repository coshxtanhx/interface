from pico2d import *
from module_system.event_table import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw
from module_object.background import Background
from module_object.number import Number
from module_object.information import Information
import module_system.opencv_manager as om
import module_system.stage_manager as sm

def handle_events():
    events = get_events()
    for raw_event in events:
        event = convert_event(raw_event)
        if event == QUIT:
            gf.change_state('', None)
        elif event == KESCD:
            gf.change_state('', None)

def enter():
    sv.background = Background()
    sv.information.append(Information('play'))
    sv.information.append(Information('exit'))
    sv.information.append(Information('start'))
    gw.add_objects(sv.numbers, 'number')
    gw.add_object(sv.background, 'bg')
    gw.add_objects(sv.information, 'ui')

def exit():
    gw.clear_world()

def draw_all():
    clear_canvas()
    for objs in gw.all_objects():
        objs.draw()
    update_canvas()

def update():
    for objs in gw.all_objects_copy():
        objs.update()
    if om.check_gaze():
        sm.STAGE.end()