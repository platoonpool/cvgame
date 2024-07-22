import pygame
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("GUI")
fps = 30
clock = pygame.time.Clock()

c = {"lightGreen": (189, 209, 197),
     "lightOrange": (238, 204, 140),
     "lightPink": (232, 178, 152),
     "darkPink": (211, 162, 157),
     "darkGreen": (158, 171, 162),
     "darkGray": (128, 126, 126),
     "lightGray": (204, 204, 204),
     "darkBrown": (89, 61, 61),
     "white": (255, 255, 255),
     "black": (0, 0, 0),
     }
imgBackground = pygame.image.load('../Resources/Project - GUI/background.png').convert()
imgDesign = pygame.image.load('../Resources/Project - GUI/design.png').convert_alpha()
imgIcon1 = pygame.image.load('../Resources/Project - GUI/icon1.png').convert_alpha()
imgIcon2 = pygame.image.load('../Resources/Project - GUI/icon2.png').convert_alpha()
imgIcon3 = pygame.image.load('../Resources/Project - GUI/icon3.png').convert_alpha()
imgIcon4 = pygame.image.load('../Resources/Project - GUI/icon4.png').convert_alpha()
imgIcon5 = pygame.image.load('../Resources/Project - GUI/icon5.png').convert_alpha()
imgShadow = pygame.image.load('../Resources/Project - GUI/shadow.png').convert_alpha()
imgToggleOn = pygame.image.load('../Resources/Project - GUI/toggleOn.png').convert_alpha()
imgToggleOff = pygame.image.load('../Resources/Project - GUI/toggleOff.png').convert_alpha()
pads = [{"no": 1, "color": c['lightGreen'], "text": "Original", "icon": imgIcon2},
        {"no": 2, "color": c['lightOrange'], "text": "Gray Scale", "icon": imgIcon3},
        {"no": 3, "color": c['lightPink'], "text": "Edges", "icon": imgIcon4},
        {"no": 4, "color": c['darkPink'], "text": "Contours", "icon": imgIcon5}]


def drawindowpad(pos, color, text, icon):
    xo, yo, w, h = pos
    window.blit(imgShadow, (xo, yo + h - 66))
    pygame.draw.rect(window, color, (xo, yo, w, 64),
                     border_top_left_radius=10, border_top_right_radius=10)
    pygame.draw.rect(window, c['white'], (xo, yo + 64, w, h - 87),
                     border_bottom_left_radius=10, border_bottom_right_radius=10)
    window.blit(icon, (xo + 20, yo + 12))
    font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 20)
    text = font.render(text, True, c['darkBrown'])
    window.blit(text, (xo + 82, yo + 20))

     def drawfilterpad():
    drawwindowpad((75, 57, 312, 602), c["darkGreen"], "Filter", imgIcon1)
    font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 20)
    textdisp1 = font.render("Gray Scale", True, c["darkBrown"])
    window.blit(textdisp1, (106, 165))
    window.blit(imgToggleOn, (283, 164))
    textdisp2 = font.render("Edges", True, c["darkBrown"])
    window.blit(textdisp2, (106, 165 + 60))
    window.blit(imgToggleOn, (283, 164 + 60))
    textdisp3 = font.render("Contours", True, c["darkBrown"])
    window.blit(textdisp3, (106, 165 + 60 * 2))
    window.blit(imgToggleOff, (283, 164 + 60 * 2))
    textdisp4 = font.render("Blur", True, c["darkBrown"])
    window.blit(textdisp4, (106, 165 + 60 * 3))
    window.blit(imgToggleOff, (283, 164 + 60 * 3))
    font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 25)
    for y in range(0, 3):
        h = 447 + y * 55
        sliderPos = 105 + 50 * y + 30
        pygame.draw.line(window, c["lightGray"], (105, h), (105 + 155, h), 5)
        pygame.draw.line(window, c["darkGray"], (105, h), (sliderPos, h), 5)
        pygame.draw.rect(window, c["darkGray"], (sliderPos, h - 15, 12, 30))
        textDisp = font.render(str(y * 50 + 30), True, c["darkBrown"])
        window.blit(textDisp, (286, h - 18))
def drawall():
    w, h = 312, 301
    gapw, gaph = 72, 25
    drawindowpad((484, 57, w, h), pads[0]['color'], pads[0]['text'], pads[0]['icon'])
    drawindowpad((484 + gapw + w, 57, w, h), pads[1]['color'], pads[1]['text'], pads[1]['icon'])
    drawindowpad((484, 57 + gaph + h, w, h), pads[2]['color'], pads[2]['text'], pads[2]['icon'])
    drawindowpad((484 + gapw + w, 57 + gaph + h, w, h), pads[3]['color'], pads[3]['text'], pads[3]['icon'])
    drawfilterpad()


start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    window.blit(imgBackground, (0, 0))
    imgDesign.set_alpha(0)
    window.blit(imgDesign, (0, 0))
    drawall()
    pygame.display.update()
    clock.tick(fps)
   
