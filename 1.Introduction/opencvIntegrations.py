import pygame
import cv2
import numpy as np
import sys

# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

if not cap.isOpened():
    print("Error: Could not open video device")
    sys.exit()

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            cap.release()
            sys.exit()

    # OpenCV
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    # Resize image to window size
    img = cv2.resize(img, (width, height))

    # Convert BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Rotate and flip the image to match Pygame's coordinate system
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)

    # Blit the frame to the window
    window.blit(frame, (0, 0))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)

# Release resources
cap.release()
pygame.quit()
sys.exit()

