import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time
import sys
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")
fps = 30
clock = pygame.time.Clock()
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  
cap.set(4, 720)  
imgBalloon = pygame.image.load('../Resources/BalloonRed.png').convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 300
speed = 15
score = 0
startTime = time.time()
totalTime = 30
detector = HandDetector(detectionCon=0.8, maxHands=1)


def reset_balloon():
    rectBalloon.x = random.randint(100, width - 100)
    rectBalloon.y = height + 50


start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            cap.release()
            sys.exit()
    timeRemain = int(totalTime - (time.time() - startTime))
    if timeRemain < 0:
        window.fill((255, 255, 255))
        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time UP', True, (50, 50, 255))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))
    else:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        rectBalloon.y -= speed  
        if rectBalloon.y < 0:
            reset_balloon()
            speed += 1
        if hands:
            hand = hands[0]
            x, y = hand['lmList'][8][0:2]
            if rectBalloon.collidepoint(x, y):
                reset_balloon()
                score += 10
                speed += 1
        img = cv2.resize(img, (width, height))
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))
        window.blit(imgBalloon, rectBalloon)
        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore = font.render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))

    pygame.display.update()
    clock.tick(fps)

cap.release()
pygame.quit()
sys.exit()
