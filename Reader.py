import numpy as np


class Reader:
    URI: str

    def __init__(self, URI):
        self.URI = URI

    def reads(self) -> str:
        with open(self.URI) as f:
            t = f.read()
        return t.replace(" ", "")

    def __str__(self):
        return self.reads()

    def get_names(self, sep=',') -> np.ndarray:
        l = self.reads().split(sep)
        return np.asarray(l)
