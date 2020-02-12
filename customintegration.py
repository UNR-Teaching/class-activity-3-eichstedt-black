import unittest
import tictactoe2 as ti

class IntegrationTest(unittest.TestCase):
    def test_x_wins(self):
        # Create board
        board = ti.Board()

        # Create players
        playerX = ti.Player('x')
        playerO = ti.Player('o')

        game = ti.Game(board, playerX, playerO)

        # Play game and x wins
        game.board.mark_square(0,0,game.player1)
        game.board.mark_square(1,0,game.player2)
        game.board.mark_square(0,1,game.player1)
        game.board.mark_square(1,1,game.player2)
        game.board.mark_square(0,2,game.player1)

        # Assert true   
        self.assertTrue(game.has_winner())

    def test_o_wins(self):
        # Create board
        board = ti.Board()

        # Create players
        playerX = ti.Player('x')
        playerO = ti.Player('o')

        # Play game and o wins
        game = ti.Game(board, playerX, playerO)
        game.board.mark_square(0,0,game.player2)
        game.board.mark_square(1,0,game.player1)
        game.board.mark_square(0,1,game.player2)
        game.board.mark_square(1,1,game.player1)
        game.board.mark_square(0,2,game.player2)
        
        # Assert true
        self.assertTrue(game.has_winner())

    def test_no_wins(self):
        # Create board
        board = ti.Board()

        # Create players
        playerX = ti.Player('x')
        playerO = ti.Player('o')

        game = ti.Game(board, playerX, playerO)

        # Play game and no one wins
        game.board.mark_square(0,0,game.player1)
        game.board.mark_square(0,1,game.player2)
        game.board.mark_square(0,2,game.player1)
        game.board.mark_square(1,0,game.player1)
        game.board.mark_square(1,1,game.player2)
        game.board.mark_square(1,2,game.player2)
        game.board.mark_square(2,0,game.player2)
        game.board.mark_square(2,1,game.player1)
        game.board.mark_square(2,2,game.player1)

        # Assert true   
        self.assertFalse(game.has_winner())



if __name__ == '__main__':
    unittest.main()      