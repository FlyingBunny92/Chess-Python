# grid_layout.py
import random
import tkinter as tk
from enum import Enum



 
class Piece(Enum):
    KING_WHITE = 1
    QUEEN_WHITE = 2
    ROOK_WHITE = 3
    KNIGHT_WHITE = 4
    BISHOP_WHITE = 5
    PAWN_WHITE = 6

    KING_BLACK = 1
    QUEEN_BLACK = 2
    ROOK_BLACK = 3
    KNIGHT_BLACK = 4
    BISHOP_BLACK = 5
    PAWN_BLACK = 6
        

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Grid Layout')
        self.geometry('200x200')

        rows, cols = (8, 8)
        arr = [[0]*cols]*rows
        self.board = arr
        self.frame = tk.Frame()
        self.frame.pack(expand=True)

        self.button = [None] * 64
        for i in range(64):
            r, c = divmod(i, 8)
            self.button[i] = tk.Button(self.frame, text=' ', font='TkFixedFont',
                                       command=lambda n=i: self.button_click(n))
            self.button[i].grid(row=r, column=c)

        self.fill_board()

    def piece_to_string(self, x, y):
        character = ' '
        print("self.board[x][y]:", self.board[x][y])
        if self.board[x][y] ==  Piece.KING_WHITE:
            character = 'K'
        if self.board[x][y] ==  Piece.KING_BLACK:
            character = 'K'
        if self.board[x][y] ==  Piece.QUEEN_WHITE:
            character = 'Q'
        if self.board[x][y] ==  Piece.QUEEN_BLACK:
            character = 'Q'
        if self.board[x][y] ==  Piece.ROOK_WHITE:
            character = 'R'
        if self.board[x][y] ==  Piece.ROOK_BLACK:
            character = 'R'
        if self.board[x][y] ==  Piece.KNIGHT_WHITE:
            character = 'KN'
        if self.board[x][y] ==  Piece.KNIGHT_BLACK:
            character = 'KN'
        if self.board[x][y] ==  Piece.BISHOP_BLACK:
            character = 'B'
        if self.board[x][y] ==  Piece.BISHOP_WHITE:
            character = 'B'
        if self.board[x][y] ==  Piece.PAWN_WHITE:
            character = 'P'
        if self.board[x][y] ==  Piece.PAWN_BLACK:
            character = 'P'

        return character


    def fill_board(self):
        for i in range(8):
            self.board[i][1] = (Piece.PAWN_WHITE)

        for i in range(8):
            self.board[i][6] = (Piece.PAWN_BLACK)

        self.board[0][0] = (Piece.ROOK_WHITE)
        self.board[7][0] = (Piece.ROOK_WHITE)
        self.board[1][0] = (Piece.BISHOP_WHITE)
        self.board[6][0] = (Piece.BISHOP_WHITE)
        self.board[3][0] = (Piece.QUEEN_WHITE)
        self.board[5][0] = (Piece.KING_WHITE)


        self.board[0][7]= (Piece.ROOK_BLACK)
        self.board[7][7] = (Piece.ROOK_BLACK)
        self.board[1][7] = (Piece.BISHOP_BLACK)
        self.board[6][7] = (Piece.BISHOP_BLACK)
        self.board[3][7] = (Piece.QUEEN_BLACK)
        self.board[5][7] = (Piece.KING_BLACK)

        # print(self.board)


    def button_click(self, n):
        choice = random.randrange(2)
        x = (n%8)
        y = int(n/8)
        print("\n\n\n\n ")
        print(" x:", x)
        print(" y:", y)

        # txt = str(self.board[x][y])
        txt  = self.piece_to_string(x, y)
        character, color = (('x', 'red'), ('o', 'green'))[choice]
        self.button[n]['text'] = txt
        self.button[n]['fg'] = color

if __name__ == '__main__':
    root = Root()
    root.mainloop()
