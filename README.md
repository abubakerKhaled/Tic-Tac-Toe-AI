# Tic-Tac-Toe Game with AI (Minimax Algorithm)

This project implements a Tic-Tac-Toe game where a human player can compete against an AI player that uses the Minimax algorithm. The AI is designed to play optimally, ensuring the best possible move in every situation.

## Features

- **Human vs. AI**: Compete against an AI that uses the Minimax algorithm for optimal play.
- **Minimax Algorithm**: The AI uses the Minimax algorithm to evaluate the best possible moves.
- **Command-line Interface**: Simple and easy-to-use text-based interface.
- **Multiple Player Types**: Includes random computer player and human player for variety.

## Project Structure

- **`tic_tac_toe.py`**: Contains the main game logic, including the game board management and win detection.
- **`player.py`**: Defines the base `Player` class, which is inherited by specific player types.
- **`random_computer_player.py`**: Contains the implementation of a random computer player.
- **`human_player.py`**: Manages the human player's interaction with the game.
- **`minimax_computer_player.py`**: Implements the AI player using the Minimax algorithm.
- **`game.py`**: Main script that brings everything together and runs the game.

## How to Play

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/tictactoe-minimax.git
   ```
2. **Navigate to the Project Directory**:
   ```sh
   cd tictactoe-minimax
   ```
3. **Run the Game**:
   ```sh
   python game.py
   ```
4. **Follow the On-screen Instructions**: Input your move by selecting a position from 0 to 8 when prompted.

## Game Modes

- **Human vs. AI (Minimax)**: The default mode where the human player (X) competes against the AI player (O) using the Minimax algorithm.
- **Human vs. Random Computer**: Modify the `game.py` script to use `RandomComputerPlayer` instead of `MiniMaxComputerPlayer` for a less challenging game.

## Classes Overview

### `TicTacToe`

- **`__init__(self)`**: Initializes the game board and tracks the winner.
- **`print_board(self)`**: Displays the current state of the game board.
- **`print_board_nums()`**: Shows the board numbers corresponding to positions (0-8).
- **`available_moves(self)`**: Returns a list of available moves.
- **`empty_squares(self)`**: Checks if there are any empty squares on the board.
- **`num_empty_squares(self)`**: Counts the number of empty squares.
- **`make_move(self, square, letter)`**: Places a letter on the board and checks if the move results in a win.
- **`check_winner(self, square, letter)`**: Checks if the current move leads to a win.

### `Player` (Base Class)

- **`__init__(self, letter)`**: Initializes the player with a letter (`X` or `O`).
- **`get_move(self, game)`**: Abstract method that must be implemented by subclasses to get the next move.

### `RandomComputerPlayer`

- **`get_move(self, game)`**: Selects a random available move.

### `HumanPlayer`

- **`get_move(self, game)`**: Prompts the human player to input their move.

### `MiniMaxComputerPlayer`

- **`get_move(self, game)`**: Determines the best move using the Minimax algorithm.
- **`minimax(self, state, player)`**: Recursively evaluates the best possible move to maximize the AI player's chances of winning.

## Minimax Algorithm

The Minimax algorithm is used by the AI player to evaluate the optimal move by simulating all possible game states. It ensures that the AI either wins or forces a tie, depending on the game state.

- **Maximizing Player**: The AI tries to maximize its score.
- **Minimizing Player**: The opponent (human) tries to minimize the AI's score.
- **Base Cases**: The algorithm returns a score based on whether the game is won, lost, or tied.

## Future Improvements

- **Enhanced AI**: Add different difficulty levels by limiting the depth of the Minimax algorithm.
- **GUI Interface**: Develop a graphical user interface for a more user-friendly experience.
- **Two-player Mode**: Implement a mode where two human players can compete against each other.

## License

This project is open-source and available under the MIT License. Feel free to contribute, modify, and share!

---

Enjoy playing Tic-Tac-Toe with an AI that never loses!