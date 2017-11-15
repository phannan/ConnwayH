import unittest
from Conway.Conway import *




## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
##
##   ***
##   **.
##
##  Goes to
##
##   ***
##   *..
##
## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.



if __name__ == '__main__':
    unittest.main()