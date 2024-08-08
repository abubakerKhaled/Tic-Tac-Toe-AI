from player import Player
import math
import random

class MiniMaxComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if game.num_empty_squares() == 9:
            return random.choice(game.available_moves())
        else:
            return self.minimax(game, self.letter)["position"]

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "X" if player == "O" else "O"

        if state.winner == other_player:
            # If the other player (opponent) has one, we return a score
            # the score is positive if the other player is the AI player, as we want to maximize
            # the score is negative if the other player is not the AI player, as we want to minimize
            return {
                "position": None,
                "score": (
                    1 * (state.num_empty_squares() + 1)
                    if other_player == max_player
                    else -1 * (state.num_empty_squares() + 1)
                ),
            }

        elif not state.empty_squares():
            # the score is 0 if no one won
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # maximize the max_player(AI)
        else:
            best = {"position": None, "score": math.inf}  # minimize the other_player

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recursivly simulate a game after making that move
            sim_score = self.minimax(
                state, other_player
            )  # simulate the other player turn

            # step 3: undo the move
            state.board[possible_move] = " "
            state.winner = None

            # step 4: update the best move if necessary
            sim_score["position"] = (
                possible_move  # this step is necessary otherwise the minimax recursion won't know the move
            )

            if player == max_player:  # maximize the max player
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:  # minimize the other player
                if sim_score["score"] < best["score"]:
                    best = sim_score

        return best
