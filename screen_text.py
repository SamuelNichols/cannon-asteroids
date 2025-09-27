import pygame

class ScreenText(pygame.sprite.Sprite):
    def __init__(self, x, y, text="lorem-ipsum", font="Arial", font_size=30, font_col="white", antialias=True):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super.__init__()

        self.text_font = pygame.font.SysFont(font, font_size)
        self.position = pygame.Vector2(x, y)
        self.font_col = font_col
        self.antialias = antialias
        self.text = text

        # setting up text surface as member var so we dont have to re-render every game loop
        self.img = None
        self.needs_rerender = True
        self.render_font()

    def render_font(self):
        self.img = self.text_font.render(self.text, self.antialias, self.font_col)
        self.needs_rerender = False

    def draw(self, screen):
        if self.needs_rerender:
            self.render_font()
        print("drawing")
        screen.blit(self.img, (self.position.x, self.position.y))

    def update(self, dt):
        pass
