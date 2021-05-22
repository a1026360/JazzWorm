import numpy as np

from sim.SimGame import SimGame


class RandomPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        player = 1
        valids = self.game.getValidMoves(board, player)
        valid_indexes = [i for i, item in enumerate(valids) if item > 0]
        random_action = np.random.choice(valid_indexes)
        return random_action


class AlgoSimPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        player = 1
        valids = self.game.getValidMoves(board, player)
        valid_indexes = [i for i, item in enumerate(valids) if item > 0]
        np.random.shuffle(valid_indexes)
        for valid_action in valid_indexes:
            next_board, _ = self.game.getNextState(board, player, valid_action)
            action_is_losing = self.game.getGameEnded(next_board, player)
            if action_is_losing >= 0:
                return valid_action
        random_action = np.random.choice(valid_indexes)
        return random_action


class HumanSimPlayer:
    def __init__(self, game: SimGame):
        self.game = game

    def play(self, board):
        self.game.display(board)
        valid = self.game.getValidMoves(board, 1)
        for i in range(len(valid)):
            if valid[i]:
                print(self.game.action_index(i))
        while True:
            a = input()
            x, y = [int(x) for x in a.split(' ')]
            a = self.game.action_int(x, y)
            if valid[a]:
                break
            else:
                print('Invalid action input. Try again:')

        return a
