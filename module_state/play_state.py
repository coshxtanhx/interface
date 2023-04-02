from pico2d import *
from module_system.event_table import *
import module_system.server as sv
import module_system.game_framework as gf
import module_system.game_world as gw
from module_obj.background import Background
from module_obj.number import Number

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
    gw.add_object(sv.background, 'bg')

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