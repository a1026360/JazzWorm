# SIM and Alpha Zero General
by Paul Puntschart, May 2021

## Introduction
Hy, my name is Paul and I love teaching my computer to learn all kind of games. 

Over the last years, I already trained my computer to play "TicTacToe", 
"Jungle" (also known as "Dou Shou Qi"), "Chess", 
"Paul's Bauernschach" (a self invented chess variation with only pawns) 
and "The Catata Fish Game" (a self invented game), and then, one week ago, 
I stumbled upon the pen and paper game "SIM". 

SIM is so easy to explain and so easy to play that I 
instantly fell in love with it. I programmed it on one evening in Python and 
let my computer play and learn it over night.

My setup is the XMG Zenith Laptop with an Intel(R) Core(TM) i7-8700 
CPU @ 3.20GHz CPU and the NVIDIA GeForce GTX 1080 GPU 
(and yes, this crazy laptop contains desktop-pc devices).

## Experiments
I used this readme to write down all my findings. Happy findings!

### Training Notes
Following my training notes to some trained neural networks playing SIM.
* checkpoint numbers (e.g. checkpoint_14) are NOT linear to training durations, because I changed some training hyperparameters now and then. Details could still be reverse-engineered via the git commits.
* The player making the fist move is referred as "red", the other player as "blue".

#### 15h Training
After 15h of training, I got following results:

* checkpoint_182 vs AlgoPlayer:

```
Arena.playGames (1): 100%| 100/100 [05:15<00:00,  3.15s/it]
Arena.playGames (2): 100%| 100/100 [02:21<00:00,  1.41s/it]

Player1 begins (100 games): ( 93, 7, 93% )
Player2 begins (100 games): ( 99, 1, 99% )
Player1 vs Player2 (total of 200 games): (192, 8, 96%)

Arena.playGames (1): 100%| 500/500 [18:53<00:00,  2.27s/it]
Arena.playGames (2): 100%| 500/500 [04:22<00:00,  1.91it/s]

Player1 begins (500 games): ( 467, 33, 93% )
Player2 begins (500 games): ( 497, 3, 99% )
Player1 vs Player2 (total of 1000 games): (964, 36, 96%)
```

* checkpoint_182 vs checkpoint_148:

```
Arena.playGames (1): 100%| 200/200 [04:21<00:00,  1.31s/it]
Arena.playGames (2): 100%| 200/200 [02:26<00:00,  1.36it/s]

Player1 begins (200 games): ( 79, 121, 40% )
Player2 begins (200 games): ( 200, 0, 100% )
Player1 vs Player2 (total of 400 games): (279, 121, 70%)
```

#### 11h Training
After 11h of training, I got following results:

* checkpoint_148 vs checkpoint_148:

```
# Run 1 (100 games):
Arena.playGames (1): 100%| 32/32 [01:26<00:00,  2.70s/it]
Arena.playGames (2): 100%| 32/32 [00:57<00:00,  1.81s/it]
Arena.playGames (1): 100%| 18/18 [01:01<00:00,  3.44s/it]
Arena.playGames (2): 100%| 18/18 [00:34<00:00,  1.93s/it]

Player1 begins (50 games): ( 4, 46, 8% )
Player2 begins (50 games): ( 47, 3, 94% )
Player1 vs Player2 (total of 100 games): (51, 49, 51%)

# Run 2 (100 games):
Arena.playGames (1): 100%| 50/50 [01:58<00:00,  2.37s/it]
Arena.playGames (2): 100%| 50/50 [01:10<00:00,  1.41s/it]

Player1 begins (50 games): ( 2, 48, 4% )
Player2 begins (50 games): ( 39, 11, 78% )
Player1 vs Player2 (total of 100 games): (41, 59, 41%)
```
We can see that the NN is way better if playing as blue, with a win rate of 90% over 200 games.
This means, the better the players are, the more likely it is that blue wins.
I issued another 200 games to tighten this assumption:

```
Arena.playGames (1): 100%| 100/100 [03:07<00:00,  1.88s/it]
Arena.playGames (2): 100%| 100/100 [00:59<00:00,  1.67it/s]

Player1 begins (100 games): ( 12, 88, 12% )
Player2 begins (100 games): ( 100, 0, 100% )
Player1 vs Player2 (total of 200 games): (112, 88, 56%)
```
and yes, blue is again winning 94% on 200 games played.
At this point I wondered how the much weaker checkpoint_1 model would perform,
so I also issued 200 games with checkpoint_1 vs checkpoint_1:

```
Arena.playGames (1): 100%| 100/100 [09:09<00:00,  5.49s/it]
Arena.playGames (2): 100%| 100/100 [07:34<00:00,  4.54s/it]

Player1 begins (100 games): ( 46, 54, 46% )
Player2 begins (100 games): ( 68, 32, 68% )
Player1 vs Player2 (total of 200 games): (114, 86, 57%)
```
which shows a win rate of 61% for blue (so it is quite lower compared to checkpoint_148).


* checkpoint_148 results vs AlgoPlayer:

