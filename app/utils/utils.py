import random

def generate_random_list(size):
    """
    Generate a list of random integers for sort visualization
    """
    # option 1 used random sample function to generate random list from 1 to 150 with choice size
    #list = random.sample(range(1,150), size)
    # option 2 used randint function
    list = [random.randint(1, 300) for _ in range(size)]
    return list

def figure_layout(list_size):
    # säkerställa om man råkar skicka in en list
    if isinstance(list_size, list):
        list_size = len(list_size)

    if list_size <= 20:
        tickvals = [1] + list(range(2, list_size+1))   # visa alla från 1 till size
    elif list_size <= 60:
        # Visa ticks vid 1, 5, 10, 15, 20 ... upp till size
        tickvals = [1] + list(range(5, list_size+1, 5))
    else:
        # Visa ticks vid 1, 10, 20, 30 ... upp till size
        tickvals = [1] + list(range(10, list_size+1, 10))
    ticktext = [str(v) for v in tickvals]

    return tickvals, ticktext