# SIM and Alpha Zero General
by Paul Puntschart, May 2021

## Experiments

### Training Notes
Following my training notes to some trained neural networks.
* checkpoint numbers (e.g. checkpoint_14) are NOT linear to training durations, because I changed some training hyperparameters now and then. Details can still be reverse-engineered via the git commits.


#### 2h Training
After 2h of training, I got following results:

* checkpoint_30 results vs AlgoPlayer:

```
Arena.playGames (1): 100%| 100/100 [05:35<00:00,  3.35s/it]

Player1 begins: ( 86, 14, 86% )

Arena.playGames (2): 100%| 100/100 [03:54<00:00,  2.34s/it]

Player2 begins (100 games): ( 86, 14, 86% )

Player1 vs Player2 (total of 200 games): (172, 28, 86%)
```


#### 1h Training
After 1h of training, I got following results:

* checkpoint_24 results vs AlgoPlayer
  
```
Arena.playGames (1): 100%| 50/50 [02:57<00:00,  3.54s/it]

Player1 begins: ( 39, 11, 78% )

Arena.playGames (2): 100%| 50/50 [02:07<00:00,  2.55s/it]

Player2 begins (50 games): ( 37, 13, 74% )

Player1 vs Player2 (total of 100 games): (76, 24, 76%)
```

* checkpoint_24 was able to beat the RandomPlayer 94 - 6.
* checkpoint_4 (trained for 10 min) was able to beat the RandomPlayer 99 - 1,<br/>but loses 7 - 17 vs checkpoint_24.

#### Initial Model Evaluation
With the second-generation neural network model, I got following results:

* checkpoint_1 results vs AlgoPlayer

```
Arena.playGames (1): 100%| 50/50 [03:15<00:00,  3.90s/it]

Player1 begins: ( 34, 16, 68% )

Arena.playGames (2): 100%| 50/50 [02:41<00:00,  3.22s/it]

Player2 begins (50 games): ( 41, 9, 82% )

Player1 vs Player2 (total of 100 games): (75, 25, 75%)
```

this is already very interesting, because the second-generation model wins 75% against the AlgoPlayer. So it is already better than the 1-action-look-ahead intelligence (see chapter AlgoPlayer).


* checkpoint_1 (second generation) was able to beat the RandomPlayer 46 - 4.


### RandomPlayer vs RandomPlayer
Stats are given as Tuple: (Player1 wins, Player2 wins).<br/>
Running 1 million games with two RandomPlayer resulted in:
```
Arena.playGames (1): 100%| 500000/500000 [07:07<00:00, 1168.89it/s]
Arena.playGames (2): 100%| 500000/500000 [07:16<00:00, 1144.61it/s]
(499148, 500852)
```
which means their win chances are equal.

### AlgoPlayer vs RandomPlayer
Stats are given as Tuple: (Player1 wins, Player2 wins).<br/>
Running 100k games with AlgoPlayer vs RandomPlayer resulted in:

```
(88150, 11850)
```
which is a win rate of 88%.


### AlgoPlayer vs AlgoPlayer
Stats are given as Tuple: (Player1 wins, Player2 wins).<br/>
Running 100k games with two AlgoPlayers resulted in:

```
Arena.playGames (1): 100%| 50000/50000 [01:26<00:00, 579.51it/s]
Arena.playGames (2): 100%| 50000/50000 [01:27<00:00, 574.35it/s]
(49983, 50017)
```
which means their win chances are equal.

## Players
Following all my developed SIM players

### RandomPlayer
Chooses actions randomly. Stupid, but useful to create baselines (e.g. to measure how good the AlgoPlayer performs vs the RandomPlayer, see chapter "AlgoPlayer vs RandomPlayer").

### AlgoPlayer
Performs a 1-action-look-ahead. This means the AlgoPlayer will not choose an action that instantly looses the game (if such an action exists). If there are more than one actions that will not loose the game instantly, the AlgoPlayer will choose one of those actions randomly.