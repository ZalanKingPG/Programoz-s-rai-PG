file = open("Kérdések", "r", encoding="utf-8")
sorok = file.readlines()
file.close()

file2 = open("nyeremények", "r", encoding="utf-8")
sorok2 = file2.readlines()
file2.close()

reward = []
for i in range(len(sorok2)):
    winnnnings = sorok2[i].strip()
    reward.append(winnnnings)


class Valaszok:
    def __init__(self, kerdes, a, b, c, d, helyes):
        self.kerdes = kerdes
        self.valaszok = {"A": a, "B": b, "C": c, "D": d}
        self.helyes = helyes

adatok = []
for i in sorok:
    quest = i.strip().split(";")
    if len(quest) == 6:
        x = Valaszok(quest[0], quest[1], quest[2], quest[3], quest[4], quest[5])
        adatok.append(x)
    else:
        print(f"Hiba: Hiányos sor itt {i}")


print("Üdvözöljük a legyen ön is milliomos nevezetű játékban!")
game_over = False
valasz = input("Készen áll? (i/n): ").strip().lower()
if valasz == "n":
    print("Köszönjük hogy játszottál")
    game_over = True
index = 0
while index < len(adatok) and not game_over:
    kerdes_szam = adatok[index]
    print(f"\n{index + 1}. kérdés: {kerdes_szam.kerdes}")

    for betu, valasz in kerdes_szam.valaszok.items():
        print(f"\t\t{betu}: {valasz}")

    be = input("Tegye meg a válaszát: ").strip().lower()
    benn = "n"
    if be == kerdes_szam.helyes:
        print("Helyes válasz")
        print(f"Feltételes nyeresége: {reward[index]}, ki akar szállni?")
        if index < len(adatok) - 1:
            benn = input("i/n: ").strip().lower()
            if benn == "i":
                print(f"Köszönjük, hogy játszottál! Végleges nyereményed: {reward[index]}")
                game_over = True
        else:
            print(f"Gratulálok megnyerted a játékot! A nyereményed {reward[index]}")
            game_over = True
    else:
        print(f"Köszönjük hogy játszottál! Végleges nyereményed: {reward[index]}")
        game_over = True

    if not game_over:
        index += 1