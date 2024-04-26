import random

randomInteger = random.randint(1, 10)
print(randomInteger)

randomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")



#43 heads or tails coding exercise


import random
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")    