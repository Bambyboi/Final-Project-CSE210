from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICKS_GROUP)
        if len(bricks) == 0:
            stats = cast.get_first_actor(STATS_GROUP)
            # stats.add_points(1)
            callback.on_next(NEXT_ROUND)