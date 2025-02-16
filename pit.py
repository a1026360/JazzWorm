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

human_vs_nn = False
rnd_vs_nn = True
sf_vs_nn = False

g = ChessGame()

# all players
rp = RandomPlayer(g).play
hp = HumanChessPlayer(g).play
sf = StockfishChessPlayer(g).play

# nnet players
n1 = NNet(g)
n1.load_checkpoint('./jazz/', 'best.h5')
args1 = TrainingConfig({'numMCTSSims': 25, 'cpuct': 1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

# make p1 random player to test:
#n1p = RandomPlayer(g).play
#n1p = sf

if human_vs_nn:
    player2 = hp
elif rnd_vs_nn:
    player2 = rp
elif sf_vs_nn:
    player2 = sf
else:
    n2 = NNet(g)
    n2.load_checkpoint('./jazz/', 'best.h5')
    args2 = TrainingConfig({'numMCTSSims': 25, 'cpuct': 1.0})
    mcts2 = MCTS(g, n2, args2)
    n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

    player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

arena = Arena.Arena(n1p, player2, g, display=ChessGame.display)

print(arena.playGames(10, verbose=False))
