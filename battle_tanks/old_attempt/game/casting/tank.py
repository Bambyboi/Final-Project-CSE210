from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Tank(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Tank.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the tank's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the tank's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the tank using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def turn_left(self):
        """Rotates the tank counterclockwise at a steady pace."""

    def turn_right(self):
        """Rotates the tank clockwise at a steady pace."""

    def drive_backward(self): # This used to swing left
        """Moves the tank backwards, relative to its angle."""
        velocity = Point(-TANK_VELOCITY, 0)  ###Changed from RACKET_VELOCITY to TANK_VELOCITY
        self._body.set_velocity(velocity)
        
    def drive_forward(self): # this used to swing right, now it moves the tank in a forward direction
        """Moves the tank forwards, relative to its angle."""
        velocity = Point(TANK_VELOCITY, 0)   ### Same as mentioned above, where is this originally from???
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the tank from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)

        