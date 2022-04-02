from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideTankAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        for i in range(NUMBER_OF_PLAYERS):
            bullets = cast.get_actors(BULLET_GROUP)
            for bullet in bullets:
                tank = cast.get_nth_actor(TANKS_GROUP, i)
                
                bullet_body = bullet.get_body()
                tank_body = tank.get_body()

                if self._physics_service.has_collided(bullet_body, tank_body):
                    bullet.bounce_y()
                    sound = Sound(HIT_SOUND)
                    self._audio_service.play_sound(sound)
                    cast.clear_actors(TANKS_GROUP)
                    cast.clear_actors(BULLET_GROUP)
                    cast.clear_actors(BRICKS_GROUP)
                    update_score = cast.get_nth_actor(STATS_GROUP, i)
                    update_score.add_points(1)
                    callback.on_next(NEXT_ROUND)

    # def dead_tank_check(self):
    #     if self._tank_is_hit:
    #         self._tank_is_hit = False
    #         return True
    #     else:
    #         return False

