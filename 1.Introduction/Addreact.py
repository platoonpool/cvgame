import pygame
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()
imgBackground = pygame.image.load("../Resources/BackgroundBlue.jpg").convert()
imgBalloonRed = pygame.image.load("../Resources/BalloonRed.png").convert_alpha()
rectBalloon = imgBalloonRed.get_rect()
rectNew = pygame.Rect(500, 0, 200, 200)


start = True
while start:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    print(rectBalloon.colliderect(rectNew))
    rectBalloon.x += 2
    window.blit(imgBackground, (0, 0))
    window.blit(imgBalloonRed, rectBalloon)
    pygame.display.update()
    clock.tick(fps)
