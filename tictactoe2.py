class Player():
    def __init__(self, value):
        self.value = value

class Board():
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def  mark_square(self, row, column, player):
        if self.board[int(row)][int(column)] == '-':
            self.board[int(row)][int(column)] = player.value
            return True
        else:
            print("invalid location")
            return False

class Game():
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def validate_input(self, vals):
        if len(vals) == 3:
            for i in range(len(vals)):
                if len(vals[i]) != 1:
                    return False
                else:
                    continue
            return True
        else:
            return False

    def play_game_helper(self, val):
        if self.validate_input(val):
            if val[2] == self.player1.value:
                self.board.mark_square(val[0], val[1], self.player1)
            else:
                self.board.mark_square(val[0], val[1], self.player2)
            # self.printBoard()
            return True
        else:
            return False


    def play_game(self):
        while not self.has_winner():
            val=input("Enter move in form: Row, Column, Symbol\n")
            val = val.split(', ')
            self.play_game_helper(val)
            self.printBoard()
        return 0

    def has_winner(self):
        return (self.board.board[0][0] == self.board.board[0][1] == self.board.board[0][2] != '-') or (self.board.board[1][0] == self.board.board[1][1] == self.board.board[1][2] != '-') or (self.board.board[2][0] == self.board.board[2][1] == self.board.board[2][2] != '-') or (self.board.board[0][0] == self.board.board[1][0] == self.board.board[2][0] != '-') or (self.board.board[0][1] == self.board.board[1][1] == self.board.board[2][1] != '-') or (self.board.board[0][2] == self.board.board[1][2] == self.board.board[2][2] != '-') or (self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] != '-') or (self.board.board[2][0] == self.board.board[1][1] == self.board.board[0][2] != '-')
    
    def printBoard(self):
        print(self.board.board[0])
        print(self.board.board[1])
        print(self.board.board[2])    

if __name__ == '__main__':
    game = Game(Board(), Player('x'), Player('o'))
    game.play_game()