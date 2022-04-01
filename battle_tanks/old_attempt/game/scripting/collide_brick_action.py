from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        bullets = cast.get_actors(BULLET_GROUP)
        bricks = cast.get_actors(BRICKS_GROUP)
        tanks = cast.get_actors(TANKS_GROUP)
        # stats = cast.get_first_actor(STATS_GROUP)

        for i in range(len(bullets)):
            bullet = cast.get_nth_actor(BULLET_GROUP, i)
            for brick in bricks:
                bullet_body = bullet.get_body()
                brick_body = brick.get_body()

                if self._physics_service.has_collided(brick_body, bullet_body):
                    # bullet.bounce_y()
                    # sound = Sound(BOUNCE_SOUND)
                    # self._audio_service.play_sound(sound)
                    # points = brick.get_points()
                    # stats.add_points(points)
                    cast.remove_actor(BRICKS_GROUP, brick)
        for j in range(len(tanks)):
            tank = cast.get_nth_actor(TANKS_GROUP, j)
            for brick in bricks:
                tank_body = tank.get_body()
                brick_body = brick.get_body()

                if self._physics_service.has_collided(tank_body, brick_body):
                    tank.stop_moving(wall=True)
