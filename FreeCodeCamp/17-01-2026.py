"""
17-01-2026
FreeCodeCamp
Given the position of a knight on a chessboard, return the number of valid squares the knight can move to.

A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:

A8	B8	C8	D8	E8	F8	G8	H8
A7	B7	C7	D7	E7	F7	G7	H7
A6	B6	C6	D6	E6	F6	G6	H6
A5	B5	C5	D5	E5	F5	G5	H5
A4	B4	C4	D4	E4	F4	G4	H4
A3	B3	C3	D3	E3	F3	G3	H3
A2	B2	C2	D2	E2	F2	G2	H2
A1	B1	C1	D1	E1	F1	G1	H1
A knight moves in an "L" shape: two squares in one direction (horizontal or vertical), and one square in the perpendicular direction.

This means a knight can move to up to eight possible positions, but fewer when near the edges of the board. For example, if a knight was at A1, it could only move to B3 or C2.

Tests
1. knight_moves("A1") should return 2.
2. knight_moves("D4") should return 8.
3. knight_moves("G6") should return 6.
4. knight_moves("B8") should return 3.
5. knight_moves("H3") should return 4.
"""

# Global variable to store the chessboard
board = {}


def setup_board():
    for row in range(8):
        for col in range(8):
            board[(row + 1, col + 1)] = None
    return board


def fill_board_values(board):
    for col in range(8):
        for row in range(8):
            letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
            board[(col + 1, row + 1)] = f"{letters[col]}{row + 1}"
    return board


def knight_moves(position):
    """
    Given a value on the board find all possible moves for a knight.
    Knights moves in L shape 2 spaces + 1 space right or left
    On board row + means up, row - means down, col + means right, col - means left
    There are no rows below 1 or above 8, no columns left of A or right of H
    """

    # Need to get coords when given a value
    coords = [pos for pos, val in board.items() if val == position]

    # Possible moves for knight
    possible_moves = []
    row, col = coords[0]
    possible_moves.append((row + 2, col + 1))
    possible_moves.append((row + 2, col - 1))
    possible_moves.append((row - 2, col + 1))
    possible_moves.append((row - 2, col - 1))
    possible_moves.append((row + 1, col + 2))
    possible_moves.append((row + 1, col - 2))
    possible_moves.append((row - 1, col + 2))
    possible_moves.append((row - 1, col - 2))

    # Filter out invalid moves
    possible_moves = [
        move for move in possible_moves if 1 <= move[0] <= 8 and 1 <= move[1] <= 8
    ]
    return len(possible_moves)


def main():
    board = setup_board()
    board = fill_board_values(board)
    print(knight_moves("B8"))


if __name__ == "__main__":
    main()
