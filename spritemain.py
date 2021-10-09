import pygame
import sys
import random

#!INIT AND CLOCK
pygame.init()
clock = pygame.time.Clock()

#!BACKGROUND AND SCREEN
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
background = pygame.image.load("woodbg.jpg").convert_alpha()


#!CONTROLS GENERAL

#!{Mouse}
pygame.mouse.set_visible(False)
#!CLASSES

#!{Crosshair Class}


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("laser.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    # *updates simultaneously
    def update(self):

        self.rect.center = pygame.mouse.get_pos()
        

#!{TARGET CLASS}


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


#!DECLARATIONS
#!{Crosshair}
crosshair = Crosshair("crosshair_white_small.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


#!{TARGET}
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("icon_target.png", random.randrange(
        0, width), random.randrange(0, height))
    target_group.add(new_target)

#!MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
