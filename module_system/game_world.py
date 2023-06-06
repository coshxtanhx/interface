import module_system.server as sv

DEPTH_DICT = dict()
obj_list = [
    'bg', 'number', 'ui'
]
obj_list_len = len(obj_list)

cnt = 0
for obj_name in obj_list:
    DEPTH_DICT[obj_name] = cnt
    cnt += 1

world = dict()
cur_world = None

state_list = [
    'play_state', 'gaze_check_state', 'play_state_2'
]

for state_name in state_list:
    world[state_name] = [[] for _ in range(obj_list_len)]

def all_objects():
    for layer in world[cur_world]:
        for o in layer:
            yield o

def all_objects_copy():
    for layer in world[cur_world]:
        for o in layer.copy():
            yield o

def add_object(o, depth):
    if type(depth) == int:
        depth = obj_list[depth]
    world[cur_world][DEPTH_DICT[depth]].append(o)

def add_objects(ol, depth):
    if type(depth) == int:
        depth = obj_list[depth]
    world[cur_world][DEPTH_DICT[depth]] += ol

def clear_world():
    for layer in world[cur_world]:
        layer.clear()
        sv.clear_server()
    #if cur_world == 'play_state':
    #    sv.clear_server()

def remove_object(o):
    for layer in world[cur_world]:
        if o in layer:
            layer.remove(o)
            #del(o)
            o.delete_from_server()
            return

def pop_object(depth):
    remove_object(world[cur_world][DEPTH_DICT[depth]][-1])