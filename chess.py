import functools
import operator
import math


class Board:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Piece:
    def __init__(self):
        self.x = None
        self.y = None

    # place a piece on a tile
    def place(self, x, y):
        self.x = x
        self.y = y

    # returns true if self and piece have the same
    # x, y coordinates
    def at(self, piece):
        return self.y == piece.y and self.x == piece.x

    # returns true if can reach piece.x, piece.y next turn
    # returns false otherwise
    def covers(self, piece):
        pass


class Knight(Piece):
    def covers(self, piece):
        if abs(piece.x - self.x) == 2 and abs(piece.y - self.y) == 1 or \
                abs(piece.x - self.x) == 1 and abs(piece.y - self.y) == 2:
            return True
        else:
            return self.at(piece)


class Bishop(Piece):
    def covers(self, piece):
        if abs(piece.x - self.x) == abs(piece.y - self.y):
            return True
        else:
            return self.at(piece)


class King(Piece):
    def covers(self, piece):
        if abs(piece.x - self.x) <= 1 and abs(piece.y - self.y) <= 1:
            return True
        else:
            return self.at(piece)


class Rook(Piece):
    def covers(self, piece):
        if abs(piece.x - self.x) == 0 or abs(piece.y - self.y) == 0:
            return True
        else:
            return self.at(piece)


class Queen(Piece):
    def covers(self, piece):
        if abs(piece.x - self.x) == abs(piece.y - self.y):
            return True
        elif piece.x == self.x or piece.y == self.y:
            return True
        else:
            return self.at(piece)


def count_no_coverage_states(width, length, n_kings, n_queens, n_bishops, n_rooks, n_knights):
    pieces = [King() for _ in range(n_kings)] + [Queen() for _ in range(n_queens)] + \
             [Bishop() for _ in range(n_bishops)] + [Rook() for _ in range(n_rooks)] + \
             [Knight() for _ in range(n_knights)]
    repeat_reps = [math.factorial(n) for n in [n_kings, n_queens, n_bishops, n_rooks, n_knights]]

    raw_result = no_coverage_impl(Board(width, length), pieces, [])

    return functools.reduce(operator.truediv, repeat_reps, raw_result)


def no_coverage_impl(board, unfixed, fixed):
    if not unfixed:
        return 1
    result = 0
    uf = unfixed[0]
    for x in range(board.width):
        for y in range(board.length):
            uf.place(x, y)
            if not fixed:
                result += no_coverage_impl(board, unfixed[1:], fixed + [uf])
            else:
                if not functools.reduce(lambda agg, pp: agg or (pp.covers(uf) or uf.covers(pp)), fixed, False):
                    result += no_coverage_impl(board, unfixed[1:], fixed + [uf])
    return result

