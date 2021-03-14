import Arena
from MCTS import MCTS
from environment.ChessGame import ChessGame
from environment.keras.NNet import NNetWrapper as NNet
from environment.ChessPlayers import *

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

human_vs_cpu = False
human_vs_rnd = True

g = ChessGame()

# all players
rp = RandomPlayer(g).play
hp = HumanChessPlayer(g).play

# nnet players
n1 = NNet(g)
n1.load_checkpoint('./jazz/', 'checkpoint.h5')
args1 = TrainingConfig({'numMCTSSims': 50, 'cpuct': 1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

if human_vs_cpu:
    player2 = hp
elif human_vs_rnd:
    player2 = rp
else:
    n2 = NNet(g)
    n2.load_checkpoint('./jazz/', 'checkpoint_18.h5')
    args2 = TrainingConfig({'numMCTSSims': 50, 'cpuct': 1.0})
    mcts2 = MCTS(g, n2, args2)
    n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

    player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

arena = Arena.Arena(n1p, player2, g, display=ChessGame.display)

print(arena.playGames(10, verbose=False))
