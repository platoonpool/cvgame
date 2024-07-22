import pygame
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()
imgBackground = pygame.image.load("../Resources/BackgroundBlue.jpg").convert()
imgBalloonRed = pygame.image.load("../Resources/BalloonRed.png").convert_alpha()
imgBalloonRed = pygame.transform.rotozoom(imgBalloonRed, 90, 0.3)


start = True
while start:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    window.blit(imgBackground, (0, 0))
    window.blit(imgBalloonRed, (200, 300))

    pygame.display.update()
    clock.tick(fps)
    
