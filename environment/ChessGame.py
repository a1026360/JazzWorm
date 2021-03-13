from __future__ import print_function

import numpy as np

import chess
from Game import Game
from .ChessLogic import board_to_array, board_to_fen, uci_strings
import logging
import coloredlogs

log = logging.getLogger(__name__)

coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.


class ChessGame(Game):
    def __init__(self):
        self.size = [9, 8]
        self.action_size = 1968
        self.seen_moves = 0
        self.highest_move = 0
        self.seen_results = [0, 0, 0]

    def getInitBoard(self):
        board = chess.Board()
        return board_to_array(board)

    def getBoardSize(self):
        return self.size

    def getActionSize(self):
        return self.action_size

    def getNextState(self, board_array, player, action):
        self.seen_moves += 1
        move_number = int(board_array[8, 1])
        if move_number > self.highest_move:
            self.highest_move = move_number
        if self.seen_moves % 200 == 0:
            log.info(f"highest_move; seen moves / results: "
                     f"{self.highest_move};\t{self.seen_moves}\t / {self.seen_results}")
        fen = board_to_fen(board_array)
        board = chess.Board(fen)
        if board.is_game_over():
            return board, -player
        try:
            board.push(chess.Move.from_uci(uci_strings[action]))
        except AssertionError as ae:
            raise ae
        board_array = board_to_array(board)
        return board_array, -player

    def getValidMoves(self, board, player):
        fen = board_to_fen(board)
        board = chess.Board(fen)
        valid_actions = np.zeros(self.action_size)
        for move in board.legal_moves:
            valid_actions[uci_strings.index(str(move))] = 1
        return valid_actions

    @staticmethod
    def quick_end(board):
        move_number = int(board[8, 1])
        if move_number > 5:
            return 1
        return 0

    def getGameEnded(self, board, player):
        # test quick ending
        return self.quick_end(board)

        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        fen = board_to_fen(board)
        board = chess.Board(fen)
        result = board.result()
        if result[0] == "*":
            return 0
        elif result[1] == "/":
            self.seen_results[2] = self.seen_results[2] + 1
            return 1e-4  # return a low number for draws
        elif result[0] == "1":
            self.seen_results[0] = self.seen_results[0] + 1
            return 1
        self.seen_results[1] = self.seen_results[1] + 1
        return -1

    def getCanonicalForm(self, board, player):
        return board
        # use this code if mirroring is necessary:
        # if player == 1:
        #    return board
        # fen = board_to_fen(board)
        # board = chess.Board(fen)
        # return board_to_array(board.mirror())

    def getSymmetries(self, board, pi):
        return [(board, pi)]

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    @staticmethod
    def display(board):
        fen = board_to_fen(board)
        board = chess.Board(fen)
        print(board + "\n")
