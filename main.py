import numpy as np
import numpy.random

from Reader import Reader
from ausdruck import print_pdf

from datetime import datetime

# Get the current time
time_now = datetime.now()
# Format the time with milliseconds
formatted_time = time_now.strftime("%Y--%m--%d--%H-%M-%S") + f"-{time_now.microsecond // 1000}"


if __name__ == "__main__":

    n = (6, 12)

    # get names
    reader = Reader("names.txt")
    names = reader.get_names_randomized()
    # Make sure that the file 'names.txt' is in the same folder as this script.
    # Please do not push 'names.txt' with any sensitive information.


    offset = round(len(names) * 0.6) # Set offset to roughly 60% of number of names
    assert offset != 0 or offset != len(names), "Offset can not be 0 or 'len(names)' as this would result in murdering yourself."
    assert offset < len(names), "Offset must be less than number of names!"
    # Offset victim list to get murder
    victims = names[offset:] + names[:offset]

    # Needed for moderator list
    data = np.array([names, victims])

    # Slice list into chunks, to create rows in PDF.
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

    # Flip each row of the victim list. Necessary as the back side of the page is printed the other way around.
    victims_flipped = [list(reversed(a)) for a in victims]

    #Create PDFs for printing
    print_pdf(names, "lists/murdergame_murderers__" + formatted_time + ".pdf", n=n)
    print_pdf(victims_flipped, "lists/murdergame_victims__" +formatted_time + ".pdf", n=n)
    print("PDFs were generated and saved in folder 'lists'.")

    # Create list for moderators.
    numpy.savetxt("lists/mod_list__" + formatted_time + ".csv", data.transpose(), delimiter=",",fmt="%s")
    print("Moderator list was generated and saved in folder 'lists'.")




