#Rebecca Hamid ID: 23803320

import unittest
from main import Die, DiceGame

class TestDiceGame(unittest.TestCase):
    def test_evaluate_roll_negative_total(self):
        game = DiceGame()
        self.assertEqual(game.evaluate_roll(-1), "Invalid Total")

    def test_roll_type(self):
        die = Die()
        self.assertIsInstance(die.roll(), int)

    def test_game_result_all_values(self):
        game = DiceGame()
        outcomes = {"Win": False, "Lose": False, "Roll Again": False}
        for total in range(2, 13):
            result = game.evaluate_roll(total)
            if result in outcomes:
                outcomes[result] = True
        self.assertTrue(outcomes["Win"])
        self.assertTrue(outcomes["Lose"])
        self.assertTrue(outcomes["Roll Again"])

if __name__ == "__main__":
    unittest.main()