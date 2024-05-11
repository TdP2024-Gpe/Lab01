""" 
Modulo delle domande
"""

from dataclasses import dataclass

import tabulate


""" class Domanda:
    def __init__(
        self, domanda, livello, risposta_c, risposta_s1, risposta_s2, risposta_s3
    ):
        self.domanda = domanda
        self.livello = livello
        self.risposta_c = risposta_c
        self.risposta_s1 = risposta_s1
        self.risposta_s2 = risposta_s2
        self.risposta_s3 = risposta_s3

    def __str__(self) -> str:
        return f" domanda: {self.domanda}\n livello: {self.livello}"
 """


@dataclass
class Domanda:
    domanda: str
    livello: int
    risposta_c: str
    risposta_s1: str
    risposta_s2: str
    risposta_s3: str


class ElencoDomande:
    def __init__(self):
        self._domande = []

    def append(self, domanda):
        self._domande.append(domanda)

    def __str__(self):
        return f"{self._domande}"

    def tabella(self):
        header = [
            "Pos.",
            "Domanda",
            "Livello",
            "Risposta_C",
            "Risposta_S1",
            "Risposta_S2",
            "Risposta_S3",
            "",
        ]
        rows = self._domande
        return tabulate.tabulate(rows, header, tablefmt="grid", showindex="always")


@dataclass
class Punti:
    name: str
    punti: int


class ListaPunti:

    def __init__(self):
        self._punti = {}

    def update(self, name):
        self._punti.update(name)

    def __str__(self):
        return f"{self._punti}"


""" 
TESTING AREA
"""


def _domanda_test():
    print(__name__)
    d1 = Domanda(
        "Qual è il Capoluogo di Regione della Toscana?",
        0,
        "Firenze",
        "Cagliari",
        "Bari",
        "Milano",
    )
    print(d1)


if __name__ == "__main__":
    _domanda_test()
