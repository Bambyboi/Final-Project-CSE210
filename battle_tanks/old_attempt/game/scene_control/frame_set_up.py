import csv # Same
import random
from constants import * # Same
from game.casting.animation import Animation # Same
from game.casting.bullet import Bullet  # Changed ALL INSTANCES of BALL to BULLET
from game.casting.body import Body # Same
from game.casting.brick import Brick # Same (Though we need a wall builder... ideas?)
from game.casting.image import Image # Same
from game.casting.label import Label # Same
from game.casting.point import Point # Same
from game.casting.tank import Tank # Changed ALL INSTANCES of RACKET to TANK
from game.casting.stats import Stats # Same, though it needs new methods for score
from game.casting.text import Text # Same
from game.casting.background import Background
from game.scripting.change_scene_action import ChangeSceneAction # Same
from game.scripting.check_over_action import CheckOverAction # Same
from game.scripting.collide_borders_action import CollideBordersAction #Same, so far
from game.scripting.collide_brick_action import CollideBrickAction # Same, so far......
from game.scripting.collide_tank_action import CollideTankAction # Same, for now....
from game.scripting.control_tank_action import ControlTankAction # Same, for now...
from game.scripting.draw_bullet_action import DrawBulletAction # Same, for now...
from game.scripting.draw_bricks_action import DrawBricksAction # Same, for now...
from game.scripting.draw_dialog_action import DrawDialogAction # Same
from game.scripting.draw_hud_action import DrawHudAction # Same
from game.scripting.draw_tank_action import DrawTankAction # Same, for now...
from game.scripting.draw_background_action import DrawBackgroundAction
from game.scripting.end_drawing_action import EndDrawingAction # Same
from game.scripting.initialize_devices_action import InitializeDevicesAction # Same
from game.scripting.load_assets_action import LoadAssetsAction # Same
from game.scripting.move_bullet_action import MoveBulletAction # Same, for now...
from game.scripting.move_tank_action import MoveTankAction # Same, for now...
from game.scripting.play_sound_action import PlaySoundAction # Same
from game.scripting.release_devices_action import ReleaseDevicesAction # Same
from game.scripting.start_drawing_action import StartDrawingAction # Same
from game.scripting.timed_change_scene_action import TimedChangeSceneAction # Same
from game.scripting.unload_assets_action import UnloadAssetsAction # Same
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService

