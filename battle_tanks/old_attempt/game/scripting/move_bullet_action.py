from constants import *
from game.scripting.action import Action


class MoveBulletAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bullets = cast.get_actors(BULLET_GROUP)
        for bullet in bullets:
            body = bullet.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)

            if body.get_position().get_y() > SCREEN_HEIGHT:
                cast.remove_actor(BULLET_GROUP, bullet)
            elif body.get_position().get_y() < 0 - BULLET_HEIGHT:
                cast.remove_actor(BULLET_GROUP, bullet)
            elif body.get_position().get_x() > SCREEN_WIDTH:
                cast.remove_actor(BULLET_GROUP, bullet)
            elif body.get_position().get_x() < 0 - BULLET_WIDTH:
                cast.remove_actor(BULLET_GROUP, bullet)
