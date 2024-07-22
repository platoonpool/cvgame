import pygame
import cv2
import numpy as np
import sys
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height
if not cap.isOpened():
    print("Error: Could not open video device")
    sys.exit()
start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            cap.release()
            sys.exit() 
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    img = cv2.resize(img, (width, height))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)
    window.blit(frame, (0, 0))
    pygame.display.update()
    clock.tick(fps)

cap.release()
pygame.quit()
sys.exit()

