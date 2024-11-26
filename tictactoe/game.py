class TickTacToe:
    def __init__(self):
        self.board=['a' for x in range(9)]
    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print("| "," |".join(row)," ")
    print_board()              