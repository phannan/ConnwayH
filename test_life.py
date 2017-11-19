import unittest
from Conway.Conway import *
## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.

## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.


class conway_test(unittest.TestCase):
#  Helps me make sure tests are running.
    def test_smoke(self):
        self.assertEqual(True, False)



if __name__ == '__main__':
    unittest.main()