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
        removed_bul = False
        for bullet in bullets:
            for brick in bricks:
                bullet_body = bullet.get_body()
                brick_body = brick.get_body()

                if self._physics_service.has_collided(bullet_body, brick_body):
                    # bullet.bounce_y()
                    # sound = Sound(BOUNCE_SOUND)
                    # self._audio_service.play_sound(sound)
                    # stats.add_points(points)
                    cast.remove_actor(BRICKS_GROUP, brick)
                    removed_bul = True
            if removed_bul == True:
                cast.remove_actor(BULLET_GROUP, bullet)
            removed_bul = False
        bullets = cast.get_actors(BULLET_GROUP)
        bricks = cast.get_actors(BRICKS_GROUP)
        for brick in bricks:
            for bullet in bullets:
                bullet_body = bullet.get_body()
                brick_body = brick.get_body()

                if self._physics_service.has_collided(bullet_body, brick_body):
                    # bullet.bounce_y()
                    # sound = Sound(BOUNCE_SOUND)
                    # self._audio_service.play_sound(sound)
                    # stats.add_points(points)
                    cast.remove_actor(BULLET_GROUP, bullet)
            #         removed_bul = True
            # if removed_bul == True:
            #     cast.remove_actor(BRICKS_GROUP, bricks)
            # removed_bul = False
            
                    
        for tank in tanks:
            for brick in bricks:
                tank_body = tank.get_body()
                brick_body = brick.get_body()

                if self._physics_service.has_collided(tank_body, brick_body):
                    tank.stop_moving(wall=True)
