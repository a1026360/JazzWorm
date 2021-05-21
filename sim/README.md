# SIM implementation for Alpha Zero General

Experiments:

Running 1 million games with two RandomPlayer resulted in:

Arena.playGames (1): 100%|██████████| 500000/500000 [07:07<00:00, 1168.89it/s]
Arena.playGames (2): 100%|██████████| 500000/500000 [07:16<00:00, 1144.61it/s]
(499148, 500852, 0)

Training for 1h:

* checkpoint_24 was able to beat the RandomPlayer 94 - 6.
* checkpoint_4 (trained for 10 min) was able to beat the RandomPlayer 99 - 1, but loses 7 - 17 vs checkpoint_24.
* checkpoint_1 (second generation) was able to beat the RandomPlayer 46 - 4.
