## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.

## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.

# everything should assume to die unless it has a reason to live.



class Life(object):
    # def __init__(starting_point : set):
    def __init__(self, starting_point : set):
        self.alive_cells = starting_point


    def next(self):
        # everything should assume to die unless it has
        #   a reason to live.
        # board = set()
        board = set()

        for (x, y) in self.alive_cells:
            cnt = count_live_neighbors((x, y))
            # print(x, ' ', y, ' cnt = ', cnt)
            if (cnt == 2 or cnt == 3):
                board.add((x, y))

        return (board)



        ## Reproduction: if a dead cell is surrounded
        ##  by exactly three cells, it lives!

        return (board)

    # return set()

        ## Stasis: if a living cell is surrounded by
        #  two or three living cells, it survives.



def count_dead_in_board(board:set):
    if board.__len__() == 0 :
        return 0
    else :
        max_x = 0
        max_y = 0
        for (x,y) in board:
            if x > max_x : max_x = x
            if y > max_y : max_y = y

        living = board.__len__()
        total_board = (max_x+1)*(max_y+1)
        # print('living= ',living, ' ', max_x,' ',max_y)

        return ( total_board - living)

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



