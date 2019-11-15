import random


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


def roll():
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    numbers = (number1, number2)
    return numbers
