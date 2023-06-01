
import random
import tkinter as tk
from enum import Enum


class Type(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3
    KNIGHT = 4
    BISHOP = 5
    PAWN = 6
    NONE = 7

class Color(Enum):
    WHITE = 1
    BLACK = 2
    NONE = 3


 
class Piece():
    def __init__(self, type, color, x, y):
        self.type = type
        self.color = color
        self.activated = False
        self.x = x
        self.y = y
        
        

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Grid Layout')
        self.geometry('200x200')

        self.player_turn = 1
        self.active_node = None
        self.active_x = -1
        self.active_y = -1

        self.board = self.create_board()
        self.frame = tk.Frame()
        self.frame.pack(expand=True)

        self.button = [None] * 64
        for i in range(64):
            r, c = divmod(i, 8)
            x = (i%8)
            y = int(i/8)
            txt  = self.piece_to_string(x, y)
            color = 'blue'
            if self.board[y][x].color == Color.BLACK:
                color = 'green'
            if self.board[y][x].color == Color.WHITE:
                color = 'blue'

            self.button[i] = tk.Button(self.frame, text=txt, font='TkFixedFont',
                                       command=lambda n=i: self.button_click(n))
            self.button[i].grid(row=r, column=c)
            self.button[i]['fg'] = color




    def create_board(self):
        self.board = []
        
        row1 = []
        row1.append(Piece(Type.ROOK, Color.WHITE, 0, 0))
        row1.append(Piece(Type.KNIGHT, Color.WHITE, 1, 0))
        row1.append(Piece(Type.BISHOP, Color.WHITE, 2, 0))
        row1.append(Piece(Type.QUEEN, Color.WHITE, 3, 0))
        row1.append(Piece(Type.KING, Color.WHITE, 4, 0))
        row1.append(Piece(Type.BISHOP, Color.WHITE, 5, 0))
        row1.append(Piece(Type.KNIGHT, Color.WHITE, 6, 0))
        row1.append(Piece(Type.ROOK, Color.WHITE, 7, 0))
        self.board.append(row1)

        row2 = []
        for i in range(8):
            row2.append(Piece(Type.PAWN, Color.WHITE, i, 1))
        self.board.append(row2)

        row3 = []
        for i in range(8):
            row3.append(Piece(Type.NONE, Color.NONE, i, 2))
        self.board.append(row3)

        row4 = []
        for i in range(8):
            row4.append(Piece(Type.NONE, Color.NONE, i, 3))
        self.board.append(row4)

        row5 = []
        for i in range(8):
            row5.append(Piece(Type.NONE, Color.NONE, i, 4))
        self.board.append(row5)

        row6 = []
        for i in range(8):
            row6.append(Piece(Type.NONE, Color.NONE, i, 5))
        self.board.append(row6)

        row7 = []
        for i in range(8):
            row7.append(Piece(Type.PAWN, Color.BLACK, i, 6))
        self.board.append(row7)

        row8 = []
        row8.append(Piece(Type.ROOK, Color.BLACK, 0, 7))
        row8.append(Piece(Type.KNIGHT, Color.BLACK, 1, 7))
        row8.append(Piece(Type.BISHOP, Color.BLACK, 2, 7))
        row8.append(Piece(Type.QUEEN, Color.BLACK, 3, 7))
        row8.append(Piece(Type.KING, Color.BLACK, 4, 7))
        row8.append(Piece(Type.BISHOP, Color.BLACK, 5, 7))
        row8.append(Piece(Type.KNIGHT, Color.BLACK, 6, 7))
        row8.append(Piece(Type.ROOK, Color.BLACK, 7, 7))
        self.board.append(row8)
        for row in self.board:
            r = ""
            for p in row:
                r += (self.print_piece(p)) + " "


        return self.board


    def print_piece(self, p):
        character = ' '
        if p.type==Type.KING and p.color==Color.WHITE:
            return 'K'
        if p.type==Type.KING and p.color==Color.BLACK:
            return 'K'
        if p.type==Type.QUEEN and p.color==Color.WHITE:
            return 'Q'
        if p.type==Type.QUEEN and p.color==Color.BLACK:
            return 'Q'
        if p.type==Type.ROOK and p.color==Color.WHITE:
            return 'R'
        if p.type==Type.ROOK and p.color==Color.BLACK:
            return 'R'
        if p.type==Type.KNIGHT and p.color==Color.WHITE:
            return 'KN'
        if p.type==Type.KNIGHT and p.color==Color.BLACK:
            return 'KN'
        if p.type==Type.BISHOP and p.color==Color.BLACK:
            return 'B'
        if p.type==Type.BISHOP and p.color==Color.WHITE:
            return 'B'
        if p.type==Type.PAWN and p.color==Color.BLACK:
            return 'P'
        if p.type==Type.PAWN and p.color==Color.WHITE:
            return 'P'

        return character


    def piece_to_string(self, x, y):

        if self.board[y][x].type==Type.KING and self.board[y][x].color==Color.WHITE:
            return 'K'
        if self.board[y][x].type==Type.KING and self.board[y][x].color==Color.BLACK:
            return 'K'
        if self.board[y][x].type==Type.QUEEN and self.board[y][x].color==Color.WHITE:
            return 'Q'
        if self.board[y][x].type==Type.QUEEN and self.board[y][x].color==Color.BLACK:
            return 'Q'
        if self.board[y][x].type==Type.ROOK and self.board[y][x].color==Color.WHITE:
            return 'R'
        if self.board[y][x].type==Type.ROOK and self.board[y][x].color==Color.BLACK:
            return 'R'
        if self.board[y][x].type==Type.KNIGHT and self.board[y][x].color==Color.WHITE:
            return 'KN'
        if self.board[y][x].type==Type.KNIGHT and self.board[y][x].color==Color.BLACK:
            return 'KN'
        if self.board[y][x].type==Type.BISHOP and self.board[y][x].color==Color.WHITE:
            return 'B'
        if self.board[y][x].type==Type.BISHOP and self.board[y][x].color==Color.BLACK:
            return 'B'
        if self.board[y][x].type==Type.PAWN and self.board[y][x].color==Color.WHITE:
            return 'P'
        if self.board[y][x].type==Type.PAWN and self.board[y][x].color==Color.BLACK:
            return 'P'

        return ' '


    def fill_board(self):
        
        rows, cols = (8, 8)
        self.board = [[Piece(Type.NONE, Color.NONE, -1, -1)]*cols]*rows
        for i in range(8):
            self.board[i][1] = Piece(Type.PAWN, Color.WHITE, i, 1)

        for i in range(8):
            self.board[i][6] = Piece(Type.PAWN, Color.BLACK, i, 6)


        self.board[0][0] = Piece(Type.ROOK, Color.WHITE, 0, 0)
        self.board[7][0] = Piece(Type.ROOK, Color.WHITE, 7, 0)
        self.board[1][0] = Piece(Type.BISHOP, Color.WHITE, 1, 0)
        self.board[6][0] = Piece(Type.BISHOP, Color.WHITE, 6, 0)
        self.board[3][0] = Piece(Type.QUEEN, Color.WHITE, 3, 0)
        self.board[5][0] = Piece(Type.KING, Color.WHITE, 5, 0)


        self.board[0][7] = Piece(Type.ROOK, Color.BLACK, 0, 7)
        self.board[7][7] = Piece(Type.ROOK, Color.BLACK, 7, 7)
        self.board[1][7] = Piece(Type.BISHOP, Color.BLACK, 1, 7)
        self.board[6][7] = Piece(Type.BISHOP, Color.BLACK, 6, 7)
        self.board[3][7] = Piece(Type.QUEEN, Color.BLACK, 3, 7)
        self.board[5][7] = Piece(Type.KING, Color.BLACK, 5, 7)

        return self.board


    def update_buttons(self, coords1, coords2):
        x1 = coords1[0]
        y1 = coords1[1]
        i1 = (y1*8)+x1
        x2 = coords2[0]
        y2 = coords2[1]
        i2 = (y2*8)+x2
        txt  = self.piece_to_string(x2, y2)
        color = 'blue'
        if self.board[y2][x2].color == Color.BLACK:
            color = 'green'
        if self.board[y2][x2].color == Color.WHITE:
            color = 'blue'

        self.button[i2]['text'] = txt
        self.button[i2]['fg'] = color

        txt2  = self.piece_to_string(x1, y1)
        color2 = 'blue'
        if self.board[y1][x1].color == Color.BLACK:
            color2 = 'green'
        if self.board[y1][x1].color == Color.WHITE:
            color2 = 'blue'

        self.button[i1]['text'] = txt2
        self.button[i1]['fg'] = color2



    def check_piece_moves(self, coords1, coords2):
        x1 = coords1[0]
        y1 = coords1[1]
        x2 = coords2[0]
        y2 = coords2[1]

        if self.active_node == None:
            return False 

        if self.active_node.type==Type.PAWN and self.active_node.color==Color.WHITE:
            if (y1-y2) == 1:
                return True
            if abs(x1-x2) == 1 or (y1-y2) == 1 and self.board[y1][x1].type != Type.NONE:
                return True
            return False 
                
        if self.active_node.type==Type.PAWN and self.active_node.color==Color.BLACK:
            print("abs(x1-x2):", abs(x1-x2))
            print("y1-y2:", y1-y2)
            if (y1-y2) == -1:
                return True
            if abs(x1-x2) == 1 or (y1-y2) == -1 and self.board[y1][x1].type != Type.NONE:
                return True
            return False
            
        if self.active_node.type==Type.BISHOP:
            if abs(x1-x2) == abs(y1-y2):
                return True
            return False
            
        if self.active_node.type==Type.KNIGHT:
            if (abs(x1-x2) == 2) and (abs(y1-y2) == 1):
                return True
            if (abs(x1-x2) == 1) and (abs(y1-y2) == 2):
                return True
            return False
        
        if self.active_node.type==Type.ROOK:
            if (abs(x1-x2) > 1) and (abs(y1-y2) == 0):
                return True
            if (abs(x1-x2) == 0) and (abs(y1-y2) > 0):
                return True
            return False
        
        if self.active_node.type==Type.QUEEN:
            if abs(x1-x2) == abs(y1-y2):
                return True
            if (abs(x1-x2) == 1) and (abs(y1-y2) == 1):
                return True
            if (abs(x1-x2) == 1) and (abs(y1-y2) == 0):
                return True
            if (abs(x1-x2) == 0) and (abs(y1-y2) == 1):
                return True
            return False
        
        if self.active_node.type==Type.KING:
            if (abs(x1-x2) == 1) and (abs(y1-y2) == 1):
                return True
            if (abs(x1-x2) == 1) and (abs(y1-y2) == 0):
                return True
            if (abs(x1-x2) == 0) and (abs(y1-y2) == 1):
                return True
            return False



        return False





    def button_click(self, n):
        x = (n%8)
        y = int(n/8)
        print("n:", n)
        print("self.board[y][x].color:", self.board[y][x].color)
        print("self.board[y][x].type:", self.board[y][x].type)
        print("self.board[y][x]:", self.board[y][x])
        txt  = self.piece_to_string(x, y)

        # It is not white players turn
        if self.board[y][x].color == Color.WHITE and self.player_turn == -1:
            print("It is not white players turn")
            return False
        
        # It is not black players turn
        if self.board[y][x].color == Color.BLACK and self.player_turn == 1:
            print("It is not black players turn")
            return False

        if self.active_node == None:
            print("if self.active_node == None:")
            color = 'red'
            self.button[n]['text'] = txt
            self.button[n]['fg'] = color
            self.active_node = self.board[y][x]
            self.active_node.x = x
            self.active_node.y = y
            self.active_x = x
            self.active_y = y

        result = self.check_piece_moves([x, y], [self.active_x, self.active_y])
        if result == False:
            return False

        if self.active_node != None:
            print("if self.active_node != None:")
            self.board[y][x] = Piece(self.board[self.active_y][self.active_x].type, self.board[self.active_y][self.active_x].color, x, y)
            self.board[self.active_y][self.active_x] = Piece(Type.NONE, Color.NONE, self.active_x, self.active_y)
            self.update_buttons([x, y], [self.active_x, self.active_y])
            self.active_node = None
            self.player_turn *= -1

       


        return True
        


if __name__ == '__main__':
    root = Root()
    root.mainloop()
