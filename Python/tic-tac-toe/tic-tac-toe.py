import pygame

pygame.init()
pygame.font.init()

board = {
    (250, 50): None, (450, 50): None, (650, 50): None,
    (250, 250): None, (450, 250): None, (650, 250): None,
    (250, 450): None, (450, 450): None, (650, 450): None
}

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.display.set_caption("Tic-Tac-Toe")
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
XO_font = pygame.font.SysFont("Comic Sans MS", 200)
text_font = pygame.font.SysFont("Arial", 50)
player = "X"
winner = None

while True:
    
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:

                if not winner:

                    if mouse_pos[0] in list(x for x in range(203, 398)) and mouse_pos[1] in list(y for y in range(198)):
                        if not board[list(board)[0]]:
                            if player == "X":
                                board[list(board)[0]] = "X"
                                player = "O"
                            else:
                                board[list(board)[0]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(403, 598)) and mouse_pos[1] in list(y for y in range(198)):
                        if not board[list(board)[1]]:
                            if player == "X":
                                board[list(board)[1]] = "X"
                                player = "O"
                            else:
                                board[list(board)[1]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(603, 800)) and mouse_pos[1] in list(y for y in range(198)):
                        if not board[list(board)[2]]:
                            if player == "X":
                                board[list(board)[2]] = "X"
                                player = "O"
                            else:
                                board[list(board)[2]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(203, 398)) and mouse_pos[1] in list(y for y in range(203, 398)):
                        if not board[list(board)[3]]:
                            if player == "X":
                                board[list(board)[3]] = "X"
                                player = "O"
                            else:
                                board[list(board)[3]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(403, 598)) and mouse_pos[1] in list(y for y in range(203, 398)):
                        if not board[list(board)[4]]:
                            if player == "X":
                                board[list(board)[4]] = "X"
                                player = "O"
                            else:
                                board[list(board)[4]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(603, 800)) and mouse_pos[1] in list(y for y in range(203,398)):
                        if not board[list(board)[5]]:
                            if player == "X":
                                board[list(board)[5]] = "X"
                                player = "O"
                            else:
                                board[list(board)[5]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(203, 398)) and mouse_pos[1] in list(y for y in range(403, 600)):
                        if not board[list(board)[6]]:
                            if player == "X":
                                board[list(board)[6]] = "X"
                                player  = "O"
                            else:
                                board[list(board)[6]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(403, 598)) and mouse_pos[1] in list(y for y in range(403, 600)):
                        if not board[list(board)[7]]:
                            if player == "X":
                                board[list(board)[7]] = "X"
                                player = "O"
                            else:
                                board[list(board)[7]] = "O"
                                player = "X"

                    if mouse_pos[0] in list(x for x in range(603, 800)) and mouse_pos[1] in list(y for y in range(403, 600)):
                        if not board[list(board)[8]]:
                            if player == "X":
                                board[list(board)[8]] = "X"
                                player = "O"
                            else:
                                board[list(board)[8]] = "O"
                                player = "X"

    gameDisplay.fill(white)
    pygame.draw.line(gameDisplay, black, (200, 200), (800, 200), 4)
    pygame.draw.line(gameDisplay, black, (200, 400), (800, 400), 4)
    pygame.draw.line(gameDisplay, black, (400, 0), (400, 600), 4)
    pygame.draw.line(gameDisplay, black, (600, 0), (600, 600), 4)
    
    for i in board:
        if board[i]:
            gameDisplay.blit(XO_font.render(board[i], False, black), i)

    if board[(250, 50)] == board[(450, 50)] == board[(650, 50)] and board[(250, 50)] != None:
        winner = board[(250, 50)]

    if board[(250, 250)] == board[(450, 250)] == board[(650, 250)] and board[(250, 250)] != None:
        winner = board[(250, 250)]

    if board[(250, 450)] == board[(450, 450)] == board[(650, 450)] and board[(250, 450)] != None:
        winner = board[(250, 450)]

    if board[(250, 50)] == board[(250, 250)] == board[(250, 450)] and board[(250, 50)] != None:
        winner = board[(250, 50)]

    if board[(450, 50)] == board[(450, 250)] == board[(450, 450)] and board[(450, 50)] != None:
        winner = board[(450, 50)]

    if board[(650, 50)] == board[(650, 250)] == board[(650, 450)] and board[(650, 50)] != None:
        winner = board[(650, 50)]

    if board[(250, 50)] == board[(450, 250)] == board[(650, 450)] and board[(250, 50)] != None:
        winner = board[(250, 50)]

    if board[(650, 50)] == board[(450, 250)] == board[(250, 450)] and board[(650, 50)] != None:
        winner = board[(650, 50)]

    if winner:
        gameDisplay.blit(text_font.render("Game over", False, red), (380, 275))

    pygame.display.update()

    clock.tick(60)