from constants import *
from game.scripting.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        for i in range(2):
            if i == 1:
                tank = cast.get_nth_actor(TANKS_GROUP, 0)
                if self._keyboard_service.is_key_down(P1_UP): 
                    tank.drive_forward()
                elif self._keyboard_service.is_key_down(P1_DOWN): 
                    tank.drive_backward()  
                else: 
                    tank.stop_moving()  
            elif i == 2:
                tank = cast.get_nth_actor(TANKS_GROUP, 1)
                if self._keyboard_service.is_key_down(P2_UP): 
                    tank.drive_forward()
                elif self._keyboard_service.is_key_down(P2_DOWN): 
                    tank.drive_backward()  
                else: 
                    tank.stop_moving()     