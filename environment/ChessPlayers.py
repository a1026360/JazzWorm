import chess
import numpy as np

from environment.ChessLogic import uci_strings, board_to_fen


class RandomPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        valids_array = []
        for i, vm in enumerate(valids):
            if vm == 1:
                valids_array.append(i)
        a = np.random.randint(len(valids_array))
        return valids_array[a]


class HumanChessPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        fen = board_to_fen(board)
        chess_board = chess.Board(fen)
        print(str(chess_board))
        valid = self.game.getValidMoves(board, 1)
        for i, vm in enumerate(valid):
            if vm == 1:
                print(uci_strings[i])
        while True:
            a = input()
            a = uci_strings.index(str(a))
            if valid[a]:
                break
            else:
                print('Invalid')
        return a
