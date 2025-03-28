from random import sample

def pick_n_different_random_numbers(start: int, end: int, n: int) -> list:
    numbers = range(start, end)
    sample_numbers = sample(numbers, n)
    return sample_numbers

