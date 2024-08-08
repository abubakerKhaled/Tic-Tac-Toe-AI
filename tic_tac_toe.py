class TicTacToe:
    def __init__(self):
        self.board = [
            " " for _ in range(9)
        ]  # We will use single list to represent 3x3 board
        self.winner = None  # keeps track of winner!

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def check_row(self, square, letter):
        # first lets check the row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True

    def check_column(self, square, letter):
        column_ind = square % 3
        column = [self.board[column_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

    def check_diagonal_one(self, letter):
        diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
        if all(spot == letter for spot in diagonal1):
            return True

    def check_diagonal_two(self, letter):
        diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
        if all(spot == letter for spot in diagonal2):
            return True

    def check_diagonal(self, letter):
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves to win a diagonal
        if self.check_diagonal_one(letter):
            return True

        elif self.check_diagonal_two(letter):
            return True

        return False

    def check_winner(self, square, letter):
        # winner if 3 in a row anywhere..
        # we have to check all of these!
        if self.check_row(square, letter):
            return True
        # check the column
        elif self.check_column(square, letter):
            return True
        # check diagonal
        # the square must be even square
        if square % 2 == 0:
            if self.check_diagonal(letter):
                return True
        # if all of these fail
        return False

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.winner = letter
            return True
        else:
            return False



