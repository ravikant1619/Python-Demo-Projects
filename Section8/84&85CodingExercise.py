#84Paint Area Calculator Question

import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)    



#--------------------------------------------------------------------------------------------------------

#85Prime Number Question

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        is_prime = False
    if is_prime:
        print("It is a prime number.")
    else:
        print("It's not a prime number.")

n = int(input())
prime_checker(number=n)