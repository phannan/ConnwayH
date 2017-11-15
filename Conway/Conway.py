## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
##  Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.

# everything should assume to die unless it has a reason to live.
class Life:
    # def __init__(starting_point : set):
    def __init__(self,starting_point : set):
        # type: () -> object
        pass

    def next(starting_point : set):
    # everything should assume to die unless it has a reason to live.
        empty_board = set()
        return (empty_board)

    # return set()

def count_live_neighbors(board : set, cell : tuple):
    start = 0
# a neighbor is in the same line
#    one left  (x-1) or one right (x+1)
#    one above (y-1) or one below (y+1)
# OR diagonal
#    one to the left  and one above (x-1,y-1)
#    one to the right and one above (x+1,y-1)
#    one to the left  and one below (x-1,y+1)
#    one to the right and one below (x+1,y+1)
    x, y = cell

    #inline

    if (x,   y-1) in board : start = start + 1
    if (x,   y+1) in board : start = start + 1
    if (x-1, y)   in board : start = start + 1
    if (x+1, y)   in board : start = start + 1

    # diagonal
    if (x-1, y-1) in board : start = start + 1
    if (x+1, y-1) in board : start = start + 1
    if (x-1, y+1)   in board : start = start + 1
    if (x+1, y+1)   in board : start = start + 1


    return(start)

## Data Structure - Set of living cells.



