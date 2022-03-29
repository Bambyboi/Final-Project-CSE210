import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Battle Tanks"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "battle_tanks/old_attempt/game/assets/fonts/zorque.otf"
FONT_SMALL = 10
FONT_LARGE = 25

# SOUND
BOUNCE_SOUND = "game/assets/sounds/sound1.wav"
WELCOME_SOUND = "game/assets/sounds/sound2.wav"
OVER_SOUND = "game/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS P1
P1_LEFT = "left"
P1_RIGHT = "right"
P1_UP = "up"
P1_Down = "down"
P1_SHOOT = "q"

# KEYS P2
P2_LEFT = "left"
P2_RIGHT = "right"
P2_UP = "up"
P2_Down = "down"
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

# VISUALS

START_MENU_IMAGE = "battle_tanks/old_attempt/game/assets/images/start_menu_image.jpeg"
CONTROLS_IMAGE = "battle_tanks/old_attempt/game/assets/images/controls_image.jpeg"


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

# HUD
HUD_MARGIN = 15
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BULLET
BULLET_GROUP = "bullet"
BULLET_IMAGE = "battle_tanks/old_attempt/game/assets/images/bullet1.jpeg"
BULLET_WIDTH = 28
BULLET_HEIGHT = 28
BULLET_VELOCITY = 6

# PLAYER 1 
P1_TANK = "p1_tank"
p1_TANK_IMAGE = "battle_tanks/old_attempt/game/assets/images/tank_blue.jpeg"

# PLAYER 2
P2_TANK = "p2_tank"
P2_TANK_IMAGE = "battle_tanks/old_attempt/game/assets/images/tank_red.jpeg"

# BOTH TANKS
TANKS_GROUP = "tanks"
TANKS_IMAGES = {
    "player_1": "battle_tanks/old_attempt/game/assets/images/tank_red.jpeg",
    "player_2": "battle_tanks/old_attempt/game/assets/images/tank_blue.jpeg",
    "player_3": "battle_tanks/old_attempt/game/assets/images/tank_yellow.jpeg",
    "player_4": "battle_tanks/old_attempt/game/assets/images/tank_green.jpeg"
}
TANK_WIDTH = 100
TANK_HEIGHT = 100
TANK_RATE = 6
TANK_VELOCITY = 7

# WALLS   ###Are these the bricks?
WALLS_GROUP = "walls"
WALL_IMAGES = {
    "wall_1": "game/assets/images/wall_1.png",
    "wall_2": "game/assets/images/wall_2.png",
    "wall_3": "game/assets/images/wall_3.png"
}
WALLS_WIDTH = 80
WALLS_HEIGHT = 28
WALLS_RATE = 4
WALLS_LIVES = 10

BRICKS_GROUP = "bricks"
BRICK_IMAGES = {
    "brick_1": "game/assets/images/brick_1.png",
    "brick_2": "game/assets/images/brick_2.png",
    "brick_3": "game/assets/images/brick_3.png"
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_RATE = 4
BRICK_LIVES = 10

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
# PREP_TO_LAUNCH = "PREPARING TO LAUNCH" # Removed
# WINNER = f"{winner} Wins!" # We will worry about this later if there is time
