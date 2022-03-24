from settings import *
from game.director import Director
from game.scene_control.frame_set_up import FrameSetUp


def main():
    director = Director(FrameSetUp.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()