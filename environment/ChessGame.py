from __future__ import print_function

from typing import Any, Tuple

import numpy as np

import chess
from Game import Game
from .ChessLogic import board_to_array, board_to_fen, uci_strings, pawn_chess_ending_mapping
import logging
import coloredlogs

log = logging.getLogger(__name__)

fileHandler = logging.FileHandler("training.log")
log.addHandler(fileHandler)

coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.


class ChessGame(Game):
    def __init__(self):
        self.size = [9, 8]
        self.action_size = len(uci_strings)

        # "8/1q3R2/4Q3/1k6/8/8/4RK2/8 w - - 6 4" for CM in 4#
        # "8/1RR5/4Q3/8/8/3k4/5K2/8 w - - 3 7"
        # "7k/6pp/P2P2pq/5p2/8/QP2p2p/PP6/K7 w - - 0 1"
        # "7k/B5pp/P2PN1pq/5p2/2P5/QP1pp1pp/PP6/K7 w - - 0 1"
        # "7k/6pp/6rq/8/8/QR6/PP6/K7 w - - 0 1"
        # "8/8/3k4/8/8/4K3/8/4Q3 w - - 0 1"
        # "6R1/3P4/1K2N2p/7k/8/2r5/rp6/8 w - - 4 46"
        # self.start_fen = chess.Board().fen()
        #self.start_fen = "7k/6pP/pppp2P1/8/8/PPPP2p1/6Pp/7K w - - 0 1"
        #self.start_fen = "7k/ppppp1pP/6P1/8/8/6p1/PPPPP1Pp/7K w - - 0 1"
        self.start_fen = chess.Board().fen()

    def getInitBoard(self) -> Tuple[Any, chess.Board]:
        board = chess.Board(self.start_fen)
        return board_to_array(board), board

    def getBoardSize(self):
        return self.size

    def getActionSize(self):
        return self.action_size

    def getNextState(self, board_array, player, action):
        board_array = self.getCanonicalForm(board_array, player)
        fen = board_to_fen(board_array)
        board = chess.Board(fen)
        if board.is_game_over():
            return board_array, -player
        try:
            board.push(chess.Move.from_uci(uci_strings[action]))
        except AssertionError as ae:
            raise ae
        board_array = board_to_array(board)
        board_array = self.getCanonicalForm(board_array, player)
        return board_array, -player

    def getValidMoves(self, board, player):
        fen = board_to_fen(board)
        board = chess.Board(fen)
        valid_actions = np.zeros(self.action_size)
        for move in board.legal_moves:
            valid_actions[uci_strings.index(str(move))] = 1
        return valid_actions

    def getGameEnded(self, board_array, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        fen = board_to_fen(board_array)
        board = chess.Board(fen)

        result = board.result()
        if result[0] == "*":
            if board_array[8, 2] > 100:
                return -1e-4
            board.turn = False
            if board.result()[0] == "*":
                return 0
        elif result[1] == "/":
            return 1e-4  # return a low number for draws

        return -1

    def getCanonicalForm(self, board, player):
        if player == 1:
            return board
        board = board.copy()
        mirrored_board = board[:-1, :] * player
        flipped_mirrored_borad = np.flip(mirrored_board, axis=0)
        board[:-1, :] = flipped_mirrored_borad
        b_castle = board[8, 5:7].copy()
        board[8, 5:7] = board[8, 3:5].copy()
        board[8, 3:5] = b_castle
        board[8, 0] = 1
        return board

    def getSymmetries(self, board, pi):
        return [(board, pi)]

    def stringRepresentation(self, board):
        return board.tostring()

    @staticmethod
    def display(board):
        fen = board_to_fen(board)
        print(str(fen) + "\n")
