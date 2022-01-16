import pygame
import random
from guiInputText import InputBox

pygame.init()
size = (1600, 800)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")

# COLORS
C_BACKGROUND = (0, 0, 0)
C_BLACK = (12, 24, 56)
C_WHITE = (145, 170, 57)

carryOn = True
clock = pygame.time.Clock()

game_str = ""

is_login = True
is_scoreboard = False
is_gameselect = False
is_game = False
input_login_login = InputBox(900, 300, 300, 100, "NICK")
input_login_password = InputBox(900, 400, 300, 100, "PASSWORD")
input_register_login = InputBox(1200, 200, 300, 100, "NICK")
input_register_password = InputBox(1200, 300, 300, 100, "PASSWORD")
input_register_email = InputBox(1200, 400, 400, 100, "EMAIL")

input_join_by_id = InputBox(900, 300, 300, 100, "ID")

login_input_boxes = [input_login_login, input_login_password, input_register_login, input_register_password,
                     input_register_email]
game_select_input_boxes = [input_join_by_id]

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 30)


def isMouseInRegion(mx, my, rx1, ry1, rx2, ry2):
    if rx1 < mx < rx1 + rx2 and ry1 < my < ry1 + ry2:
        return True
    return False


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            # login
            if is_login:
                if isMouseInRegion(mousePos[0], mousePos[1], 950, 550, 100, 50):
                    for b in login_input_boxes:
                        b.text = ""
                    is_login = False
                    is_gameselect = True
                # register
                if isMouseInRegion(mousePos[0], mousePos[1], 1200, 550, 200, 50):
                    for b in login_input_boxes:
                        b.text = ""
                    is_login = False
                    is_gameselect = True
            elif is_gameselect:
                # join
                if isMouseInRegion(mousePos[0], mousePos[1], 950, 550, 100, 50):
                    # create game
                    is_gameselect = False;
                    pass
                    # is_game=True
                # create
                if isMouseInRegion(mousePos[0], mousePos[1], 1200, 550, 200, 50):
                    game_select_input_boxes[0].text = random.randint(0, 1000)
                #scoreboard
                if isMouseInRegion(mousePos[0], mousePos[1],  950, 625, 325, 50):
                    is_gameselect=False
                    is_scoreboard=True

        for box in login_input_boxes:
            box.handle_event(event)
        for box in game_select_input_boxes:
            box.handle_event(event)
    screen.fill(C_BACKGROUND)

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, C_WHITE, pygame.Rect(100 * i, 100 * j, 100, 100))
            else:
                pygame.draw.rect(screen, C_BLACK, pygame.Rect(100 * i, 100 * j, 100, 100))
    if is_login:
        for box in login_input_boxes:
            box.draw(screen)
        for box in login_input_boxes:
            box.update()

        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(950, 550, 100, 50))
        textsurface = font.render("LOGIN", False, (0, 0, 0))
        screen.blit(textsurface, (950, 550))
        textsurface = font.render("REGISTER", False, (0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1200, 550, 200, 50))
        screen.blit(textsurface, (1220, 550))
    if is_gameselect:
        for box in game_select_input_boxes:
            box.update()
        for box in game_select_input_boxes:
            box.draw(screen)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(950, 550, 100, 50))
        textsurface = font.render("JOIN", False, (0, 0, 0))
        screen.blit(textsurface, (950, 550))
        textsurface = font.render("CREATE", False, (0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1200, 550, 200, 50))
        screen.blit(textsurface, (1220, 550))
        textsurface = font.render("SHOW SCOREBOARD", False, (0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(950, 625, 325, 50))
        screen.blit(textsurface, (950, 625))
    pygame.display.flip()
    clock.tick(60)
