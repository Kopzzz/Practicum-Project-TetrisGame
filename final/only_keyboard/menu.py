import pygame
import random
#import usb
#from practicum import find_mcu_boards, McuBoard, PeriBoard
from Tetris import Tetris,Figure
from multi import multi_play
from single import single_play
from how_to_play import tutorial_single

colors = [
    (0, 0, 0),
    (200, 175, 250), #purple
    (100, 250, 250), #blue
    (250, 250, 70), #yellow
    (155, 255, 0), #green
    (230, 25, 0), #red
    (250, 100, 255), #pink
]
'''
devs = find_mcu_boards()
mcu_1 = McuBoard(devs[0])
peri = PeriBoard(mcu_1)
if len(devs) == 2 :
    mcu_2 = McuBoard(devs[1])
    peri1 = PeriBoard(mcu_2)
'''
# Initialize the game engine
pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)

background = pygame.image.load("./pic/BG_Menu.jpg")
select_m = pygame.image.load("./pic/menu_button.png")

menu_state = "menu"
select = 0
pygame.display.set_caption("Tetris upgrade")

clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

#multi_play(colors, screen)
#single_play(peri, colors, screen)
done = False
check_up = 1
check_left = 1
check_right = 1
check_down = 1

pygame.mixer.music.load("./audio/BGM Menu.mp3")
pygame.mixer.music.play(-1)
while not done:
    #screen.fill((0,0,0))
    screen.blit(background,(0,0))

    font = pygame.font.Font('./font/04B_30__.ttf', 25)
    text = font.render("Singleplayer", True, WHITE)
    text2 = font.render("Multiplayer", True, WHITE)
    text3 = font.render("How to play", True, WHITE)
    select = select % 3
    screen.blit(select_m, [35 + 180 + 50, 14 + 70 + select * 50])
    screen.blit(text, [200+100,100+20])
    screen.blit(text2, [200+100,150+20])
    screen.blit(text3, [200+100,200+20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and check_up:
                #pygame.draw.rect(screen, BLACK, [180, 100 + select * 50, 20, 20])
                select -= 1
                check_up = 0
            if event.key == pygame.K_DOWN and check_down:
                #pygame.draw.rect(screen, BLACK, [180, 100 + select * 50, 20, 20])
                select += 1
                check_down = 0
            if event.key == pygame.K_RIGHT:
                if select == 0:
                    single_play(colors, screen)
                elif select == 1:
                    multi_play(colors, screen)
                else:
                    tutorial_single(colors, screen)
                check_right = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                check_up = 1
            if event.key == pygame.K_DOWN:
                check_down = 1
            if event.key == pygame.K_RIGHT:
                check_right = 1
        '''
        if not peri.get_up():
            check_up = 1
        if not peri.get_left():
            check_left = 1
        if not peri.get_right():
            check_right = 1
        if not peri.get_down():
            check_down = 1

        
    if peri.get_up() and check_up:
        pygame.draw.rect(screen, BLACK, [180, 100 + select * 50, 20, 20])
        select -= 1
        check_up = 0
    if peri.get_down() and check_down:
        pygame.draw.rect(screen, BLACK, [180, 100 + select * 50, 20, 20])
        select += 1
        check_down = 0
    if peri.get_right() and check_right:
        if select == 0:
            single_play(peri, colors, screen)
        else:
            multi_play(peri, peri1, colors, screen)
        check_right = 0

    if not peri.get_up():
        check_up = 1
    if not peri.get_left():
        check_left = 1
    if not peri.get_right():
        check_right = 1
    if not peri.get_down():
        check_down = 1
    '''
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()