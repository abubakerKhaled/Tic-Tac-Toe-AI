from human_player import HumanPlayer
from random_computer_player import RandomComputerPlayer
from minimax_computer_player import MiniMaxComputerPlayer
from tic_tac_toe import TicTacToe
import time


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter)! or None for a tie.
    if print_game:
        game.print_board_nums()

    letter = "X"  # startting letter
    # iterate while the same has empty squares
    # ( we don't have to worry about winner because we'll just return that
    #   which breaks the loop )
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")  # just empty line

            if game.winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            # after we made our move, we need to alternate letters
            letter = "O" if letter == "X" else "X"  # swiches

        # tiny break
        if print_game:
            time.sleep(0.8)

    if print_game:
        print("it's a tie!")


# if __name__ == "__main__":
#     x_wins = 0
#     o_wins = 0
#     ties = 0
#     x_player = RandomComputerPlayer('X')
#     o_player = MiniMaxComputerPlayer("O")
    
#     for _ in range(1000):
#         game = TicTacToe()
#         result = play(game, x_player, o_player, print_game=False)

#         if result == "X":
#             x_wins += 1
#         elif result == "O":
#             o_wins += 1
#         else:
#             ties += 1

#     print(
#         f"After 1000 iterations, we see {x_wins} Random wins, {o_wins} MiniMax wins, and {ties} ties."
#     )


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = MiniMaxComputerPlayer("O")
    game = TicTacToe()

    play(game, x_player, o_player)