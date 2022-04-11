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

light_min1 = peri1.get_light()

check_up1 = 1
check_left1 = 1
check_right1 = 1

pressing_down = False

light_min = peri.get_light()

check_up = 1
check_left = 1
check_right = 1

while not done:
    if game1.state == "calibrate":
        if peri1.get_down():
            light_min1 = peri1.get_light()
            game1.state = "start"

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
            if game1.state == "game over" and game.state == "game over" and event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)
                game1.__init__(20, 10)

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

    screen.fill(WHITE)

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

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font2 = pygame.font.SysFont('Calibri', 13, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text1 = font.render("Score: " + str(game1.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))
    text_next = font2.render("NEXT BLOCK",True, (0,0,0))

    screen.blit(text, [0, 0])
    screen.blit(text_next, [game.next_blockX-10,180])

    screen.blit(text1, [400, 0])
    screen.blit(text_next, [game1.next_blockX-10,180])

    if game.state == "game over":
        screen.blit(text_game_over, [20, 200])

    if game1.state == "game over":
        screen.blit(text_game_over, [20+400, 200])

    if game.state == "game over" and game1.state == "game over":
        screen.blit(text_game_over1, [200, 265])

    pygame.display.flip()
    clock.tick(fps)