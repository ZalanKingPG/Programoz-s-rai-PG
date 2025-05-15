f = open("hangman szavak", "r", encoding="utf-8")
sorok = f.readlines()
f.close()
adatok = []
for i in range(len(sorok)):
    a = sorok[i].strip()
    adatok.append(a)
stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    """
]

import random
word = random.randint(0, len(adatok) - 1)
feladvany = adatok[word]

tip = "_" * len(feladvany)
szint = 0
while True:
    print(f"A gondolt szó: {tip}")
    print(stages[szint])
    betu = input("Kérek egy betűt: ").lower()
    if feladvany.find(betu) > -1:
        elozo = tip
        tip = ""
        for i in range(len(feladvany)):
            if feladvany[i] == betu:
                tip += betu
            else:
                tip += elozo[i]
    else:
        szint += 1
    if szint == 6:
        print("Fölakaszottak")
        print(stages[szint])
        print(f"A szó a {feladvany} volt")
        break
    if tip == feladvany:
        print("Kitaláltad!")
        print(feladvany)
        break