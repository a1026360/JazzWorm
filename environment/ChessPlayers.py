import chess
import chess.engine
import numpy as np

from environment.ChessLogic import uci_strings, board_to_fen


class RandomPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)

        valids_array = []
        for i, vm in enumerate(valids):
            if vm == 1:
                valids_array.append(i)
        len_valids = len(valids_array)
        if len_valids > 0:
            a = np.random.randint(len_valids)
        else:
            print(f"No valid moves in {board}")
            raise ValueError
        return valids_array[a]


class StockfishChessPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        fen = board_to_fen(board)
        chess_board = chess.Board(fen)
        engine = chess.engine.SimpleEngine.popen_uci(
            "B:\development\JazzWorm\sf\stockfish_13_win_x64\stockfish_13_win_x64.exe")

        # timing
        #start = time.time()
        result = engine.play(chess_board, chess.engine.Limit(depth=3))

        #print('SF PREDICTION TIME TAKEN : {0:03f}'.format(time.time()-start))
        engine.quit()
        return uci_strings.index(str(result.move))


class HumanChessPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        fen = board_to_fen(board)
        chess_board = chess.Board(fen)
        print(str(chess_board))
        valid = self.game.getValidMoves(board, 1)
        for i, vm in enumerate(valid):
            if vm == 1:
                print(uci_strings[i])
        while True:
            a = input()
            a = uci_strings.index(str(a))
            if valid[a]:
                break
            else:
                print('Invalid')
        return a