```
Arena.playGames (1): 100%| 100/100 [05:11<00:00,  3.11s/it]
Arena.playGames (2): 100%| 100/100 [02:30<00:00,  1.50s/it]

Player1 begins (100 games): ( 90, 10, 90% )
Player2 begins (100 games): ( 99, 1, 99% )
Player1 vs Player2 (total of 200 games): (189, 11, 94%)


Arena.playGames (1): 100%| 100/100 [05:14<00:00,  3.14s/it]
Arena.playGames (2): 100%| 100/100 [02:23<00:00,  1.44s/it]

Player1 begins (100 games): ( 89, 11, 89% )
Player2 begins (100 games): ( 99, 1, 99% )
Player1 vs Player2 (total of 200 games): (188, 12, 94%)


Arena.playGames (1): 100%| 500/500 [19:57<00:00,  2.39s/it]
Arena.playGames (2): 100%| 500/500 [05:08<00:00,  1.62it/s]

Player1 begins (500 games): ( 454, 46, 91% )
Player2 begins (500 games): ( 494, 6, 99% )
Player1 vs Player2 (total of 1000 games): (948, 52, 95%)
```
so the total score for 1400 games is:
* Playing as Player1 (700 games): ( 633, 67, 90%)
* Playing as Player2 (700 games): ( 692, 8, 99%)
* Player1 vs Player2 (total of 1400 games): (1325, 75, 95%)

We can see that the NN is slightly better if playing as Player2.
There is also a significant difference in the playing time (3.14s vs 1.44s).
I played another 20 games to analyse the playing time and counts of turns played:

```
Game over: Turn  14 Result  1
Game over: Turn  14 Result  1
Game over: Turn  14 Result  1
Game over: Turn  12 Result  1
Game over: Turn  14 Result  1
Game over: Turn  14 Result  1
Game over: Turn  14 Result  1
Game over: Turn  12 Result  1
Game over: Turn  14 Result  1
Game over: Turn  14 Result  1

Game over: Turn  13 Result  -1
Game over: Turn  15 Result  -1
Game over: Turn  13 Result  -1
Game over: Turn  13 Result  -1
Game over: Turn  13 Result  -1
Game over: Turn  13 Result  -1
Game over: Turn  15 Result  -1
Game over: Turn  13 Result  -1
Game over: Turn  15 Result  -1
Game over: Turn  15 Result  -1
```
this shows that if the NN plays as Player1, he normally needs 7 turns to win,<br>
but as Player2, he normally only needs 5 turns. This is the reason why those games are played faster.

* checkpoint_148 results vs RandomPlayer:

```
Arena.playGames (1): 100%| 50/50 [02:45<00:00,  3.31s/it]
Arena.playGames (2): 100%| 50/50 [01:22<00:00,  1.65s/it]

Player1 begins (50 games): ( 49, 1, 98% )
Player2 begins (50 games): ( 50, 0, 100% )
Player1 vs Player2 (total of 100 games): (99, 1, 99%)
```


#### 2h Training
After 2h of training, I got following results:

* checkpoint_40 results vs AlgoPlayer:

```
Arena.playGames (1): 100%| 100/100 [05:35<00:00,  3.35s/it]
Arena.playGames (2): 100%| 100/100 [03:54<00:00,  2.34s/it]

Player1 begins: ( 86, 14, 86% )
Player2 begins (100 games): ( 86, 14, 86% )
Player1 vs Player2 (total of 200 games): (172, 28, 86%)
```


#### 1h Training
After 1h of training, I got following results:

* checkpoint_24 results vs AlgoPlayer
  
```
Arena.playGames (1): 100%| 50/50 [02:57<00:00,  3.54s/it]
Arena.playGames (2): 100%| 50/50 [02:07<00:00,  2.55s/it]

Player1 begins: ( 39, 11, 78% )
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
Arena.playGames (2): 100%| 50/50 [02:41<00:00,  3.22s/it]

Player1 begins: ( 34, 16, 68% )
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

Player1 vs Player2 (total of 1000000 games): (499148, 500852, 50%)
```
which means their win chances are equal.

### AlgoPlayer vs RandomPlayer
Stats are given as Tuple: (Player1 wins, Player2 wins).<br/>
Running 100k games with AlgoPlayer vs RandomPlayer resulted in:

```
Player1 vs Player2 (total of 100000 games): (88150, 11850, 88%)
```
which is a win rate of 88%.


### AlgoPlayer vs AlgoPlayer
Stats are given as Tuple: (Player1 wins, Player2 wins).<br/>
Running 100k games with two AlgoPlayers resulted in:

```
Arena.playGames (1): 100%| 50000/50000 [01:27<00:00, 571.62it/s]
Arena.playGames (2): 100%| 50000/50000 [01:26<00:00, 575.54it/s]

Player1 begins (50000 games): ( 25279, 24721, 51% )
Player2 begins (50000 games): ( 24640, 25360, 49% )
Player1 vs Player2 (total of 100000 games): (49919, 50081, 50%)
```
which means their win chances are equal.

## Players
Following all my developed SIM players

### RandomPlayer
Chooses actions randomly. Stupid, but useful to create baselines 
(e.g. to measure how good the AlgoPlayer performs vs the RandomPlayer,
see chapter "AlgoPlayer vs RandomPlayer").

### AlgoPlayer
Performs a 1-action-look-ahead. This means the AlgoPlayer will 
choose an action that will not instantly loose the game 
(if such an action exists). If there are more than one actions 
that will not loose the game instantly, the AlgoPlayer will choose 
one of those actions randomly.