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

    #first attempt
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
            #field top
            for border_top in borders_top:
                tank_body = tank.get_body()
                border_top_body = border_top.get_body()

                if self._physics_service.has_collided(tank_body, border_top_body):
                    tank.stop_moving(wall=True)
            #field bottom
            for border_bottom in borders_bottom:
                tank_body = tank.get_body()
                border_bottom_body = border_bottom.get_body()

                if self._physics_service.has_collided(tank_body, border_bottom_body):
                    tank.stop_moving(wall=True)
            #field left
            for border_left in borders_left:
                tank_body = tank.get_body()
                border_left_body = border_left.get_body()

                if self._physics_service.has_collided(tank_body, border_left_body):
                    tank.stop_moving(wall=True)
            #field right
            for border_right in borders_right:
                tank_body = tank.get_body()
                border_right_body = border_right.get_body()

                if self._physics_service.has_collided(tank_body, border_right_body):
                    tank.stop_moving(wall=True)





       
       
        #second attempt
        tanks = cast.get_actors(TANKS_GROUP)
        borders_top = cast.get_actors(FIELD_TOP)
        borders_bottom = cast.get_actors(FIELD_BOTTOM)
        borders_left = cast.get_actors(FIELD_LEFT)
        borders_right = cast.get_actors(FIELD_RIGHT)
        #top field
        for i in range(len(borders_top)):
            border_top = cast.get_nth_actor(FIELD_TOP, i)
            for tank in tanks:
                border_top_body = border_top.get_body()
                tank_body = tank.get_body()

                if self._physics_service.has_collide(border_top_body, tank_body):
                    cast.remove_actor(TANKS_GROUP, tank)
        
            for border_top in borders_top:
                tank_body = tank.get_body()
                border_top_body = border_top.get_body()

                if self._physics_service.has_collided(tank_body, border_top_body):
                    tank.stop_moving(wall=True)
        #bottom field
        for i in range(len(borders_bottom)):
            border_bottom = cast.get_nth_actor(FIELD_BOTTOM, i)
            for tank in tanks:
                border_bottom_body = border_bottom.get_body()
                tank_body = tank.get_body()

                if self._physics_service.has_collide(border_bottom_body, tank_body):
                    cast.remove_actor(TANKS_GROUP, tank)
        
            for border_bottom in borders_bottom:
                tank_body = tank.get_body()
                border_bottom_body = border_bottom.get_body()

                if self._physics_service.has_collided(tank_body, border_bottom_body):
                    tank.stop_moving(wall=True)
        #left field
        for i in range(len(borders_left)):
            border_left = cast.get_nth_actor(FIELD_LEFT, i)
            for tank in tanks:
                border_left_body = border_left.get_body()
                tank_body = tank.get_body()

                if self._physics_service.has_collide(border_left_body, tank_body):
                    cast.remove_actor(TANKS_GROUP, tank)
        
            for border_left in borders_left:
                tank_body = tank.get_body()
                border_left_body = border_left.get_body()

                if self._physics_service.has_collided(tank_body, border_left_body):
                    tank.stop_moving(wall=True)
        #right field
        for i in range(len(borders_right)):
            border_right = cast.get_nth_actor(FIELD_RIGHT, i)
            for tank in tanks:
                border_right_body = border_right.get_body()
                tank_body = tank.get_body()

                if self._physics_service.has_collide(border_right_body, tank_body):
                    cast.remove_actor(TANKS_GROUP, tank)
        
            for border_right in borders_right:
                tank_body = tank.get_body()
                border_right_body = border_right.get_body()

                if self._physics_service.has_collided(tank_body, border_right_body):
                    tank.stop_moving(wall=True)

        

