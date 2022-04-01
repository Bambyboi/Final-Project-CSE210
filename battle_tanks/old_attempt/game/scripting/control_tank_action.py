from constants import *
from game.scripting.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        for i in range(NUMBER_OF_PLAYERS):
            if i == 0:
                tank = cast.get_nth_actor(TANKS_GROUP, i)
                if self._keyboard_service.is_key_down(P1_UP): 
                    tank.drive_forward()
                elif self._keyboard_service.is_key_down(P1_DOWN): 
                    tank.drive_backward()  
                elif self._keyboard_service.is_key_down(P1_LEFT):
                    tank.turn_left()
                elif self._keyboard_service.is_key_down(P1_RIGHT):
                    tank.turn_right()
                else: 
                    tank.stop_moving()  
            elif i == 1:
                tank = cast.get_nth_actor(TANKS_GROUP, i)
                if self._keyboard_service.is_key_down(P2_UP): 
                    tank.drive_forward()
                elif self._keyboard_service.is_key_down(P2_DOWN): 
                    tank.drive_backward()  
                elif self._keyboard_service.is_key_down(P2_LEFT):
                      tank.turn_left()
                elif self._keyboard_service.is_key_down(P2_RIGHT):
                    tank.turn_right()
                else: 
                    tank.stop_moving()     
                    
    