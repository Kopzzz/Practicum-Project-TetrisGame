import pygame
import random
import usb
from practicum import find_mcu_boards, McuBoard, PeriBoard
from Tetris import Tetris,Figure

def single_play(peri, colors, screen):
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    YELLOW = (255, 255, 0)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0
    game.x += 200
    game.next_blockX += 200

    pressing_down = False

    light_min = peri.get_light()

    check_up = 1
    check_left = 1
    check_right = 1

    while not done:
        if game.state == "calibrate":
            if peri.get_down():
                light_min = peri.get_light()
                game.state = "start"

        if game.figure is None:
            game.figure = Figure(3, 0)
            game.next_figure = Figure(3, 0)
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start" or game.state == "obstacle":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False
        if game.state == "start" or game.state == "obstacle":
            if peri.get_light() >= 0.5 * light_min:
                if peri.get_up() and check_up:
                    game.rotate()
                    check_up = 0
                if peri.get_down():
                    pressing_down = True
                if peri.get_left() and check_left:
                    game.go_side(-1)
                    check_left = 0
                if peri.get_right() and check_right:
                    game.go_side(1)
                    check_right = 0

                if not peri.get_up():
                    check_up = 1
                if not peri.get_left():
                    check_left = 1
                if not peri.get_right():
                    check_right = 1

                if not peri.get_down():
                    pressing_down = False
        if game.state == "game over":
            if peri.get_right() :
                game.__init__(20, 10)

            if peri.get_left() :
                return
        screen.fill(WHITE)

        if game.state == "obstacle":
            a = peri.get_light()
            if a <= 0.5 * light_min:
                game.state = "start"
                print(a, light_min)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            for i in range(game.height):
                for j in range(game.width):
                    pygame.draw.rect(screen, GRAY,
                                     [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                    pygame.draw.rect(screen, YELLOW,
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                                      game.zoom - 1])

            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(screen, colors[game.figure.color],
                                             [game.x + game.zoom * (j + game.figure.x) + 1,
                                              game.y + game.zoom * (i + game.figure.y) + 1,
                                              game.zoom - 2, game.zoom - 2])
            if game.next_figure is not None:
                for i in range(4):
                    for j in range(4):
                        pygame.draw.rect(screen, GRAY,
                                         [game.next_blockX + game.zoom * (j),
                                          game.next_blockY + game.zoom * (i), game.zoom, game.zoom], 1)
                        p = i * 4 + j
                        if p in game.next_figure.image():
                            pygame.draw.rect(screen, colors[game.next_figure.color],
                                             [game.next_blockX + game.zoom * (j) + 1,
                                              game.next_blockY + game.zoom * (i) + 1,
                                              game.zoom - 2, game.zoom - 2])
        else:
            for i in range(game.height):
                for j in range(game.width):
                    pygame.draw.rect(screen, GRAY,
                                     [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                    if game.field[i][j] > 0:
                        pygame.draw.rect(screen, colors[game.field[i][j]],
                                         [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                                          game.zoom - 1])

            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(screen, colors[game.figure.color],
                                             [game.x + game.zoom * (j + game.figure.x) + 1,
                                              game.y + game.zoom * (i + game.figure.y) + 1,
                                              game.zoom - 2, game.zoom - 2])

            if game.next_figure is not None:
                for i in range(4):
                    for j in range(4):
                        pygame.draw.rect(screen, GRAY,
                                         [game.next_blockX + game.zoom * (j),
                                          game.next_blockY + game.zoom * (i), game.zoom, game.zoom], 1)
                        p = i * 4 + j
                        if p in game.next_figure.image():
                            pygame.draw.rect(screen, colors[game.next_figure.color],
                                             [game.next_blockX + game.zoom * (j) + 1,
                                              game.next_blockY + game.zoom * (i) + 1,
                                              game.zoom - 2, game.zoom - 2])

        font = pygame.font.SysFont('Calibri', 25, True, False)
        font2 = pygame.font.SysFont('Calibri', 13, True, False)
        font1 = pygame.font.SysFont('Calibri', 65, True, False)
        text = font.render("Score: " + str(game.score), True, BLACK)
        text_game_over = font1.render("Game Over", True, (255, 125, 0))
        text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))
        text_next = font2.render("NEXT BLOCK", True, (0, 0, 0))

        screen.blit(text, [0, 0])
        screen.blit(text_next, [game.next_blockX - 10, 180])
        if game.state == "game over":
            screen.blit(text_game_over, [200+20, 200])
            screen.blit(text_game_over1, [200+25, 265])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()