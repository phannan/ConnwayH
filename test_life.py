import unittest


## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.

## Stasis: if a living cell is surrounded by two or three living cells, it survives.
## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.


class Board():
    def __init__(self):
        self.live_cells = set()

    def num_live(self):
        return len(self.live_cells)

    def add_one_location(self, location):
        self.live_cells.add(location)

    def num_live_neighbors(self, location):
        my_neighbors = self.find_live_neighborhood(location)
        return len(my_neighbors)

    def find_live_neighborhood(self, location):

        neighbor_offsets = set([(-1,0),(1,0),(0,-1),(0,1),
                            (-1,-1),(1,1),(1,-1),(-1,1)])
        my_neighbors = set()

        x,y = location

        if self.num_live() <= 1 :
            return set()
        else :
            for n in neighbor_offsets :
                xoffset, yoffset = n

                if (x+xoffset,y+yoffset) in self.live_cells:
                     my_neighbors.add((x+xoffset,y+yoffset))

            return my_neighbors

    # dead neighbors of living cells, aka candidates for birth
    def zombies(self,location):

        neighbor_offsets = set([(-1,0),(1,0),(0,-1),(0,1),
                            (-1,-1),(1,1),(1,-1),(-1,1)])

        z = set()

        x,y = location

        if self.num_live() <= 1 :
            return set()
        else :
            for n in neighbor_offsets :
                xoffset, yoffset = n

                if (x+xoffset,y+yoffset) not in self.live_cells:
                     z.add((x+xoffset,y+yoffset))

        return z

    def add_locations(self, locations):
        for (x,y) in locations :
            self.add_one_location((x, y))
        pass

    def next_gen(self):
        # default is that a cell dies
        next_gen = set()

        ## Stasis: if a living cell is surrounded by two or three living cells, it survives.
        for (x,y) in self.live_cells:
            # print((x,y), ' ',self.num_live_neighbors((x,y)))
            if self.num_live_neighbors((x,y)) in [2, 3]:
                # print('add')
                next_gen.add((x,y))

        birth_candidates = set()
        z = set()

        ## Birth: if a dead cell is surrounded by exactly three cells, it becomes a live cell.
        for(x,y) in self.live_cells:
            z = self.zombies((x,y))
            for (birthx,birthy) in z:
                birth_candidates.add((birthx,birthy))

        for (x,y) in birth_candidates:
            if self.num_live_neighbors((x,y)) == 3:
                next_gen.add((x,y))

        self.live_cells = next_gen

    def is_alive(self, position):
        # print(position)
        # print(self.live_cells)
        if position in self.live_cells:
            return True

        return False







class conway_test(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.one_cell_board = Board()
        self.one_cell_board.add_one_location((0, 0))
        self.stable_board_locations = set([(0, 0),(0, 1),(1, 1), (1, 0)])
        self.stable = Board()
        self.stable.add_locations(self.stable_board_locations)
        self.niner_board = Board()
        self.niner_board.add_locations(
            {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        )
        self.make_babies = Board()
        self.make_babies.add_locations(set([(0, 0), (0, 1), (1, 0)]))

    #  Helps me make sure tests are running.
    def test_smoke(self):
        self.assertEqual(True, True)

    def test_can_create_board(self):
        self.assertIsNotNone(self.board)

    def test_empty_board_live_count_is_zero(self):
        self.assertEqual(self.board.num_live(),0)

    def test_can_add_cell(self):
        self.board.add_one_location((0, 0))
        self.assertEqual(self.board.num_live(),1)

    def test_one_cell_has_no_neighbors(self):
        self.assertEqual(self.one_cell_board.num_live_neighbors((0,0)), 0)

    def test_can_add_location(self):
          self.assertEqual(self.stable.num_live(), 4)

    def test_find_neighborhood_single(self):
        self.assertEqual(self.one_cell_board.find_live_neighborhood((0, 0)), set())

    def test_find_neigborhood_stable(self):
       self.assertEqual(self.stable.find_live_neighborhood((1, 0)), set([(0, 1), (1, 1), (0, 0)]))

    def test_find_neigborhood_niner(self):
        self.assertEqual(self.niner_board.find_live_neighborhood((0, 0)),
                         set([(0, 1), (1, 1), (1, 0)]))

    def test_count_neighbors_exclude_cell(self):
        self.assertEqual(self.niner_board.num_live_neighbors((1, 1)), 8)

    ## Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
    def test_one_cell_board_dies(self):
        self.one_cell_board.next_gen()
        self.assertEqual(self.one_cell_board.num_live(),0)

    ## Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
    ##   ***
    ##   **
    ##    ^  dies
    def test_overpopulation_die(self):
        over_populated = Board()
        over_populated.add_locations( {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)})
        self.assertEqual(over_populated.num_live_neighbors((1,1)),4)
        over_populated.next_gen()
        self.assertEqual(over_populated.is_alive((1, 1)),False)

        # the corner of the all nine board should live as it only has three
        # the middle of the all nine board should die as it has 8 neighbors
        self.assertEqual(self.niner_board.num_live_neighbors((0,0)),3)
        self.niner_board.next_gen()
        self.assertEqual(self.niner_board.is_alive((1, 1)), False)
        self.assertEqual(self.niner_board.is_alive((0, 0)), True)

    def test_statis_three_neighbors(self):
    ## Stasis: if a living cell is surrounded by two or three living cells, it survives.
        my_board = Board()
        my_board.add_locations(self.stable_board_locations)
        my_board.next_gen()
        self.assertEqual(my_board.live_cells,self.stable_board_locations)


    def test_zombies(self):
        result_z =  set([(0,2),(1,2),(2,2),(2,1),(2,0)])
        #  note... this is an infinite board... no outer edges
        self.assertEqual(self.make_babies.zombies((1,1)),result_z )


    ## Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.
    ##  **
    ##  *.
    ##   ^ a new baby here  (1,1)

    def test_birth(self):

        self.assertEqual(self.make_babies.is_alive((1, 1)), False)
        self.assertEqual(self.make_babies.num_live_neighbors((1, 1)), 3)
        self.make_babies.next_gen()
        self.assertEqual(self.make_babies.is_alive((1, 1)), True)

    def test_blinker(self):

        blinker = Board()
        blinker.add_locations({(1, 0), (1, 1), (1, 2)})
        save_blinker = Board()
        save_blinker.add_locations(blinker.live_cells)

        blinker.next_gen()
        self.assertNotEqual(blinker.live_cells, save_blinker.live_cells)
        blinker.next_gen()
        self.assertEqual(blinker.live_cells,save_blinker.live_cells)



if __name__ == '__main__':
    unittest.main()