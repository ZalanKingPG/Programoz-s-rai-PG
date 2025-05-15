import random

def valid_lotto_szam(szam, legkisebb, maximum, vane):
    while True:
        try:
            num = int(input(szam))
            if num in vane:
                print("Ezt a számot már megadtad, kérlek válassz másikat.")
            elif legkisebb <= num <= maximum:
                return num
            else:
                print(f"Csak a {legkisebb} és a {maximum} közötti számok érvényesek!")
        except ValueError:
            print("Ervényes számot adj meg!")

def kilep():
    stop = input("Nyomd meg a 'q' betűt a kilépéshez, vagy bármi mást a folytatáshoz: ").strip().lower()
    return stop == 'q'

def otoslotto():
    while True:
        szamok = list(range(1, 91))
        otos_nyeroszamok = random.sample(szamok, 5)

        userSzamok5 = []
        print("Add meg a nyerőszámaidat (1 és 90 között)")
        for i in range(5):
            userSzamok5.append(valid_lotto_szam(f"{i + 1}. szám: ", 1 ,90, userSzamok5))

        talalatok = set(userSzamok5) & set(otos_nyeroszamok)
        print(f"Nyerőszámok: {sorted(otos_nyeroszamok)}")
        print(f"A találataid: {len(talalatok)} ({sorted(talalatok)})")

        if len(szamok) == 5:
            print("GRATULÁLOK! Nyertél 1,035 milliárd Ft-ot!")
        else:
            print("Nem nyertél. Próbáld újra!")

        if kilep():
            break


def hatoslotto():
    while True:
        szamok = list(range(1, 46))
        hatos_nyeroszamok = random.sample(szamok, 6)

        userSzamok6 = []
        print("Add meg a nyerőszámaidat (1 és 45 között)")
        for i in range(6):
            userSzamok6.append(valid_lotto_szam(f"{i + 1}, szám: ", 1, 45 ,userSzamok6))

        talalatok = set(userSzamok6) & set(hatos_nyeroszamok)
        print(f"Nyerőszámok: {sorted(hatos_nyeroszamok)}")
        print(f"A találataid: {len(talalatok)} ({sorted(talalatok)})")

        if len(talalatok) == 6:
            print("GRATULÁLOK! Nyertél 1,93 milliárd Ft-ot!")
        else:
            print("Nem nyertél. Próbáld újra!")

        if kilep():
            break


def skandinavlotto():
    while True:
        szamok = list(range(1, 31))
        skandinav_nyeroszam = random.sample(szamok, 7)

        user_skandinav = []
        print("Add meg a nyerőszámaidat (1 és 30 között)")
        for i in range(7):
            user_skandinav.append(valid_lotto_szam(f"{i + 1}, szám: ", 1, 30, user_skandinav))

        talalatok = set(user_skandinav) & set(skandinav_nyeroszam)
        print(f"A nyerőszámok: {sorted(skandinav_nyeroszam)}")
        print(f"A találataid: {len(talalatok)} ({sorted(talalatok)})")

        if len(talalatok) == 7:
            print("GRATULÁLOK! Nyertél 365 millió Ft-ot!")
        else:
            print("Nem nyertél. Próbáld újra!")

        if kilep():
            break


def main():
    while True:
        print("\nVálasz egy lottót:")
        print("1. Ötös lottó.")
        print("2. Hatos lottó.")
        print("3. Skandináv lottó.")
        print("4. Kilépés.")

        valasztas = input("Kérlek írd be a játék számát (1-4): ")
        if valasztas == '1':
            otoslotto()
        elif valasztas == '2':
            hatoslotto()
        elif valasztas == '3':
            skandinavlotto()
        elif valasztas == '4':
            print("Köszönjük hogy játszottál!")
            break
        else:
            print("Érvénytelen választás, kérlek próbáld újra.")


if __name__ == '__main__':
    main()
