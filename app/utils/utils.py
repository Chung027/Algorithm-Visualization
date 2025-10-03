import random

def generate_random_list(size):
    """
    Generate a list of random integers for sort visualization
    """
    # option 1 used random sample function to generate random list from 1 to 150 with choice size
    #list = random.sample(range(1,150), size)
    # option 2 used randint function
    list = [random.randint(1, 150) for _ in range(size)]
    return list