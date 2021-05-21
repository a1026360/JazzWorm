from __future__ import print_function
import sys

from Game import Game
from .SimLogic import Board
import numpy as np

sys.path.append('..')


class SimGame(Game):
    def __init__(self, n=5):
        self.n = n
        self.map = np.zeros((n, n))
        self.init_map()
        self.action_size = int((self.n * (self.n + 1)) / 2)

    def init_map(self):
        i = 0
        for r in range(self.n):
            for c in range(r + 1):
                self.map[r][c] = i
                i += 1

    def action_index(self, action: int):
        match = np.where(self.map == action)
        return match[0][0], match[1][0]

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return self.n, self.n

    def getActionSize(self):
        # return number of actions
        return self.action_size + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.getActionSize() - 1:
            return board, -player
        b = Board(self.n)
        b.pieces = np.copy(board)
        move = self.action_index(action)
        b.execute_move(move, player)
        return b.pieces, -player

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0] * (self.getActionSize())
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves = b.get_legal_moves(player)
        if len(legalMoves) == 0:
            valids[-1] = 1
            return np.array(valids)
        for x, y in legalMoves:
            valids[int(self.map[x][y])] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n)
        b.pieces = np.copy(board)

        if b.is_lost(player):
            return -1
        if b.is_lost(-player):
            return 1
        if b.has_legal_moves():
            return 0
        # draw has a very little value 
        return 1e-4

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player * board

    def getSymmetries(self, board, pi):
        assert len(pi) == self.getActionSize()  # 1 for pass
        return [(board, pi)]

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    @staticmethod
    def display(board):
        n = board.shape[0]

        print("   ", end="")
        for y in range(n):
            print(y, "", end="")
        print("")
        print("  ", end="")
        for _ in range(n):
            print("-", end="-")
        print("--")
        for y in range(n):
            print(y, "|", end="")  # print the row #
            for x in range(n):
                piece = board[y][x]  # get the piece to print
                if piece == -1:
                    print("X ", end="")
                elif piece == 1:
                    print("O ", end="")
                else:
                    if x == n:
                        print("-", end="")
                    else:
                        print("- ", end="")
            print("|")

        print("  ", end="")
        for _ in range(n):
            print("-", end="-")
        print("--")
