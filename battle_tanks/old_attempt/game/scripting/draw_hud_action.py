from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        # self._draw_label(cast, LEVEL_GROUP, LEVEL_FORMAT, stats.get_level())
        # self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats.get_lives())
        for i in range(2):
            self._draw_label_n(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score(), i)
        # self._draw_label_n(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score(), n=1)

    def _draw_label(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)
    
    def _draw_label_n(self, cast, group, format_str, data, n=1):
        label = cast.get_nth_actor(group, n)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)