class FrameSetUp:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BRICKS_ACTION = CollideBrickAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_TANK_ACTION = CollideTankAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_TANK_ACTION = ControlTankAction(KEYBOARD_SERVICE)
    DRAW_BACKGROUND_ACTION = DrawBackgroundAction(VIDEO_SERVICE)
    DRAW_BULLET_ACTION = DrawBulletAction(VIDEO_SERVICE)
    DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_TANK_ACTION= DrawTankAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BULLET_ACTION = MoveBulletAction()
    MOVE_TANK_ACTION = MoveTankAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == START_MENU:
            self._prepare_start_menu(cast, script)
        elif scene == CONTROLS:
            self._prepare_controls(cast, script)
        elif scene == START_PLAYING:
            self._prepare_start_playing(cast, script)
        elif scene == NEXT_ROUND:    
            self._prepare_next_round(cast, script)
        elif scene == WINNER:    
            self._prepare_game_over(cast, script)
        elif scene == PLAY_AGAIN:
            self._prepare_play_again(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    
    def _prepare_start_menu(self, cast, script):
        self._add_background(cast, START_MENU_IMAGE)
        self._add_stats(cast, player=1)
        self._add_stats(cast, player=2)
        self._add_score(cast, player=1)
        self._add_score(cast, player=2)
        self._add_tank(cast, player=1)
        self._add_tank(cast, player=2)
        self._add_dialog(cast, ENTER_TO_CONTROLS)


        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, CONTROLS))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    
    def _prepare_controls(self, cast, script):
        self._add_background(cast, CONTROLS_IMAGE)
        self._add_dialog(cast, ENTER_TO_START, y=CENTER_Y / 2)
        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, START_PLAYING))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
    

    def _prepare_start_playing(self, cast, script):
        self._add_background(cast, BACKGROUND_IMAGE)
        self._add_stats(cast)   
        self._add_bullets(cast)
        self._add_bricks(cast)
        
        self._add_dialog(cast, "IT WORKED")

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_TANK_ACTION)
        # script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_ROUND))
        self._add_update_script(script)
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

        
    def _prepare_next_round(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        self._remove_tanks
        self._remove_bullet
        self._add_bullets(cast)
        self._add_bricks(cast)
        self._add_tank(cast)
        self._add_tank(cast, 2)
        self._add_dialog(cast, LOADING_NEW_MAP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_TANK_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_play_again(self, cast, script):
        self._add_bullet(cast)
        self._add_tank(cast)
        self._add_dialog(cast, LOADING_NEW_MAP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(PLAY_AGAIN, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    # def _prepare_in_play(self, cast, script):
    #     self._activate_bullet(cast)
    #     cast.clear_actors(DIALOG_GROUP)

    #     script.clear_actions(INPUT)
    #     script.add_action(INPUT, self.CONTROL_TANK_ACTION)
    #     self._add_update_script(script)
    #     self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        
        self._add_bullets(cast)
        self._add_tank(cast)
        self._add_dialog(cast, WINNER)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(START_MENU, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _add_background(self, cast, filename):
        cast.clear_actors(BACKGROUND_GROUP)
        x = 0
        y = 0
        position = Point(x, y)
        size = Point(SCREEN_WIDTH, SCREEN_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(filename)
        background = Background(body, image, True)
        cast.add_actor(BACKGROUND_GROUP, background)

    def _activate_bullet(self, cast):
        bullet = cast.get_first_actor(BULLET_GROUP)
        bullet.release()

    def _add_bullets(self, cast):
        x = BULLET_WIDTH * 2
        y = CENTER_Y - 100
        position = Point(x, y)
        size = Point(BULLET_WIDTH, BULLET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BULLET_IMAGE)
        bullet = Bullet(body, image, True)
        cast.add_actor(BULLET_GROUP, bullet)
    
    def _remove_bullet(self, cast):
        cast.clear_actors(BULLET_GROUP)

    def _add_bricks(self, cast):
        cast.clear_actors(BRICKS_GROUP)
        how_many_bricks_per_group = 50
        if NUMBER_OF_PLAYERS > 2:
            for i in range(how_many_bricks_per_group):
                x = FIELD_LEFT + i * SCREEN_WIDTH / how_many_bricks_per_group
                y = i * SCREEN_HEIGHT / how_many_bricks_per_group
                
                position = Point(x, y)
                size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                velocity = Point(0, 0)
                image_num = random.randint(1, 3)
                image = BRICK_IMAGES[image_num]
                body = Body(position, size, velocity, image)
                brick = Brick(body)
                cast.add_actor(BRICKS_GROUP, brick)
            for i in range(how_many_bricks_per_group):
                x = FIELD_LEFT + i * SCREEN_WIDTH / how_many_bricks_per_group
                y = SCREEN_HEIGHT - (i * SCREEN_HEIGHT / how_many_bricks_per_group)
                
                position = Point(x, y)
                size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                velocity = Point(0, 0)
                image_num = random.randint(1, 3)
                image = BRICK_IMAGES[image_num]
                body = Body(position, size, velocity, image)
                brick = Brick(body)
                cast.add_actor(BRICKS_GROUP, brick)
        if NUMBER_OF_PLAYERS == 2:
            for j in range(10):
                for i in range(how_many_bricks_per_group):
                    x = round(250 + BRICK_WIDTH * j)
                    y = SCREEN_HEIGHT - (i * SCREEN_HEIGHT / how_many_bricks_per_group)
                    
                    position = Point(x, y)
                    size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                    velocity = Point(0, 0)
                    image_num = random.randint(1, 3)
                    image = BRICK_IMAGES[image_num]
                    body = Body(position, size, velocity, image)
                    

                    brick = Brick(body)
                    cast.add_actor(BRICKS_GROUP, brick)
            


        # Drawing an outline around the map
        # for i in range(round(SCREEN_WIDTH/BRICK_WIDTH)):
            # x = i * BRICK_WIDTH
            # y = 0
            
        # edit to add walls of bricks in randomly but not on top of tank
        
        # stats = cast.get_first_actor(STATS_GROUP)
        # level = stats.get_level() % BASE_LEVELS
        # filename = LEVEL_FILE.format(level)

        # with open(filename, 'r') as file:
        #     reader = csv.reader(file, skipinitialspace=True)

        #     for r, row in enumerate(reader):
        #         for c, column in enumerate(row):

        #             x = FIELD_LEFT + c * BRICK_WIDTH
        #             y = FIELD_TOP + r * BRICK_HEIGHT
        #             color = column[0]
        #             frames = int(column[1])
        #             points = BRICK_POINTS 
                    
        #             if frames == 1:
        #                 points *= 2
                    
        #             position = Point(x, y)
        #             size = Point(BRICK_WIDTH, BRICK_HEIGHT)
        #             velocity = Point(0, 0)
        #             images = BRICK_IMAGES[color][0:frames]

        #             body = Body(position, size, velocity)
        #             animation = Animation(images, BRICK_RATE, BRICK_DELAY)

        #             brick = Brick(body, animation, points)
        #             cast.add_actor(BRICK_GROUP, brick)

    def _add_dialog(self, cast, message, x=CENTER_X,y=CENTER_Y):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(x, y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    # def _add_level(self, cast):
    #     cast.clear_actors(LEVEL_GROUP)
    #     text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
    #     position = Point(HUD_MARGIN, HUD_MARGIN)
    #     label = Label(text, position)
    #     cast.add_actor(LEVEL_GROUP, label)

    # def _add_lives(self, cast):
    #     cast.clear_actors(LIVES_GROUP)
    #     text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
    #     position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
    #     label = Label(text, position)
    #     cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast, player):
        if player == 1:
            x = 100
            y = 0 
        elif player == 2:
            x = SCREEN_WIDTH - 100
            y = 0
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(x, y)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast, player=1):
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)
    
    def _remove_stats(self, cast):
        cast.clear_actors(STATS_GROUP)

    def _add_tank(self, cast, player=1):
        # cast.clear_actors(TANKS_GROUP) # moved to _remove_tanks
        if player == 1:
            x = TANK_WIDTH
            y = SCREEN_HEIGHT / 2 - TANK_HEIGHT / 2
        elif player == 2:
            x = SCREEN_WIDTH - TANK_WIDTH * 2
            y = SCREEN_HEIGHT / 2 - TANK_HEIGHT / 2

        position = Point(x, y)
        size = Point(TANK_WIDTH, TANK_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(TANKS_IMAGES, TANK_RATE)
        image = Image(TANKS_IMAGES[f"player_{player}"])
        tank = Tank(body, animation, image)
        cast.add_actor(TANKS_GROUP, tank)

    def _remove_tanks(self, cast):
        cast.clear_actors(TANKS_GROUP)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_BACKGROUND_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BULLET_ACTION)
        script.add_action(OUTPUT, self.DRAW_BRICKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_TANK_ACTION)
        script.add_action(OUTPUT, self.DRAW_TANK_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BRICKS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TANK_ACTION)
        script.add_action(UPDATE, self.MOVE_BULLET_ACTION)
        script.add_action(UPDATE, self.MOVE_TANK_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)