import unittest
from Conway.Conway import *
## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.

## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.

# # *.
# # ..
# b_corner      = set([(0, 0)])
#
# # *.*
# # .*.
# b_triangle = set([(0,0),(0,2),(1,1)])
#
# # this one always stays the same
# # **
# # **
# b_stable      = set([(0, 0), (0, 1), (1, 0), (1, 1)])
#
# ##   ***
# ##   **.
# #
# b_3top_2below = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)])
#
# #   ...
# #   ***
# #   ...
# #
# b_blinker = set([(0,1),(1,1),(2,1)])

class conway_test(unittest.TestCase):
#  Helps me make sure tests are running.
    def test_smoke(self):
        Life()
        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()