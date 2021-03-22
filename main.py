import logging

import coloredlogs

from Coach import Coach
from environment.ChessGame import ChessGame
from environment.keras.NNet import NNetWrapper as nn
from utils import *
import numpy as np

np.random.seed(1408)

log = logging.getLogger(__name__)

coloredlogs.install(level='INFO')  # INFO or other levels. Change this to DEBUG to see more info.

args = TrainingConfig({
    'numIters': 100,
    'numEps': 6,              # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 15,        #
    'updateThreshold': 0.51,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 24,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 8,         # Number of games to play during arena play to determine if new net will be accepted.
    'arenaVerbose': False,         # Show games during arena play.
    'cpuct': 1,

    'checkpoint': './jazz/',
    'load_model': True,
    'load_folder_file': ('./jazz', 'best.h5'),
    'numItersForTrainExamplesHistory': 24,

})


def main():
    log.info('Loading %s...', ChessGame.__name__)
    g = ChessGame()

    log.info('Loading %s...', nn.__name__)
    nnet = nn(g)

    if args.load_model:
        log.info(f'Loading checkpoint "{args.load_folder_file}" ...')
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
    else:
        log.warning('Not loading a checkpoint!')

    log.info('Loading the Coach...')
    c = Coach(g, nnet, args)

    if args.load_model:
        log.info("Loading 'trainExamples' from file ...")
        c.loadTrainExamples()

    log.info('Starting the learning process ...')
    c.learn()


if __name__ == "__main__":
    main()
