from sre_parse import State
import pygame
import random
#import usb
#from practicum import find_mcu_boards, McuBoard, PeriBoard
from Tetris import Tetris,Figure

def multi_play(colors, screen):
    pygame.mixer.music.load("./PracticumProject-TetrisGame/audio/BGM InGame.mp3")
    pygame.mixer.music.play(-1)
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
    game1 = Tetris(20, 10)
    game1.x += 400
    game1.next_blockX += 400
    counter = 0

    pressing_down1 = False

    #light_min1 = peri1.get_light()

    check_up1 = 1
    check_left1 = 1
    check_right1 = 1

    pressing_down = False

   # light_min = peri.get_light()

    check_up = 1
    check_left = 1
    check_right = 1

    font_socre = pygame.font.SysFont('Calibri', 32, True, False)
    font_game_over = pygame.font.SysFont('Calibri',72 , True, False)
    font_press = pygame.font.SysFont('Calibri',44 , True, False)
    font_next = pygame.font.SysFont('Calibri', 14, True, False)
    
    text_game_over = font_game_over.render("Game Over", True, (255, 125, 0))
    text_press_right = font_press.render("Press right : Play again", True, (255, 215, 0))
    text_press_left = font_press.render("Press left   : Return to menu", True, (255, 215, 0))
    text_next = font_next.render("NEXT BLOCK",True, WHITE)
    

    game.state = "start"
    game1.state = "start"
    while not done:
        text_score = font_socre.render("Score: " + str(game.score), True, WHITE)
        text1_score = font_socre.render("Score: " + str(game1.score), True, WHITE)
        '''
        if game1.state == "calibrate":
            if peri1.get_down():
                light_min1 = peri1.get_light()
                game1.state = "start"
        '''
        if game1.figure is None:
            game1.figure = Figure(3, 0)
            game1.next_figure = Figure(3, 0)

        if game.state == "calibrate":
            if peri.get_down():
                light_min = peri.get_light()
                game.state = "start"

        if game.figure is None:
            game.figure = Figure(3,0)
            game.next_figure = Figure(3,0)

        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game1.level // 2) == 0 or pressing_down1:
            if game1.state == "start" or game1.state == "obstacle":
                game1.go_down()

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start" or game.state == "obstacle":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if game1.state == "game over" and game.state == "game over":
                    if event.key == pygame.K_RIGHT:
                        game.__init__(20, 10)
                        game1.__init__(20, 10)
                    if event.key == pygame.K_LEFT:
                        pygame.mixer.music.load("./audio/BGM Menu.mp3")
                        pygame.mixer.music.play(-1)
                        return
                if game1.state != "game over":
                    if event.key == pygame.K_UP:
                        game1.rotate()
                    if event.key == pygame.K_DOWN:
                        pressing_down1 = True
                    if event.key == pygame.K_LEFT:
                        game1.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        game1.go_side(1)

                if game.state != "game over":
                    if event.key == pygame.K_w:
                        game.rotate()
                    if event.key == pygame.K_s:
                        pressing_down = True
                    if event.key == pygame.K_a:
                        game.go_side(-1)
                    if event.key == pygame.K_d:
                        game.go_side(1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    pressing_down = False
                if event.key == pygame.K_DOWN:
                    pressing_down1 = False
        '''
        if game1.state == "start" or game1.state == "obstacle":
            if peri1.get_light() >= 0.5*light_min1:
                if peri1.get_up() and check_up1:
                    game1.rotate()
                    check_up1 = 0
                if peri1.get_down():
                    pressing_down1 = True
                if peri1.get_left() and check_left1:
                    game1.go_side(-1)
                    check_left1 = 0
                if peri1.get_right() and check_right1:
                    game1.go_side(1)
                    check_right1 = 0

                if not peri1.get_up():
                    check_up1 = 1
                if not peri1.get_left():
                    check_left1 = 1
                if not peri1.get_right():
                    check_right1 = 1

                if not peri1.get_down():
                    pressing_down1 = False

        if game.state == "start" or game.state == "obstacle":
            if peri.get_light() >= 0.5*light_min:
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
        if game1.state == "game over" and game.state == "game over":
            if peri.get_right() or peri1.get_right():
                game.__init__(20, 10)
                game1.__init__(20, 10)

            if peri.get_left() or peri1.get_left():
                return
        '''
        screen.fill(BLACK)
        if game1.state != 'game over':
            screen.blit(text1_score, [400, 0])
            screen.blit(text_next, [game1.next_blockX,180])

            if game1.state == "obstacle":
                a = peri1.get_light()
                if a <= 0.5*light_min1:
                    game1.state = "start"
                    print(a, light_min1)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

                for i in range(game1.height):
                    for j in range(game1.width):
                        pygame.draw.rect(screen, GRAY, [game1.x + game1.zoom * j, game1.y + game1.zoom * i, game1.zoom, game1.zoom], 1)
                        pygame.draw.rect(screen, YELLOW,
                                        [game1.x + game1.zoom * j + 1, game1.y + game1.zoom * i + 1, game1.zoom - 2, game1.zoom - 1])

                if game1.figure is not None:
                    for i in range(4):
                        for j in range(4):
                            p = i * 4 + j
                            if p in game1.figure.image():
                                pygame.draw.rect(screen, colors[game1.figure.color],
                                                [game1.x + game1.zoom * (j + game1.figure.x) + 1,
                                                game1.y + game1.zoom * (i + game1.figure.y) + 1,
                                                game1.zoom - 2, game1.zoom - 2])
                if game1.next_figure is not None:
                    for i in range(4):
                        for j in range(4):
                            pygame.draw.rect(screen, GRAY,
                                            [game1.next_blockX + game1.zoom * (j) ,
                                            game1.next_blockY + game1.zoom * (i) , game1.zoom, game1.zoom], 1)
                            p = i * 4 + j
                            if p in game1.next_figure.image():
                                pygame.draw.rect(screen, colors[game1.next_figure.color],
                                                [game1.next_blockX + game1.zoom * (j) + 1,
                                                game1.next_blockY + game1.zoom * (i) + 1,
                                                game1.zoom - 2, game1.zoom - 2])
            else:
                for i in range(game1.height):
                    for j in range(game1.width):
                        pygame.draw.rect(screen, GRAY, [game1.x + game1.zoom * j, game1.y + game1.zoom * i, game1.zoom, game1.zoom], 1)
                        if game1.field[i][j] > 0:
                            pygame.draw.rect(screen, colors[game1.field[i][j]],
                                            [game1.x + game1.zoom * j + 1, game1.y + game1.zoom * i + 1, game1.zoom - 2, game1.zoom - 1])

                if game1.figure is not None:
                    for i in range(4):
                        for j in range(4):
                            p = i * 4 + j
                            if p in game1.figure.image():
                                pygame.draw.rect(screen, colors[game1.figure.color],
                                                [game1.x + game1.zoom * (j + game1.figure.x) + 1,
                                                game1.y + game1.zoom * (i + game1.figure.y) + 1,
                                                game1.zoom - 2, game1.zoom - 2])
                if game1.next_figure is not None:
                    for i in range(4):
                        for j in range(4):
                            pygame.draw.rect(screen, GRAY,
                                            [game1.next_blockX + game1.zoom * (j) ,
                                            game1.next_blockY + game1.zoom * (i) , game1.zoom, game1.zoom], 1)
                            p = i * 4 + j
                            if p in game1.next_figure.image():
                                pygame.draw.rect(screen, colors[game1.next_figure.color],
                                                [game1.next_blockX + game1.zoom * (j) + 1,
                                                game1.next_blockY + game1.zoom * (i) + 1,
                                                game1.zoom - 2, game1.zoom - 2])
        elif game1.state == 'game over':
            font_socre = pygame.font.SysFont('Calibri', 44, True, False)
            text1_socre= font_socre.render("Score: " + str(game1.score), True, WHITE)
            screen.blit(text1_socre, [400, 0])        
            screen.blit(text_game_over, [420, 150])

        if game.state != 'game over':
            screen.blit(text_score, [0, 0])
            screen.blit(text_next, [game.next_blockX,180])

            if game.state == "obstacle":
                a = peri.get_light()
                if a <= 0.5*light_min:
                    game.state = "start"
                    print(a, light_min)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

                for i in range(game.height):
                    for j in range(game.width):
                        pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j,game.y + game.zoom * i, game.zoom, game.zoom], 1)
                        pygame.draw.rect(screen, YELLOW,
                                            [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

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
                                            [game.next_blockX +game.zoom * (j) ,
                                            game.next_blockY +  game.zoom * (i) , game.zoom, game.zoom], 1)
                            p = i * 4 + j
                            if p in game.next_figure.image():
                                pygame.draw.rect(screen, colors[game.next_figure.color],
                                                [game.next_blockX +game.zoom * (j) + 1,
                                                game.next_blockY +  game.zoom * (i) + 1,
                                                game.zoom - 2, game.zoom - 2])
            else:
                for i in range(game.height):
                    for j in range(game.width):
                        pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j,game.y + game.zoom * i, game.zoom, game.zoom], 1)
                        if game.field[i][j] > 0:
                            pygame.draw.rect(screen, colors[game.field[i][j]],
                                            [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

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
                                            [game.next_blockX +game.zoom * (j) ,
                                            game.next_blockY +  game.zoom * (i) , game.zoom, game.zoom], 1)
                            p = i * 4 + j
                            if p in game.next_figure.image():
                                pygame.draw.rect(screen, colors[game.next_figure.color],
                                                [game.next_blockX +game.zoom * (j) + 1,
                                                game.next_blockY +  game.zoom * (i) + 1,
                                                game.zoom - 2, game.zoom - 2])
        elif game.state == 'game over':
            font_socre = pygame.font.SysFont('Calibri', 44, True, False)
            text_socre= font_socre.render("Score: " + str(game.score), True, WHITE)
            screen.blit(text_socre, [0, 0])        
            screen.blit(text_game_over, [20, 150])
            
        if game.state == "game over" and game1.state == "game over":
            screen.blit(text_press_right, [150, 250])
            screen.blit(text_press_left, [150, 300])

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()