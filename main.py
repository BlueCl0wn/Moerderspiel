import numpy as np
from Reader import Reader
import random

names = ["Darek", "Paul", "Doro", "Niklas"]  # , "Moritz", "Mathilde", "Phuc", "Sophie"]

readers = Reader("names.txt")

names = readers.get_names()
print(names)

def find_random_name() -> str:
    """
    Returns a random element from a list and removes it from the original list.
    :return str: random element
    """
    _name = names.pop(random.randint(0, len(names) - 1))
    return _name


def create_murder_dict(name_list) -> dict:
    """
    Create a loop
    :param name_list:
    :return:
    """

    # create solution dictonary
    solution = {}

    # save first murderer for later usage
    first = find_random_name()

    # declare ongoing variable murderer
    murderer = first

    # loop doing the looping stuff
    for i in range(len(name_list)):
        victim = find_random_name()
        solution[murderer] = victim
        murderer = victim

    # closing circle bei setting last murderers victim as first murderer
    solution[murderer] = first

    return solution


print(create_murder_dict(names))
