import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Battle Tanks"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 0
FIELD_BOTTOM =  SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "battle_tanks/old_attempt/game/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
HIT_SOUND = "battle_tanks/old_attempt/game/assets/sounds/boing.wav"
WELCOME_SOUND = "battle_tanks/old_attempt/game/assets/sounds/boing.wav"
OVER_SOUND = "battle_tanks/old_attempt/game/assets/sounds/boing.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# PLAYER COUNT
NUMBER_OF_PLAYERS = 2

# KEYS P1
P1_LEFT = "a"
P1_RIGHT = "d"
P1_UP = "w"
P1_DOWN = "s"
P1_SHOOT = "q"

# KEYS P2
P2_LEFT = "j"
P2_RIGHT = "l"
P2_UP = "i"
P2_DOWN = "k"
P2_SHOOT = "u"

# General KEYS 
PAUSE = "p"
ENTER = "enter"

# SCENES
START_MENU = 0
CONTROLS = 1
START_PLAYING = 2
NEXT_ROUND = 3
WINNER = 4
PLAY_AGAIN = 5
CELL_SIZE = 10
# VISUALS

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 5
P1_LIVES = 5
P2_LIVES = 5

# Background
BACKGROUND_GROUP = "backgrounds"
START_MENU_IMAGE = "battle_tanks/old_attempt/game/assets/images/start_menu_image.png"
CONTROLS_IMAGE = "battle_tanks/old_attempt/game/assets/images/controls_image.png"
BACKGROUND_IMAGE = "battle_tanks/old_attempt/game/assets/images/background_image.png"


# HUD
HUD_MARGIN = 15
# LIVES_GROUP = "lives"
SCORE_GROUP = "score"
# LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BULLET
BULLET_GROUP = "bullet"
BULLET_IMAGE = "battle_tanks/old_attempt/game/assets/images/bullet1.png"
BULLET_WIDTH = 20
BULLET_HEIGHT = 20
BULLET_VELOCITY = 6


# PLAYER 1 
P1_TANK = "p1_tank"
p1_TANK_IMAGE = "battle_tanks/old_attempt/game/assets/images/tank_blue.png"

# PLAYER 2
P2_TANK = "p2_tank"
P2_TANK_IMAGE = "battle_tanks/old_attempt/game/assets/images/tank_red.png"

# BOTH TANKS
TANKS_GROUP = "tanks"
TANKS_IMAGES = {
    "player_1": "battle_tanks/old_attempt/game/assets/images/tank_red_copy.png",
    "player_2": "battle_tanks/old_attempt/game/assets/images/tank_blue_copy.png",
    "player_3": "battle_tanks/old_attempt/game/assets/images/tank_yellow.png",
    "player_4": "battle_tanks/old_attempt/game/assets/images/tank_green.png"
}
TANK_WIDTH = 50 #100
TANK_HEIGHT = 50 #100
TANK_RATE = 6
TANK_VELOCITY = 3

# WALLS   ###Are these the bricks?
WALLS_GROUP = "walls"
WALL_IMAGES = {
    "wall_1": "battle_tanks/old_attempt/game/assets/images/wall_1.png",
    "wall_2": "battle_tanks/old_attempt/game/assets/images/wall_2.png",
    "wall_3": "battle_tanks/old_attempt/game/assets/images/wall_3.png"
}
WALLS_WIDTH = 80
WALLS_HEIGHT = 28
WALLS_RATE = 4
WALLS_LIVES = 10

BRICKS_GROUP = "bricks"
BRICK_IMAGES = {
    1: "battle_tanks/old_attempt/game/assets/images/brick1.png",
    2: "battle_tanks/old_attempt/game/assets/images/brick2.png",
    3: "battle_tanks/old_attempt/game/assets/images/brick3.png"
}
BRICK_WIDTH = 21
BRICK_HEIGHT = 7
# BRICK_RATE = 4
# BRICK_LIVES = 10

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_CONTROLS = "PRESS ENTER"
ENTER_TO_START = f"Player 1 Controls: \n  ASDW to move and Q to shoot.     \nPlayer 2 Controls: \n IJKL to move and U to shoot.  \n \n   PRESS ENTER AGAIN TO BEGIN"
LOADING_NEW_MAP = "LOADING NEW MAP"
WINNER = "{winner} Wins!" # We will worry about this later if there is time


#bullet 
BULLET_SPEED = 10
BULLET_LIFE = 60