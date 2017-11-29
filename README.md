# Table of Contents
* About Game-Playing Agent
* Implementation Detail
* Heuristic Analysis
* Summary on AlphaGo paper by DeepMind Team
* Resources
* Other (Game Visualization)

# About Game-Playing Agent

![Example game of isolation](viz.gif)

This project is about developing an adversarial search agent to play the game "Isolation".  Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board. 

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.

# Implementation Detail

The skeleton of this project is provided by Udacity's AI-Nanodegree course instructors. My job through the project was to build some of the core logical functional blocks in game_agent.py. Those are..

* `MinimaxPlayer.minimax()`: minimax search(ref. [AIMA Minimax Decision](https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md))
* `AlphaBetaPlayer.alphabeta()`: minimax search with alpha-beta pruning (ref. [AIMA Alpha-Beta Search](https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md))
* `AlphaBetaPlayer.get_move()`: iterative deepening search [AIMA Iterative Deepening Search](https://github.com/aimacode/aima-pseudocode/blob/master/md/Iterative-Deepening-Search.md)
* `custom_score()`: your own best position evaluation heuristic

After completing the implementation, the functionalities can be tested by running tournament.py. This is a simple script for self playing game between different algorithms and evaluation functions. The custom_score() evaluation function has been tested against other ones listed below.

- Random: An agent that randomly chooses a move each turn.
- MM_Open: MinimaxPlayer agent using the open_move_score heuristic with search depth 3
- MM_Center: MinimaxPlayer agent using the center_score heuristic with search depth 3
- MM_Improved: MinimaxPlayer agent using the improved_score heuristic with search depth 3
- AB_Open: AlphaBetaPlayer using iterative deepening alpha-beta search and the open_move_score heuristic
- AB_Center: AlphaBetaPlayer using iterative deepening alpha-beta search and the center_score heuristic
- AB_Improved: AlphaBetaPlayer using iterative deepening alpha-beta search and the improved_score heuristic

# Heuristic Analysis

After a heuristic analysis on evaluation function, the custom_score() method has been implemented. The detail how the evaluation function is chosen is described in the separate document file, "heuristic_analysis.pdf". Please refer to it.

# Summary on AlphaGo paper by DeepMind Team

This part of the project is not strongly related to the actual game agent program. However, it is done for strengthen the ability to research and think thoroughly about AI field. The summary is provided in the separate file, "research_review.pdf". The contents includes briefly about

* A brief summary of the paper's goals or techniques introduced.
* A brief summary of the paper's results.

# Resources

* /isolation : class for game board (including the state)
* /isoviz : class for visualization of the game
* game_agent.py : minimax, alphabeta pruning, and couple of custom evaluation functions
* sample_players.py : sample player's code originally provided (kind of sample code to get started)
* tournament.py : script for running games between different algorithms

# Game Visualization

The `isoviz` folder contains a modified version of chessboard.js that can animate games played on a 7x7 board.  In order to use the board, you must run a local webserver by running `python -m http.server 8000` from your project directory (you can replace 8000 with another port number if that one is unavailable), then open your browser to `http://localhost:8000` and navigate to the `/isoviz/display.html` page.  Enter the move history of an isolation match (i.e., the array returned by the Board.play() method) into the text area and run the match.  Refresh the page to run a different game.  (Feel free to submit pull requests with improvements to isoviz.)
