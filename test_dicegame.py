#Rebecca Hamid ID: 23803320

import unittest
from dicegame import Die, DiceGame

class TestMyDiceGameExtras(unittest.TestCase):
    def test_die_rolls_are_random(self):
        die = Die()
        results = set(die.roll() for _ in range(100))
        # With enough rolls, we should see all numbers from 1 to 6
        for value in range(1, 7):
            self.assertIn(value, results)

    def test_multiple_rounds_append_to_history(self):
        game = DiceGame()
        history = []
        for _ in range(5):
            outcome = game.play_round()
            history.append(outcome)
        self.assertEqual(len(history), 5)
        # Each outcome should have four keys
        for outcome in history:
            self.assertTrue(all(k in outcome for k in ["roll1", "roll2", "total", "result"]))

    def test_game_result_possible_values(self):
        game = DiceGame()
        # Check for all possible results
        possible = set(game.evaluate_roll(total) for total in range(2, 13))
        expected = {"Win", "Lose", "Roll Again"}
        self.assertTrue(expected.issubset(possible))

if __name__ == "__main__":
    unittest.main()