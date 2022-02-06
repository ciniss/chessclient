import chess
from copy import deepcopy


class ChessModel:
    def __init__(self):
        self.humanPlayer = False
        self.game = chess.Board()
        self.FEN = chess.STARTING_FEN

    def validateMove(self, move):
        if chess.Move.from_uci('a8a1') in self.game.legal_moves:
            print("Moved " + move)
            # push to database
            # recieve FEN
            FEN = ""
            self.game.set_fen(FEN)
            return FEN


def isWhite(FEN):
    for i in range(len(FEN)):
        if FEN[i] == ' ':
            return True if FEN[i + 1] == 'w' else False
    return True


def FENdecoder(FEN) -> list:
    retArr = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
    ptr = 0
    for character in FEN:
        if character == ' ':
            break
        if character != '/':
            if character.isnumeric():
                for i in range(int(character)):
                    retArr[7 - ptr // 8][ptr % 8] = 'X'
                    ptr += 1
            else:
                retArr[7 - ptr // 8][ptr % 8] = character
                ptr += 1

    return retArr
