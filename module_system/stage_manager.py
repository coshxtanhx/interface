from random import *
from module_object.number import Number
from module_other.coordinates import *
from module_system.debug_manager import *
import module_system.server as sv
import module_system.game_world as gw
import module_system.opencv_manager as om

STAGES = [
    None,
    [
    [randint(8,9), '아라비아', CENTER],
    [randint(1,2), '아라비아', CENTER_RIGHT],
    [randint(3,4), '아라비아', CENTER_LEFT]
    ],
    [
    [randint(28,59), '아라비아', CENTER],
    [randint(1,6), '아라비아', RIGHT],
    [randint(10,14), '아라비아', LEFT]
    ]
]

class STAGE:
    current_level = 1
    def start():
        for attribute in STAGES[STAGE.current_level]:
            sv.numbers.append(Number(*attribute))
        gw.add_objects(sv.numbers, 'number')
    def end():
        for number in sv.numbers.copy():
            gw.remove_object(number)
        STAGE.current_level += 1
        STAGE.start()