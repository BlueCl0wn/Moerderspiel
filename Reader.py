from warnings import catch_warnings

import numpy as np


class Reader:
    URI: str

    def __init__(self, URI):
        self.URI = URI

    def reads(self) -> str:
        #try:
        with open(self.URI) as f:
            t = f.read()
        #except FileNotFoundError:
        #    print(f"FileNotFoundError: There is no file with the name or directory {self.URI}."
        #          f"Make sure to create the file URI in reference to the same folder 'main.py' is in.")
        t = t.replace(" ", "")
        t = t.replace("\t", "")
        return t

    def __str__(self):
        return self.reads()

    def split(self, sep=','):
        return self.reads().split(sep)

    def get_names(self, sep=',') -> np.ndarray:
        l = self.split(sep)
        return np.asarray(l)

    def get_names_randomized(self, sep=','):
        name_list = np.asarray(self.split(sep)) # Convert list to np.ndarray
        rng = np.random.default_rng() # Create shuffle order
        rng.shuffle(name_list) # Shuffle name_list
        return name_list.tolist()

