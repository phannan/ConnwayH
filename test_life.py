import unittest
from Conway.Conway import *

# *.
# ..
b_corner      = set([(0, 0)])

# *.*
# .*.
b_triangle = set([(0,0),(0,2),(1,1)])

# this one always stays the same
# **
# **
b_stable      = set([(0, 0), (0, 1), (1, 0), (1, 1)])

##   ***
##   **.
#
b_3top_2below = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)])

#   ...
#   ***
#   ...
#
b_blinker = set([(0,1),(1,1),(2,1)])

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

    def test_how_many_live_neighbors_stable(self):
           for (x,y) in b_stable :
              self.assertEqual(
                  count_live_neighbors(b_stable, (x,y)), 3)

    def test_how_many_live_neighbors_b3top(self):
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
        # self.assertEqual(Life.next(b_stable),b_stable)
        self.assertEqual(b_stable,Life.next(b_stable))

    def test_only_one_dies(self):
        self.assertEqual(Life.next(b_corner),set())
    ##
    ##   ***
    ##   **.
    ##
    ##  Goes to
    ##
    ##   *.*
    ##   *..
    ##
    def test_board_is_overpopulated(self):

        next_gen = set([(0, 0), (0, 2), (1, 0)])
        game = Life.next(b_3top_2below)
        self.assertEqual(game, next_gen)

    def test_count_dead_cells(self):

        self.assertEqual(
            count_dead_in_board(b_corner),  0)
        self.assertEqual(
            count_dead_in_board(b_triangle),3)
        self.assertEqual(
            count_dead_in_board(b_stable),0)
        self.assertEqual(
            count_dead_in_board(b_3top_2below), 1)
        self.assertEqual(
            count_dead_in_board(b_blinker), 3)


    # *.*
    # *..
    #  goes to
    # .*.
    # ...
    def hid_test_birth(self):
        next_gen = set([(0,1)])

        game = Life.next(b_triangle)
        self.assertEqual(game,next_gen)
#   ...
#   ***
#   ...
#  goes to
#   .*.
#   .*.
#   .*.
    def hid_test_blinker(self):
        next_gen = set([(1,0),(1,1),(1,2)])
        game = Life.next(b_blinker)
        self.assertEqual(game,next_gen)





## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.



if __name__ == '__main__':
    unittest.main()