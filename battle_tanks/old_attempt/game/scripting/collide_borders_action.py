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

    def collide_borders(self, cast):
        "collision of each tanks when it hits to the borders."

        #if 