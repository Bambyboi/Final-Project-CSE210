from constants import *
from game.scripting.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        for i in range(2):
            tank = cast.get_nth_actor(TANKS_GROUP, i)
            if self._keyboard_service.is_key_down(P1_LEFT): 
                tank.swing_left()
            elif self._keyboard_service.is_key_down(P1_RIGHT): 
                tank.swing_right()  
            else: 
                tank.stop_moving()        