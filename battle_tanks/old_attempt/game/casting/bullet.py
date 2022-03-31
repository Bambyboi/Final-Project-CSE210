import random
import math
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Bullet(Actor):
    """A solid, spherical object that is shot around in the game to break walls and defeat other tanks."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bullet.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self):
        """Bounces the bullet in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the bullet in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

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
        
    def release(self):
        """Release the bullet in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BULLET_VELOCITY * rn, BULLET_VELOCITY * rn])
        vy = -BULLET_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)


    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        
       # self.center.x = RIFLE_WIDTH * math.cos(math.radians(angle))
       # self.center.y = RIFLE_WIDTH * math.sin(math.radians(angle))
        
