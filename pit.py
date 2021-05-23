import Arena
from MCTS import MCTS
from sim.SimGame import SimGame
from sim.keras.NNet import NNetWrapper as NNet
from sim.SimPlayers import *

import numpy as np
from utils import *

nr_of_games_to_play = 1000
verbosity = False

# Player 1 - default: NN
nn_p1 = 'best.h5'
alg_vs = False
random_vs = False

# Player 2 - default: NN
nn_p2 = 'best.h5'
vs_human = False
vs_random = False
vs_alg = True

game = SimGame()

# all players
rp_1 = RandomPlayer(game).play
rp_2 = RandomPlayer(game).play
hp = HumanSimPlayer(game).play
ap_1 = AlgoSimPlayer(game).play
ap_2 = AlgoSimPlayer(game).play

# setup player1
if alg_vs:
    player1 = ap_1
elif random_vs:
    player1 = rp_1
else:
    n1 = NNet(game)
    n1.load_checkpoint('./sim_models/', nn_p1)
    args1 = TrainingConfig({'numMCTSSims': 25, 'cpuct': 1.0})
    mcts1 = MCTS(game, n1, args1)
    player1 = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

# setup player2
if vs_human:
    player2 = hp
elif vs_random:
    player2 = rp_2
elif vs_alg:
    player2 = ap_2
else:
    n2 = NNet(game)
    n2.load_checkpoint('./sim_models/', nn_p2)
    args2 = TrainingConfig({'numMCTSSims': 25, 'cpuct': 1.0})
    mcts2 = MCTS(game, n2, args2)
    player2 = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

arena = Arena.Arena(player1, player2, game, display=SimGame.display)
oneWon, twoWon, draws = arena.playGames(nr_of_games_to_play, verbose=verbosity)
print(f"\nPlayer1 vs Player2 (total of {nr_of_games_to_play} games): "
      f"({oneWon}, {twoWon}, {round(oneWon/nr_of_games_to_play*100)}%)")
