import pygame
import random
from guiInputText import InputBox
from chessmodel import ChessModel
import RequestHandler

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

USER_ID = "none"
GAME_ID = "none"

login_input_boxes = [input_login_login, input_login_password, input_register_login, input_register_password,
                     input_register_email]
game_select_input_boxes = [input_join_by_id]

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 30)
font2 = pygame.font.SysFont("Comic Sans MS", 18)

beard = ChessModel()
print(beard.FENdecoder())

piece_set = pygame.image.load("pieceSet2.png")

piece_map = {
    "r": (0, 0, 100, 100),
    "b": (100, 0, 100, 100),
    "q": (200, 0, 100, 100),
    "k": (300, 0, 100, 100),
    "n": (400, 0, 100, 100),
    "p": (500, 0, 100, 100),

    "R": (0, 100, 100, 100),
    "B": (100, 100, 100, 100),
    "Q": (200, 100, 100, 100),
    "K": (300, 100, 100, 100),
    "N": (400, 100, 100, 100),
    "P": (500, 100, 100, 100),
    "X": (0, 0, 0, 0)
}


def isMouseInRegion(mx, my, rx1, ry1, w, h):
    if rx1 < mx < rx1 + w and ry1 < my < ry1 + h:
        return True
    return False


player_white = False

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            # login
            if is_login:
                if isMouseInRegion(mousePos[0], mousePos[1], 950, 550, 100, 50):
                    username = login_input_boxes[0].text
                    password = login_input_boxes[1].text
                    uid = RequestHandler.login(username, password)
                    if uid != "-1":
                        USER_ID = uid
                        is_login = False
                        is_gameselect = True
                # register
                if isMouseInRegion(mousePos[0], mousePos[1], 1200, 550, 200, 50):
                    username = login_input_boxes[2].text
                    password = login_input_boxes[3].text
                    email = login_input_boxes[4].text
                    uid = RequestHandler.register(username, password, email)
                    if uid is not None:
                        USER_ID = uid
                        is_login = False
                        is_gameselect = True
                print(USER_ID)
            elif is_gameselect:
                # join
                if isMouseInRegion(mousePos[0], mousePos[1], 950, 550, 100, 50):
                    # create game
                    gid = game_select_input_boxes[0].text
                    n_gid = RequestHandler.join(gid, USER_ID)
                    if gid == n_gid:
                        GAME_ID = gid
                        is_gameselect = False
                    # is_game=True
                # create
                if isMouseInRegion(mousePos[0], mousePos[1], 1200, 550, 200, 50):
                    game_select_input_boxes[0].set_text(RequestHandler.get_create_game())
                # scoreboard
                if isMouseInRegion(mousePos[0], mousePos[1], 950, 625, 325, 50):
                    is_gameselect = False
                    is_scoreboard = True
            if is_game:
                move = ""
                if isMouseInRegion(mousePos[0], mousePos[1], 0, 0, 800, 800):
                    if player_white:
                        x = mousePos[0] // 100 + 97
                        y = 8 - mousePos[1] // 100
                        move = chr(x) + str(y)
                    else:
                        x = (7 - mousePos[0] // 100) + 97
                        y = mousePos[1] // 100 + 1
                        move = chr(x) + str(y)

        for box in login_input_boxes:
            box.handle_event(event)
        for box in game_select_input_boxes:
            box.handle_event(event)

    screen.fill(C_BACKGROUND)

    indexes = ["abcdefgh", "12345678"]
    # Rendering
    for i in range(8):
        for j in range(8):
            if player_white:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, C_WHITE, pygame.Rect(100 * i, 100 * j, 100, 100))
                    if j == 7:
                        textsurface = font2.render(indexes[0][i], False, C_BLACK)
                        screen.blit(textsurface, (100 * i + 80, 770))
                    if i == 0:
                        textsurface = font2.render(indexes[1][7 - j], False, C_BLACK)
                        screen.blit(textsurface, (10, 100 * j + 10))
                else:
                    pygame.draw.rect(screen, C_BLACK, pygame.Rect(100 * i, 100 * j, 100, 100))
                    if j == 7:
                        textsurface = font2.render(indexes[0][i], False, C_WHITE)
                        screen.blit(textsurface, (100 * i + 80, 770))
                    if i == 0:
                        textsurface = font2.render(indexes[1][7 - j], False, C_WHITE)
                        screen.blit(textsurface, (10, 100 * j + 10))
            else:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, C_WHITE, pygame.Rect(100 * i, 100 * j, 100, 100))
                    if j == 7:
                        textsurface = font2.render(indexes[0][7 - i], False, C_BLACK)
                        screen.blit(textsurface, (100 * i + 80, 770))
                    if i == 0:
                        textsurface = font2.render(indexes[1][j], False, C_BLACK)
                        screen.blit(textsurface, (10, 100 * j + 10))
                else:
                    pygame.draw.rect(screen, C_BLACK, pygame.Rect(100 * i, 100 * j, 100, 100))
                    if j == 7:
                        textsurface = font2.render(indexes[0][7 - i], False, C_WHITE)
                        screen.blit(textsurface, (100 * i + 80, 770))
                    if i == 0:
                        textsurface = font2.render(indexes[1][j], False, C_WHITE)
                        screen.blit(textsurface, (10, 100 * j + 10))
    current_fen = beard.FENdecoder()
    """
        Piece rendering
    """
    for i in range(8):
        for j in range(8):
            if player_white:
                screen.blit(piece_set, (i * 100, j * 100), piece_map[current_fen[7 - j][i]])
            else:
                screen.blit(piece_set, (i * 100, j * 100), piece_map[current_fen[j][7 - i]])

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
            box.draw(screen)
        for box in game_select_input_boxes:
            box.update()

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
