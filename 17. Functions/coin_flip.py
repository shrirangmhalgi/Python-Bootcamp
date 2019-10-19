from random import random

def flip_coin():
    if random() > 0.5:
        print("Heads")
    else:
        print("Tails")

flip_coin()