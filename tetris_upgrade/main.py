import pygame
import random
import usb
from practicum import find_mcu_boards, McuBoard, PeriBoard
from Tetris import Tetris,Figure
from multi import multi_play
from single import single_play

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


devs = find_mcu_boards()
mcu_1 = McuBoard(devs[0])
peri = PeriBoard(mcu_1)
if len(devs) == 2 :
    mcu_2 = McuBoard(devs[1])
    peri1 = PeriBoard(mcu_2)



# Initialize the game engine
pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)

menu_state = "menu"
select = 0
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

#multi_play(peri, peri1, colors, screen)
#single_play(peri, colors, screen)
done = False
check_up = 1
check_left = 1
check_right = 1
check_down = 1
while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Single Player", True, WHITE)
    text2 = font.render("Multi Player", True, WHITE)
    screen.blit(text, [200,100 ])
    screen.blit(text2, [200,150])
    select = select%2
    pygame.draw.rect(screen, WHITE,
                     [180,
                      100+select*50,
                      20, 20])
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
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()