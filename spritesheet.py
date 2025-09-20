import pygame

class Sprite():
    def __init__(self, image, width, height):
        self.__image = image
        self.width = width
        self.height = height
        self.rotation = 0
        self.pos = image.get_rect()
        self.pos.center = (self.width / 2, self.height / 2)

    def blit(self, screen, position, rotation=0):
        r_image = pygame.transform.rotate(self.__image, -rotation)
        r_rect = r_image.get_rect(center=self.pos.center).move(position.x - self.width / 2, position.y - self.height / 2)
        screen.blit(r_image, r_rect)

class SpriteSheet():
    def __init__(self, spritesheet):
        self.__sheet = pygame.image.load(spritesheet)

    # loads a sprite 
    # TODO: made a spritesheet and sprite object so each spritesheet and sprite is only made once (no need to rebuild since just blitting)
    def create_sprite(self, rect, scale=0, rotation=0):
        # new image size width and height
        sheet_alpha = self.__sheet.convert_alpha()
        width, height = rect[2], rect[3]
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(sheet_alpha, (0, 0), rect)
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image = pygame.transform.rotate(image, -rotation)
        image = image.convert_alpha()

        return Sprite(image, width, height)


