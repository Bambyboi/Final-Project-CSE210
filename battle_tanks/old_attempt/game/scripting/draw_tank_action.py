from constants import *
from game.scripting.action import Action
from game.casting.image import Image


class DrawTankAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        for i in range(NUMBER_OF_PLAYERS):
            if len(cast.get_actors(TANKS_GROUP)) >= NUMBER_OF_PLAYERS:
                tank = cast.get_nth_actor(TANKS_GROUP, i)
                body = tank.get_body()

                if tank.is_debug():
                    rectangle = body.get_rectangle()
                    self._video_service.draw_rectangle(rectangle, PURPLE)
                    
                # animation = tank.get_animation()
                # image = animation.next_image()
                image = Image(TANKS_IMAGES[f"player_{i+1}"])
                position = body.get_position()
                self._video_service.draw_image(image, position)