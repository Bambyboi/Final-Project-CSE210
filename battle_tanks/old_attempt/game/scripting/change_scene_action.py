from constants import *
from game.scripting.action import Action
# from game.scripting.collide_tank_action import CollideTankAction


class ChangeSceneAction(Action):

    def __init__(self, keyboard_service, next_scene):
        self._keyboard_service = keyboard_service
        self._next_scene = next_scene
        
    def execute(self, cast, script, callback):
        if self._keyboard_service.is_key_pressed(ENTER):
            callback.on_next(self._next_scene)
        # tanks = cast.get_actors(TANKS_GROUP)
        # for tank in tanks:
            
        #         callback.on_next(self._next_scene)