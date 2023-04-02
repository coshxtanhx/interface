import module_system.opencv_manager as om
import cv2 as cv
import numpy as np
import mediapipe as mp
import module_state.play_state
from pico2d import *
import module_system.game_world as gw
from module_other.coordinates import *
from time import time

def change_state(next_module_str, next_module_option_str):
    global running, next_module, next_module_option
    running = False
    next_module, next_module_option = \
        next_module_str, next_module_option_str

def get_previous_state():
    return state_stack[-2]

def state_enter(next_module_str):
    gw.cur_world = next_module_str
    state_stack.append(next_module_str)
    eval('module_state.' + next_module_str).enter()

def state_exit(current_module_str):
    eval('module_state.' + current_module_str).exit()
    state_stack.pop()

def state_exit_all():
    for i in range(len(state_stack)-1, -1, -1):
        gw.cur_world = state_stack[i]
        eval('module_state.' + state_stack[i]).exit()
        state_stack.pop()

def state_act(next_module_str):
    gw.cur_world = next_module_str
    global running, next_module, next_module_option, elapsed_time
    running = True
    start_time = time()
    cur_module = eval('module_state.' + next_module_str)
    while(running):
        elapsed_time = time() - start_time
        start_time = time()
        
        om.run_opencv()
        
        cur_module.draw_all()
        cur_module.handle_events()
        cur_module.update()
    return next_module, next_module_option

def activate_game_framework(start_module_str):
    option = None
    next_module_str = start_module_str
    while(next_module_str != ''):
        current_module_str = next_module_str
        if(option != 'resume'):
            state_enter(next_module_str)
        next_module_str, option = state_act(next_module_str)
        if(option == 'exitall'):
            state_exit_all()
        elif(option != 'pause'):
            state_exit(current_module_str)
        if(next_module_str == 'lastest'):
            next_module_str = state_stack[-1]

state_stack = []
running = False
next_module = None
next_module_option = None
elapsed_time = 0.0