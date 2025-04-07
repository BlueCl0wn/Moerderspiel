import numpy as np
import numpy.random

from Reader import Reader
from ausdruck import print_pdf, print_text

from datetime import datetime

# Get the current time
time_now = datetime.now()
# Format the time with milliseconds
formatted_time = time_now.strftime("%Y--%m--%d--%H-%M-%S") + f"-{time_now.microsecond // 1000}"

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


    offset = round(len(names) * 0.6) # Set offset to roughly 60% of number of names
    assert offset < len(names), "Offset must be less than number of names!"
    # do murder stuff
    victims = names[offset:] + names[:offset]
    # print(victims)
    data = np.array([names, victims])


    # slice list into chunks
    names = [names[i:i + n[0]] for i in range(0, len(names), n[0])]
    victims = [victims[i:i + n[0]] for i in range(0, len(victims), n[0])]
    # print("names: ", names)
    # print("victims: ", victims)

    # print(np.asarray(data).transpose())

    names = [[name + "\n\n\n--------" for name in namess] for namess in names]
    victims = [["Opfer\n\n\n" + victim for victim in victimss] for victimss in victims]
    # Cushion last list of names to fix mirrored printing issues
    def cushion(_list):
        return _list + (n[0] - len(_list)) * [" "]
    victims[-1] = cushion(victims[-1])
    names[-1] = cushion(names[-1])

    victims_flipped = [["Opfer\n\n\n" + victim for victim in victimss].reverse() for victimss in victims]
    victims_flipped = [list(reversed(a)) for a in victims]
    #Create PDFs for printing
    print_pdf(names, "lists/murdergame_murderers__" + formatted_time + ".pdf", n=n)
    print_pdf(victims_flipped, "lists/murdergame_victims__" +formatted_time + ".pdf", n=n)


    # Create list for moderators.


    numpy.savetxt("lists/mod_list__" + formatted_time + ".csv", data.transpose(), delimiter=",",fmt="%s")




