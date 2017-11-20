"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
from game_agent import MinimaxPlayer
from game_agent import SearchTimeout
from game_agent import AlphaBetaPlayer

# from importlib import reload

class IsolationTest(unittest.TestCase):
    def setUp(self):
        # reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        self.player = MinimaxPlayer(self.game, SearchTimeout)
        self.player.minimax(self.game, 3)
        self.asserEqual(1, 1)

    def a(self):
        pass

if __name__ == '__main__':
    # unittest.main()
    # player1 = "Player1"
    # player2 = "Player2"

    player1 = AlphaBetaPlayer()
    player2 = AlphaBetaPlayer()
    game = isolation.Board(player1, player2, width=5, height=5)
    print(game.play())

    # moves = player1.minimax(game, 3)
    # game.apply_move(moves)
    # print(moves)
    #
    # moves = player2.minimax(game, 3)
    # game.apply_move(moves)
    # print(moves)
