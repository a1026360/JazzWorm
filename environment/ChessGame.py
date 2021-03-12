from __future__ import print_function

import numpy as np

import chess
from Game import Game
from .ChessLogic import board_to_array, board_to_fen, uci_strings


class ChessGame(Game):
    def __init__(self):
        self.size = 8
        self.action_size = 1968
        self.i = 0

    def getInitBoard(self):
        board = chess.Board()
        return board_to_array(board)

    def getBoardSize(self):
        return self.size, self.size

    def getActionSize(self):
        return self.action_size

    def getNextState(self, board, player, action):
        self.i += 1
        print(f"i = {self.i}")
        fen = board_to_fen(board, player, 0)
        board = chess.Board(fen)
        if board.is_game_over():
            return board, -player
        board.push(chess.Move.from_uci(uci_strings[action]))
        return board_to_array(board), -player

    def getValidMoves(self, board, player):
        fen = board_to_fen(board, player, 0)
        board = chess.Board(fen)
        valid_actions = np.zeros(self.action_size)
        for move in board.legal_moves:
            valid_actions[uci_strings.index(str(move))] = 1
        return valid_actions

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        fen = board_to_fen(board, player, 0)
        board = chess.Board(fen)
        if board.is_game_over():
            if not board.is_checkmate():
                return 1e-4
            return -player
        return 0

    def getCanonicalForm(self, board, player):
        return board

    def getSymmetries(self, board, pi):
        return []

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    @staticmethod
    def display(board):
        print(board)
