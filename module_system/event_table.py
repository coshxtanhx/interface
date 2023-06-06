from pico2d import *

KESCD, KND, KYD,\
QUIT, *_ = range(1, 6)

EVENT_DICT = {
    #(type, key, mouse_button)
    (SDL_KEYDOWN, SDLK_ESCAPE, None): KESCD,
    (SDL_KEYDOWN, SDLK_n, None): KND,
    (SDL_KEYDOWN, SDLK_y, None): KYD,
    (SDL_QUIT, None, None): QUIT
}

def convert_event(raw_event):
    event_tuple = (raw_event.type, raw_event.key, raw_event.button)
    if(event_tuple in EVENT_DICT):
        return EVENT_DICT[event_tuple]
    else:
        False