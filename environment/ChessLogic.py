import io
import chess
import numpy as np

str_int_mapping = {
    "E": 7,
    "K": 6,
    "Q": 5,
    "R": 4,
    "B": 3,
    "N": 2,
    "P": 1,
    ".": 0,
    "p": -1,
    "n": -2,
    "b": -3,
    "r": -4,
    "q": -5,
    "k": -6,
    "e": -7
}

side_mapping = {
    "2": "7",
    "3": "6",
    "4": "5",
    "5": "4",
    "6": "3",
    "7": "2",
    "8": "1",
}


pawn_chess_ending_mapping = {
    "Q": 5,
    "R": 4,
    "B": 3,
    "N": 2,
    "n": -2,
    "b": -3,
    "r": -4,
    "q": -5,
}

int_str_mapping = {
    "7": "E",
    "6": "K",
    "5": "Q",
    "4": "R",
    "3": "B",
    "2": "N",
    "1": "P",
    "0": ".",
    "-1": "p",
    "-2": "n",
    "-3": "b",
    "-4": "r",
    "-5": "q",
    "-6": "k",
    "-7": "e",
}

en_passat_mapping = {
    "E": ".",
    "e": ".",
}


def board_to_array(chess_board: chess.Board):

    board = str(chess_board)
    for key in str_int_mapping.keys():
        board = board.replace(key, str(str_int_mapping[key]))
    board = board.replace("\n", ",").replace(" ", ",")
    board = np.array(board.split(","), dtype=float).reshape((8, 8))

    if chess_board.is_en_passant(chess.Move.from_uci("a5b6")):
        board[2, 1] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("b5a6")):
        board[2, 0] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("b5c6")):
        board[2, 2] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("c5b6")):
        board[2, 1] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("c5d6")):
        board[2, 3] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("d5c6")):
        board[2, 2] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("d5e6")):
        board[2, 4] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("e5d6")):
        board[2, 3] = str_int_mapping["E"]
    elif chess_board.is_en_passant(chess.Move.from_uci("a4b3")):
        board[5, 1] = str_int_mapping["e"]
    elif chess_board.is_en_passant(chess.Move.from_uci("b4a3")):
        board[5, 0] = str_int_mapping["e"]
    elif chess_board.is_en_passant(chess.Move.from_uci("b4c3")):
        board[5, 2] = str_int_mapping["e"]
    elif chess_board.is_en_passant(chess.Move.from_uci("c4b3")):
        board[5, 1] = str_int_mapping["e"]
    elif chess_board.is_en_passant(chess.Move.from_uci("c4d3")):
        board[5, 3] = str_int_mapping["e"]
    elif chess_board.is_en_passant(chess.Move.from_uci("d4c3")):
        board[5, 2] = str_int_mapping["e"]
    elif chess_board.is_en_passant(chess.Move.from_uci("d4e3")):
        board[5, 4] = str_int_mapping["e"]
    elif chess_board.is_en_passant(chess.Move.from_uci("e4d3")):
        board[5, 3] = str_int_mapping["e"]
    return board


def board_to_fen(board):
    en_passat = "-"
    try:
        if board[2, 0] == str_int_mapping["E"]:
            en_passat = "a6"
        elif board[2, 1] == str_int_mapping["E"]:
            en_passat = "b6"
        elif board[2, 2] == str_int_mapping["E"]:
            en_passat = "c6"
        elif board[2, 3] == str_int_mapping["E"]:
            en_passat = "d6"
        elif board[2, 4] == str_int_mapping["E"]:
            en_passat = "e6"
        elif board[5, 0] == str_int_mapping["e"]:
            en_passat = "a6"
        elif board[5, 1] == str_int_mapping["e"]:
            en_passat = "b6"
        elif board[5, 2] == str_int_mapping["e"]:
            en_passat = "c6"
        elif board[5, 3] == str_int_mapping["e"]:
            en_passat = "d6"
        elif board[5, 4] == str_int_mapping["e"]:
            en_passat = "e6"
    except TypeError as te:
        raise te

    with io.StringIO() as s:
        for row in board:
            empty = 0
            for cell in row:
                if cell != 0 and cell != 7 and cell != -7:
                    if empty > 0:
                        s.write(str(empty))
                        empty = 0
                    s.write(int_str_mapping[str(int(cell))])
                else:
                    empty += 1
            if empty > 0:
                s.write(str(empty))
            s.write('/')
        s.seek(s.tell() - 1)
        s.write(' ')
        s.write('w ')
        s.write('- ')
        s.write(en_passat)
        s.write(' 0 0')
        return s.getvalue()


uci_strings = ['a5b6', 'b5a6', 'b5c6', 'c5b6', 'c5d6', 'd5c6', 'd5e6', 'e5d6', 'a4b3', 'b4a3', 'b4c3', 'c4b3', 'c4d3', 'd4c3', 'd4e3', 'e4d3', 'a2a3', 'a2a4', 'a2b3', 'a3a4', 'a3b4', 'a4a5', 'a4b5', 'a5a6', 'a5b6', 'a6a7', 'a6b7', 'a7a8b', 'a7a8n', 'a7a8q', 'a7a8r', 'b2a3', 'b2b3', 'b2b4', 'b2c3', 'b3a4', 'b3b4', 'b3c4', 'b4a5', 'b4b5', 'b4c5', 'b5a6', 'b5b6', 'b5c6', 'b6a7', 'b6b7', 'b6c7', 'b7b8b', 'b7b8n', 'b7b8q', 'b7b8r', 'c2b3', 'c2c3', 'c2c4', 'c2d3', 'c3b4', 'c3c4', 'c3d4', 'c4b5', 'c4c5', 'c4d5', 'c5b6', 'c5c6', 'c5d6', 'c6b7', 'c6c7', 'c6d7', 'c7c8b', 'c7c8n', 'c7c8q', 'c7c8r', 'd2c3', 'd2d3', 'd2d4', 'd2e3', 'd3c4', 'd3d4', 'd3e4', 'd4c5', 'd4d5', 'd4e5', 'd5c6', 'd5d6', 'd5e6', 'd6c7', 'd6d7', 'd6e7', 'd7d8b', 'd7d8n', 'd7d8q', 'd7d8r', 'e2d3', 'e2e3', 'e2e4', 'e3d4', 'e3e4', 'e4d5', 'e4e5', 'e5d6', 'e5e6', 'e6d7', 'e6e7', 'e7e8b', 'e7e8n', 'e7e8q', 'e7e8r']