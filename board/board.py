class Board:
    def __init__(self, player, choice, board):
        self.player = player
        self.choice = choice
        self.board = board

    def check_winner(self):
        check_list = []
        win = True
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == "X" :
                    check_list = check_list + orig_board[row][column]


    def draw_board(self):

        for row in range(len(self.board)):
            if row >= 1 and row < 3:
                print("---------")
            self.hold = ""
            for column in range(len(self.board[row])):
                if column >= 1 and column < 3:
                    self.hold += " | " + str(self.board[row][column])
                else:
                    self.hold += str(self.board[row][column])
            print(self.hold)

    def find_loc(self, selection, player):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == selection:
                    self.board[row][column] = player



game_board = [[1,2,3],[4,5,6],[7,8,9]]
orig_board = [[1,2,3],[4,5,6],[7,8,9]]
p = Board(1,2,game_board)
p.draw_board()
win = False
while not win:
    player = input("Player X make selection(1-9)")
    loc = p.find_loc(player, "X")
    p.draw_board()
    player = input("Player O make selection(1-9)")
    loc = p.find_loc(player, "O")
    p.draw_board()
    p.check_winner()
    win = True
