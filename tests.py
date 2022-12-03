import unittest
import game

class Test(unittest.TestCase):
    def test_updete(self):
        self.assertEqual(game.Bullet.__init__(True, True), True)

