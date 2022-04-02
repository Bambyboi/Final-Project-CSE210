from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveTankAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        for i in range(NUMBER_OF_PLAYERS):
            if len(cast.get_actors(TANKS_GROUP)) >= NUMBER_OF_PLAYERS:
                tank = cast.get_nth_actor(TANKS_GROUP, i)
                body = tank.get_body()
                image = tank.get_image()
                rotation = image.get_rotation()
                velocity = body.get_velocity()
                position = body.get_position()
                x = position.get_x()
                y = position.get_y()

                
                position = position.add(velocity)

                if y < 0:
                    position = Point(position.get_x(), 0)
                elif y > (SCREEN_HEIGHT - TANK_HEIGHT):
                    position = Point(position.get_x() ,SCREEN_HEIGHT - TANK_HEIGHT)

                if x < 0:
                    position = Point(0, position.get_y())
                elif x > (SCREEN_WIDTH - TANK_WIDTH):
                    position = Point(SCREEN_WIDTH - TANK_WIDTH, position.get_y())
                    
                body.set_position(position)
        