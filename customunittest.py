import unittest
import tictactoe2 as ti

# Unit tests
class TestPlayer(unittest.TestCase):
    def test_initialization(self):
        player = ti.Player('x')
        self.assertEqual(player.value, 'x')
        player = ti.Player('o')
        self.assertEqual(player.value, 'o')

class TestBoard(unittest.TestCase):
    def test_initialization(self):
        board = ti.Board()
        self.assertEqual(board.board[0], ['-', '-', '-'])
        self.assertEqual(board.board[1], ['-', '-', '-'])
        self.assertEqual(board.board[2], ['-', '-', '-'])

    def test_mark(self):
        board = ti.Board()
        player = ti.Player('x')
        self.assertTrue('x', board.mark_square(0,0,player))

class TestGame(unittest.TestCase):
    def test_initialization(self):
        game = ti.Game(ti.Board(), ti.Player('x'), ti.Player('o'))
        self.assertIsNotNone(game)

    def test_validate(self):
        game = ti.Game(ti.Board(), ti.Player('x'), ti.Player('o'))
        self.assertFalse(game.validate_input([]))

    # Dependent on board, go in integration
    def test_has_winner(self):
        game = ti.Game(ti.Board(), ti.Player('x'), ti.Player('o'))
        self.assertFalse(game.has_winner())

    def test_play_game_helper(self):
        game = ti.Game(ti.Board(), ti.Player('x'), ti.Player('o'))
        self.assertFalse(game.play_game_helper([10]))
        self.assertTrue(game.play_game_helper(['1','1','x']))

if __name__ == '__main__':
    unittest.main()      