#Rebecca Hamid ID: 23803320

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        total = roll1 + roll2
        result = self.evaluate_roll(total)
        return {
            'roll1': roll1,
            'roll2': roll2,
            'total': total,
            'result': result
        }

    def evaluate_roll(self, total):
        if total in (7, 11):
            return "Win"
        elif total in (2, 3, 12):
            return "Lose"
        elif total in (4, 5, 6, 8, 9, 10):
            return "Roll Again"
        else:
            return "Invalid Total"
            

def main():
    print("Welcome to the Dice Game!")
    game = DiceGame()
    while True:
        print("\nMenu:\n  1. Play a round\n  2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            outcome = game.play_round()
            print(f"Die 1: {outcome['roll1']}, Die 2: {outcome['roll2']}, Total: {outcome['total']}")
            print(f"Result: {outcome['result']}")
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()