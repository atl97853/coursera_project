import random

def random_number():
    return random.randint(1, 100)

def random_sum():
    sum = random_number() + random_number()
    print(sum)
    return sum

random_sum()
