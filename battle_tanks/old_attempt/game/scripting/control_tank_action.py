from constants import *
from game.scripting.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
                tank1 = cast.get_nth_actor(TANKS_GROUP, 0)
                if self._keyboard_service.is_key_down(P1_UP): 
                    tank1.drive_forward()
                elif self._keyboard_service.is_key_down(P1_DOWN): 
                    tank1.drive_backward()  
                else: 
                    tank1.stop_moving()  

                tank2 = cast.get_nth_actor(TANKS_GROUP, 1)
                if self._keyboard_service.is_key_down(P2_UP): 
                    tank2.drive_forward()
                elif self._keyboard_service.is_key_down(P2_DOWN): 
                    tank2.drive_backward()  
                else: 
                    tank2.stop_moving()     