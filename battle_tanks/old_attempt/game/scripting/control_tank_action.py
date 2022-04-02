from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.bullet import Bullet


class ControlTankAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._facing1 = 90
        self._facing2 = 90
        self.cool_down1 = 0
        self.cool_down2 = 0


    def execute(self, cast, script, callback):
        
        if len(cast.get_actors(TANKS_GROUP)) >= NUMBER_OF_PLAYERS:
            for i in range(NUMBER_OF_PLAYERS):
                if i == 0:
                    tank = cast.get_nth_actor(TANKS_GROUP, i)
                    if self._keyboard_service.is_key_down(P1_UP): 
                        # tank.set_rotation(270)
                        tank.drive_forward()
                        self._facing1 = 270
                    elif self._keyboard_service.is_key_down(P1_DOWN): 
                        # tank.set_rotation(90)
                        tank.drive_backward() 
                        self._facing1 = 90
                    elif self._keyboard_service.is_key_down(P1_LEFT):
                        # tank.set_rotation(180)
                        tank.turn_left(tank)
                        self._facing1 = 180
                    elif self._keyboard_service.is_key_down(P1_RIGHT):
                        # tank.set_rotation(0)
                        tank.turn_right(tank)
                        self._facing1 = 0
                    else: 
                        tank.stop_moving()  
                    self.cool_down1 += 1
                    print(self.cool_down1)
                    if self.cool_down1 >= 60:
                        if self._keyboard_service.is_key_down(P1_SHOOT):
                            self._facing1 = tank.get_velocity()
                            _body = tank.get_body()
                            _position = _body.get_position()
                            P1_x = _position.get_x()
                            P1_y = _position.get_y()
                            position = Point(P1_x + TANK_WIDTH / 2, P1_y + TANK_HEIGHT / 2)
                            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
                            velocity = Point(0, 0)
                            body = Body(position, size, velocity)
                            image = Image(BULLET_IMAGE)
                            bullet = Bullet(body, image, player = 1)
                            cast.add_actor(BULLET_GROUP, bullet)
                            bullet.fire(self._facing1, cast, player = 1, velocity_new = self._facing1)
                            self.cool_down1 -= 60

                elif i == 1:
                    tank = cast.get_nth_actor(TANKS_GROUP, i)
                    if self._keyboard_service.is_key_down(P2_UP): 
                        tank.drive_forward()
                        # tank.set_rotation(90)
                        self._facing2 = 90
                    elif self._keyboard_service.is_key_down(P2_DOWN): 
                        # tank.set_rotation(270)
                        tank.drive_backward()  
                        self._facing2 = 270
                    elif self._keyboard_service.is_key_down(P2_LEFT):
                        # tank.set_rotation(0)
                        tank.turn_left(tank)
                        self._facing2 = 0
                    elif self._keyboard_service.is_key_down(P2_RIGHT):
                        # tank.set_rotation(180)
                        tank.turn_right(tank)
                        self._facing2 = 180
                    else: 
                        tank.stop_moving()
                    self.cool_down2 += 1
                    if self.cool_down2 >= 60:     
                        if self._keyboard_service.is_key_down(P2_SHOOT):
                            self._facing2 = tank.get_velocity()
                            _body = tank.get_body()
                            _position = _body.get_position()
                            P2_x = _position.get_x()
                            P2_y = _position.get_y()
                            position = Point(P2_x + TANK_WIDTH / 2, P2_y + TANK_HEIGHT / 2)
                            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
                            velocity = Point(0, 0)
                            body = Body(position, size, velocity)
                            image = Image(BULLET_IMAGE)
                            bullet = Bullet(body, image, player = 2)
                            cast.add_actor(BULLET_GROUP, bullet)
                            bullet.fire(self._facing2, cast, player = 2, velocity_new = self._facing2)
                            self.cool_down2 -= 60
                    
    