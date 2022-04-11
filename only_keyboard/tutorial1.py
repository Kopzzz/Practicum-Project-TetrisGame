from sre_parse import State
import pygame
import random
# import usb
# from practicum import find_mcu_boards, McuBoard, PeriBoard
from Tetris import Tetris, Figure


def tutorial_single(colors, screen):
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()
    fps = 25
    pygame.mixer.music.load("../audio/BGM InGame.mp3")
    pygame.mixer.music.play(-1)
    bg = pygame.image.load("../only_keyboard/bg-.jpeg")
    board_pic = pygame.image.load("../only_keyboard/board2.jpeg")
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    YELLOW = (255, 255, 0)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    # light_min = peri.get_light()

    check_up = 1
    check_left = 1
    check_right = 1

    while not done:
        screen.fill((0,0,0))
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render("Button 1 : use hand block this sensor ", True, BLACK)
        text_1 = font.render("                  to remove obstacle ", True, BLACK)
        text1 = font.render("Button 2 : use to rotate block", True, BLACK)
        text2 = font.render("Button 3 : move block to the left", True, BLACK)
        text3 = font.render("Button 4 : move block to the right", True, BLACK)
        text4 = font.render("Button 5 : use to accelerate fall rate of the block", True, BLACK)
        screen.blit(bg, [0, 0])
        screen.blit(board_pic, [50, 60])
        screen.blit(text, [250 + 100, 100 + 50])
        screen.blit(text_1, [250 + 100, 120 + 50])
        screen.blit(text1, [250 + 100, 140 + 50])
        screen.blit(text2, [250 + 100, 160 + 50])
        screen.blit(text3, [250 + 100, 180 + 50])
        screen.blit(text4, [250 + 100, 200 + 50])

        '''pygame.draw.rect(screen, WHITE,
                         [50+180+50,
                          50+100+select*50,
                          20, 20])'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and check_up:
                    # pygame.draw.rect(screen, BLACK, [180, 100 + select * 50, 20, 20])
                    return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    check_up = 1
            '''
            if not peri.get_up():
                return
            if not peri.get_left():
                check_left = 1
            if not peri.get_right():
                check_right = 1
            if not peri.get_down():
                check_down = 1


        if peri.get_up() and check_up:
            return

        if not peri.get_up():
            check_up = 1
        '''
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()