"""Write a Python program to calculate the hypotenuse of a right angled triangle."""

import math
import pygame

if __name__ == "__main__":
    x = float(input("\n Enter the length of one side of the right angled triangle: "))
    y = float(input("\n Enter the length of the other side of the right angled triangle: "))

    z = math.sqrt(pow(x,2) + pow(y,2))

    print("Length of hypotenuse: ",z)

    pygame.init()

    screen = pygame.display.set_mode((1280,720))

    img_pos_x = 50
    img_pos_y = 50

    pygame.draw.line(screen,(255,0,255),(img_pos_x,img_pos_y),(img_pos_x,img_pos_y + y),width=4)
    pygame.draw.line(screen,(255,0,255),(img_pos_x,img_pos_y + y),(img_pos_x + x,img_pos_y+y),width = 4)
    pygame.draw.line(screen,(255,0,255),(img_pos_x + x,img_pos_y+y),(img_pos_x,img_pos_y),width = 4)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #1078 504 1190.0