import unittest
from Conway.Conway import *

# *.
# ..
b_corner      = set([(0, 0)])

# this one always stays the same
# **
# **
b_stable      = set([(0, 0), (0, 1), (1, 0), (1, 1)])

##   ***
##   **.
#
b_3top_2below = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)])

class conway_test(unittest.TestCase):
#  Helps me make sure tests are running.
    def test_smoke(self):
        board = set()
        Life(board)
        self.assertEqual(True, True)

    def test_how_many_live_neighbors_simple(self):

        self.assertEqual(count_live_neighbors(set(), (0, 0)), 0)

        board = set([(0, 0)])
        self.assertEqual(count_live_neighbors(board, (0, 1)), 1)

    def test_how_many_live_neighbors_simple(self):
        ##   ***
        ##   **.
        #
        self.assertEqual(count_live_neighbors(b_3top_2below, (0,0)),3)
        self.assertEqual(count_live_neighbors(b_3top_2below, (0,1)),4)

        # self.assertEqual(1,2)


    ## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.

    ##  *
    ##

    def test_stable_stays_same(self):
        self.assertEqual(Life.next(b_stable),b_stable)

    def hid_test_only_one_dies(self):
        self.assertEqual(Life.next(b_corner),set())
    ##
    ##   ***
    ##   **.
    ##
    ##  Goes to
    ##
    ##   ***
    ##   *..
    ##
    def hid_test_board_is_overpopulated(self):

        next_gen = set([(0, 0), (0, 1), (0, 2), (1, 0)])
        game = Life(b_3top_2below)
        self.assertEqual(game, next_gen)





## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.



if __name__ == '__main__':
    unittest.main()