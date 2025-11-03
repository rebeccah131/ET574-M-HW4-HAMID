#Rebecca Hamid ID: 23803320

import unittest
from main import Die, DiceGame

class TestDiceGame(unittest.TestCase):
    def test_negative_total(self):
        game = DiceGame()
        self.assertEqual(game.evaluate_roll(-1), "Invalid Total")

    def test_roll_type(self):
        die = Die()
        self.assertIsInstance(die.roll(), int)

    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            Die(sides=0)

if __name__ == "__main__":
    unittest.main()