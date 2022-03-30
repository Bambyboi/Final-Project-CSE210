from mimetypes import init
from constants import *
from game.casting.actor import Actor

class Background(Actor):
    """init(self, filename) 
    max width max hieght
    display image
    """
    def __init__(self, body, image, debug = False):
        """Constructs a new Background.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def _display_background(self):
        """display the background"""

    def _clear_background(self):
        """clears the given background"""