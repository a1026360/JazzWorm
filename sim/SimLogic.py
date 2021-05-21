'''
Board class for the game of Sim.
Board data:
  1=white(O), -1=black(X), 0=empty
Squares are stored and manipulated as (x,y) tuples.
'''


class Board:
    def __init__(self, n):
        """Set up initial board configuration."""
        self.n = n
        # Create the empty board array.
        self.pieces = [None] * self.n
        for i in range(self.n):
            self.pieces[i] = [0] * self.n

    # add [][] indexer syntax to the Board
    def __getitem__(self, index):
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        legal_moves = []
        is_empty = True
        for r in range(self.n):
            for c in range(r + 1):
                if self[r][c] == 0:
                    legal_move = (r, c)
                    legal_moves.append(legal_move)
                else:
                    is_empty = False
        if is_empty:
            return [(0, 0)]
        return legal_moves

    def has_legal_moves(self):
        for r in range(self.n):
            for c in range(r + 1):
                if self[r][c] == 0:
                    return True
        return False

    def is_lost(self, color):
        """Check whether the given player has collected a triangle;
        @param color (1=white,-1=black)
        """
        for r in range(self.n):
            for c in range(r + 1):
                if self[r][c] == color:
                    for i in range(r + 1, self.n):
                        if self[i][c] == color:
                            if self[i][r+1] == color:
                                return True
        return False

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """

        (x, y) = move

        if self[x][y] != 0:
            print("shit")

        # Add the piece to the empty square.
        assert self[x][y] == 0
        self[x][y] = color
