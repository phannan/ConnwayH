import unittest
from Conway.Conway import *


class test_Life(unittest.TestCase):

      def test_life_smoke(self):
        life = Life
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()