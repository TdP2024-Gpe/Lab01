from multiprocessing import Value
import random
from domanda import ElencoDomande as e

from domanda import ListaPunti as l

""" 
d1 = d(
    "Qual è il fiume più lungo d'Italia?",
    0,
    "Po",
    "Arno",
    "Piave",
    "Adige",
)

print(d1)
"""
level = 0
db_domande = e()
db_punti = l()


def read_domande():
    _f = open("domande.txt", "r", encoding="UTF-8")
    # print(f.readline())

    domanda = []

    for x in _f:
        x = x.strip()
        if x != "":
            domanda.append(x)
        else:
            db_domande.append(domanda)
            domanda = []

    # print(db_domande.tabella())
    _f.close()


def read_punti():
    _f = open("punti.txt", "r")

    _gamer = {}

    for x in _f:
        x = x.strip()
        (key, val) = x.split()
        _gamer.update({key: val})
        # print(_gamer)

    db_punti.update(_gamer)

    print(db_punti)

    # print(_f.read())
    _f.close()


def save_punti(level):
    print(f"Hai totalizzato {level} punti!")
    _n = input("Inserisci il tuo nickname: ")
    _w = ""
    # print(db_punti._punti)
    if _n in db_punti._punti:
        # print(db_punti._punti[_n])
        if level > int(db_punti._punti[_n]):
            db_punti._punti[_n] = level
            _f = open("punti.txt", "w")
            for x in db_punti._punti:
                _w = _w + f"{x} {db_punti._punti[x]}\n"
                print(_w)
            _f.write(f"{_w}")
            _f.close()
            #     pass
            print(_w)
            print(db_punti._punti)


def ask_a_question(level):

    _level_d = []
    read_domande()
    for x in db_domande._domande:
        if x[1] == str(level):
            _level_d.append(x)
    _d = random.choice(_level_d)
    _dw = _d.copy()
    print(f"Domanda Livello: {_d[1]})")
    print(f" {_d[0]}")
    _r = []
    _r1 = _dw[random.randint(2, 5)]
    _r.append(_r1)
    print(f"  1. {_r1}")
    _dw.remove(_r1)
    _r2 = _dw[random.randint(2, 4)]
    _r.append(_r2)
    print(f"  2. {_r2}")
    _dw.remove(_r2)
    _r3 = _dw[random.randint(2, 3)]
    _r.append(_r3)
    print(f"  3. {_r3}")
    _dw.remove(_r3)
    _r4 = _dw[2]
    _r.append(_r4)
    print(f"  4. {_r4}")

    x = int(input("Inserisci la risposta: "))

    if _r[x - 1] == _d[2]:
        level = level + 1
        print("Risposta corretta!")
        ask_a_question(level)
    else:
        print("Risposta sbagliata! La risposta corretta era: ", _r.index(_d[2]) + 1)
        save_punti(level)


read_punti()
ask_a_question(level)
