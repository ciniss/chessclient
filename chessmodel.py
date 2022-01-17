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

    def FENdecoder(self) -> list:
        retArr = [[], [], [], [], [], [], [], []]
        ptr = 0
        for character in self.FEN:
            if character == ' ':
                break
            if character != '/':
                if character.isnumeric():
                    for i in range(int(character)):
                        retArr[7 - ptr // 8].append('X')
                    ptr += int(character)
                else:
                    retArr[7 - ptr // 8].append(character)
                    ptr += 1

        return retArr
