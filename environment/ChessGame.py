from __future__ import print_function

from typing import Any, Tuple

import numpy as np

import chess
from Game import Game
from .ChessLogic import board_to_array, board_to_fen, uci_strings
import logging
import coloredlogs

log = logging.getLogger(__name__)

fileHandler = logging.FileHandler("training.log")
log.addHandler(fileHandler)

coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.


class ChessGame(Game):
    def __init__(self):
        self.size = [9, 8]
        self.action_size = 1968

        # "8/1q3R2/4Q3/1k6/8/8/4RK2/8 w - - 6 4" for CM in 4#
        # "8/1RR5/4Q3/8/8/3k4/5K2/8 w - - 3 7"
        # "7k/6pp/P2P2pq/5p2/8/QP2p2p/PP6/K7 w - - 0 1"
        # "7k/B5pp/P2PN1pq/5p2/2P5/QP1pp1pp/PP6/K7 w - - 0 1"
        # "7k/6pp/6rq/8/8/QR6/PP6/K7 w - - 0 1"
        # "8/8/3k4/8/8/4K3/8/4Q3 w - - 0 1"
        # "6R1/3P4/1K2N2p/7k/8/2r5/rp6/8 w - - 4 46"
        # self.start_fen = chess.Board().fen()
        self.start_fen = chess.Board().fen()

    def getInitBoard(self) -> Tuple[Any, chess.Board]:
        board = chess.Board(self.start_fen)
        return board_to_array(board), board

    def getBoardSize(self):
        return self.size

    def getActionSize(self):
        return self.action_size

    def getNextState(self, board_array, player, action):
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

    def getGameEnded(self, board, player):
        #move_number = int(board[8, 1])

        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        fen = board_to_fen(board)
        board = chess.Board(fen)

        # test quick end
        #if move_number > 12 and not board.turn:
        #    return 1

        result = board.result(claim_draw=True)
        if result[0] == "*":
            return 0
        elif result[1] == "/":
            return 1e-4  # return a low number for draws
        return -1

    def getCanonicalForm(self, board, player):
        return board

    def getSymmetries(self, board, pi):
        return [(board, pi)]

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    @staticmethod
    def display(board):
        fen = board_to_fen(board)
        print(str(fen) + "\n")
