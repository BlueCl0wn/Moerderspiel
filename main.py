import numpy as np
from Reader import Reader
import random
import numpy.random

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


def randomize(name_list: np.ndarray) -> np.ndarray:
    rng = np.random.default_rng()
    rng.shuffle(name_list)
    return name_list


def create_murder_dict_v2(name_list):
    """"""
    # create solution dictonary
    solution = {}

    # save first murderer for later usage
    first = name_list[0]

    # declare murderer variable and assign 'first'
    murderer = first

    # looping over name_list an assigned victims to murderers
    for name in name_list:
        solution[murderer] = name  # add dict entry
        murderer = name  # redefine murderer

    # create last dict entry with 'first'
    solution[murderer] = first

    return solution


print(create_murder_dict_v2(names))
