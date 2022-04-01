from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        body = bullet.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT:
            bullet.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BULLET_WIDTH):
            bullet.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            bullet.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BULLET_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            
            if stats.get_score() < 5:
                callback.on_next(WINNER) 
            else:
                callback.on_next(NEXT_ROUND)
                self._audio_service.play_sound(over_sound)

    #def collide_borders(self, cast):
    #    "collision of each tanks when it hits to the borders."

    #    #if 
        tanks = cast.get_actors(TANKS_GROUP)
        borders_top = cast.get_actors(FIELD_TOP)
        borders_bottom = cast.get_actors(FIELD_BOTTOM)
        borders_left = cast.get_actors(FIELD_LEFT)
        borders_right = cast.get_actors(FIELD_RIGHT)


        for i in range(len(tanks)):
            tank = cast.get_nth_actor(TANKS_GROUP, i)
            for border_top in borders_top:
                tank_body = tank.get_body()
                border_top_body = border_top.get_body()

                if self._physics_service.has_collided(tank_body, border_top_body):
                    tank.stop_moving(wall=True)

            for border_bottom in borders_bottom:
                tank_body = tank.get_body()
                border_bottom_body = border_bottom.get_body()

                if self._physics_service.has_collided(tank_body, border_bottom_body):
                    tank.stop_moving(wall=True)

            for border_left in borders_left:
                tank_body = tank.get_body()
                border_left_body = border_left.get_body()

                if self._physics_service.has_collided(tank_body, border_left_body):
                    tank.stop_moving(wall=True)

            for border_right in borders_right:
                tank_body = tank.get_body()
                border_right_body = border_right.get_body()

                if self._physics_service.has_collided(tank_body, border_right_body):
                    tank.stop_moving(wall=True)



           # for brick in bricks:
           #         tank_body = tank.get_body()
           #         brick_body = brick.get_body()

           #         if self._physics_service.has_collided(tank_body, brick_body):
           #             tank.stop_moving(wall=True)