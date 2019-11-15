import random


class Dice:
    def roll(self):
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        numbers = (number1, number2)
        return numbers


dice = Dice()
print(dice.roll())