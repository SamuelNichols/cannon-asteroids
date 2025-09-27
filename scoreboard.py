import pygame
from stat_manager import StatsManager
from screen_text import ScreenText

class Scoreboard(ScreenText):
    def __init__(self, stat_manager, x=0, y=0, text="lorem-ipsum", font="Arial", font_size=30, font_col="white", antialias=True):
        super().__init__(x, y, text, font, font_size, font_col, antialias)
        self.stat_manager = stat_manager
        self.score = self.stat_manager.score
        self.text = ""
        self.update_score_string()

    def update_score_string(self):
        self.text = f"Score: {self.score}"
        self.needs_rerender = True

    def update(self, _dt):
        if self.score != self.stat_manager.score:
            self.score = self.stat_manager.score
            self.update_score_string()
