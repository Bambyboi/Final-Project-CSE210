# from typing_extensions import Self
import math
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.image import Image


class Tank(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, image, debug = False, angle=0):
        """Constructs a new Tank.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._image = image
        self.angle = angle
        

    def get_animation(self):
        """Gets the tank's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the bullet's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the bullet's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def set_image(self, image):
        self._image = Image(image)
    
    def set_rotation(self, angle):
        self._image.set_rotation(angle)
    
    def get_rotation(self):
        return self._image.get_rotation()

    def move_next(self):
        """Moves the tank using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)
    
    def update_angle(self, angle):
        velocity_old = self._body.get_velocity()
        vx = velocity_old.get_x()
        vy = velocity_old.get_y()
        self.velocity_dx = vx + math.cos(math.radians(angle))
        self.velocity_dy = vy + math.sin(math.radians(angle))
        velocity = Point(self.velocity_dx, self.velocity_dy)
        self._body.set_velocity(velocity)
        
    def get_velocity(self):
        return self._body.get_velocity()

    def turn_left(self, tank):
        """Rotates the tank counterclockwise at a steady pace."""
        # velocity = Point(-TANK_VELOCITY, 0)
        old_rotation = self.get_rotation()
        tank.set_rotation(old_rotation - TANK_ROTATION_SPEED)
        # self._body.set_velocity(velocity)
        # self.update_angle(-1)

    def turn_right(self, tank):
        """Rotates the tank clockwise at a steady pace."""
        # velocity = Point(TANK_VELOCITY, 0)
        old_rotation = self.get_rotation()
        tank.set_rotation(old_rotation + TANK_ROTATION_SPEED)
        # self._body.set_velocity(velocity)

    def drive_backward(self): # This used to swing left
        """Moves the tank backwards, relative to its angle."""
        # velocity = Point(0, TANK_VELOCITY)
        self.velocity_dx = -math.cos(math.radians(self.get_rotation())) * TANK_VELOCITY
        self.velocity_dy = -math.sin(math.radians(self.get_rotation())) * TANK_VELOCITY
        velocity = Point(self.velocity_dx, self.velocity_dy)
        self._body.set_velocity(velocity)

        # self._body.set_velocity(velocity)
        
    def drive_forward(self): # this used to swing right, now it moves the tank in a forward direction
        """Moves the tank forwards, relative to its angle."""
        self.velocity_dx = math.cos(math.radians(self.get_rotation())) * TANK_VELOCITY
        self.velocity_dy = math.sin(math.radians(self.get_rotation())) * TANK_VELOCITY
        velocity = Point(self.velocity_dx, self.velocity_dy)
        self._body.set_velocity(velocity)
    
    def stop_moving(self, wall=False):
        """Stops the tank from moving."""
        if not wall:
            velocity = Point(0, 0)
        else:
            velocity = self._body.get_velocity()
            _x = velocity.get_x() * .8
            _y = velocity.get_y() * .8
            velocity = Point(_x,_y)
        self._body.set_velocity(velocity)

        