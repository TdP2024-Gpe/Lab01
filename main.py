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
max_level = 0


def read_domande():
    """
    Leggo il file domande.txt ed estraggo le singole domande nella lista
    domanda = []. Quando trovo il rigo vuoto inserisco la domanda nella lista
    db_domande [[domanda1], [domanda2],....].
    """
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
    """Leggo il file punti.txt e creo un dizionario (nome: punti)"""
    _f = open("punti.txt", "r")

    for x in _f:
        x = x.strip()
        (key, val) = x.split()  # Inserisco riga per riga i player al dizionario
        db_punti._punti.update({key: int(val)})
        # print(db_punti._punti)

    # print(db_punti._punti)

    _f.close()


def sortpunti(db_punti_punti):
    return {
        k: v
        for k, v in sorted(
            db_punti_punti.items(), key=lambda item: item[1], reverse=True
        )
    }


def writefile(db_punti):
    _w = ""  # Stringa da scrivere nel file punti.txt
    _f = open("punti.txt", "w")
    for x in db_punti:
        if _w == "":
            _w = f"{x} {db_punti[x]}\n"
            # print(_w)
        else:
            _w = _w + f"{x} {db_punti[x]}\n"
            # print(_w)
        # print(_w)
    _f.write(f"{_w}")
    _f.close()
    print(f"\nLa classifica attuale è:\n{_w}")


def save_punti(level):
    """Salvo il punteggio totalizzato nel file punti.txt"""
    print(f"Hai totalizzato {level} punti!")
    _n = input("Inserisci il tuo nickname: ")
    # print(db_punti._punti)
    if _n in db_punti._punti:  # controllo se il nickname è già presente nel db
        # print(db_punti._punti[_n])
        if level > int(db_punti._punti[_n]):  # Aggiorno il punteggio solo se è maggiore
            db_punti._punti[_n] = int(level)
            db_punti._punti = sortpunti(db_punti._punti)
            writefile(db_punti._punti)
        else:
            writefile(db_punti._punti)
    else:
        db_punti._punti[_n] = int(level)
        db_punti._punti = sortpunti(db_punti._punti)
        # print(db_punti._punti)
        writefile(db_punti._punti)
        # print(db_punti._punti)


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

    try:
        x = int(input("Inserisci la risposta: "))
    except ValueError:
        x = int(input("Riprova!, valore non accettato. Inserisci la risposta: "))

    if _r[x - 1] == _d[2] and level < db_domande.max_level():
        level = level + 1
        print("Risposta corretta!\n")
        ask_a_question(level)
    elif _r[x - 1] == _d[2] and level >= db_domande.max_level():
        print("Risposta Corretta! Hai raggiunto il massimo livello.\n")
        save_punti(level)
    else:
        print(f"Risposta sbagliata! La risposta corretta era: {_r.index(_d[2]) + 1}\n")
        save_punti(level)


read_punti()
ask_a_question(level)
