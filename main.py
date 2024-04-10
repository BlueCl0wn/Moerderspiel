import numpy as np
import numpy.random

from Reader import Reader
from ausdruck import print_pdf, print_text


def randomize(name_list: np.ndarray) -> list:
    rng = np.random.default_rng()
    rng.shuffle(name_list)
    return name_list.tolist()



if __name__ == "__main__":

    n = (6, 12)

    # get names
    reader = Reader("names.txt")
    names = randomize(reader.get_names())
    # print(names)



    # do murder stuff
    victims = names[1:] + [names[0]]
    data = [names, victims]


    # slice list into chunks
    names = [names[i:i + n[0]] for i in range(0, len(names), n[0])]
    victims = [victims[i:i + n[0]] for i in range(0, len(victims), n[0])]
    # print("names: ", names)
    # print("victims: ", victims)

    # print(np.asarray(data).transpose())

    names = [[name + "\n\n\n" for name in namess] for namess in names]
    victims = [["Opfer\n\n\n" + victim for victim in victimss] for victimss in victims]

    #do the magic
    print(names)
    print_pdf(names, "murdergame_murderers.pdf", n=n)
    print_pdf(victims, "murdergame_victims.pdf", n=n)

    mod_list = np.asarray([data[0],
                           np.full(fill_value="\t\t\t", shape=len(data[0]), dtype=str),
                           data[1],
                           np.full(fill_value="\n", shape=len(data[0]), dtype=str)])
    print(mod_list)
    print()
    print(mod_list.transpose())
    print()
    print_text(mod_list, URI="mod_list", n=(1, 1))



