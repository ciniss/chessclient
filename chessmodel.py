import chess
from copy import deepcopy
class ChessModel:
    def __init__(self):
        self.humanPlayer = False
        self.game = chess.Board()
    def validateMove(self,move):
        if chess.Move.from_uci('a8a1') in self.game.legal_moves:
            print("Moved "+ move)
            #push to database
            #recieve FEN
            FEN=""
            self.game.set_fen(FEN)
            return FEN
