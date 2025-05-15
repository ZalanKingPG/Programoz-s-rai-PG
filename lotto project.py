import random

def otoslotto():
    run = True
    while run:
        szamok = list(range(1, 91))
        otos_nyeroszamok = random.sample(szamok, 5)


        userSzamok5 = []
        for i in range(5):
            userSzamok5.append(int(input("Kérlek írd be a nyerőszámaidat: ")))
            if userSzamok5[i] > 90 or userSzamok5[i] == '':
                print("Csak az 1 és 90 közötti számok játszanak.")
                print("Kérlek próbáld újra")
                break
        if otos_nyeroszamok != userSzamok5:
            print("Ez nem talált.")
            print("Nem nyertél semmit.")
            print(f"A nyerő számok a {otos_nyeroszamok} voltak")
        else:
            print("NYERTÉL")
            print("A nyereményed: 1,035 milliárd Ft")
        print("Ki akarsz lépni?")
        stop = input("Nyomd meg a 'q' betűt a kilépéshez: ")
        if stop == 'q':
            break
        else:
            print("Akkor folytassuk.")
            continue




def hatoslotto():
    run = True
    while run:
        szamok = list(range(1, 46))
        hatos_nyeroszamok = random.sample(szamok, 6)


        userSzamok6 = []
        for i in range(6):
            userSzamok6.append(int(input("Kérlek írd be a nyrőszámaidat: ")))
            if userSzamok6[i] > 45 or userSzamok6 == "":
                print("Csak az 1 és 45 közötti számok játszanak.")
                print("Kérlek próbáld újra")
                break
        print("Ki akarsz lépni?")
        stop = input("Nyomd meg a 'q' betűt a kilépéshez: ")
        if stop == 'q':
            break
        else:
            print("Akkor fojtassuk.")
            continue



def skandinavlotto():
    run = True
    while  run:
        szamok = list(range(1, 31))
        skandinav_nyeroszamok = random.sample(szamok, 7)


        user_skandinav = []
        for i in range(7):
            print(i)
            user_skandinav.append(int(input("Kérlek írd be a nyerőszámaidat: ")))
            if user_skandinav[i] > 30 or user_skandinav[i] == "":
                print("Csak az 1 és 30 közötti számok játszanak.")
                print("Kérlek próbáld újra")
                break
        print("Ki akarsz lépni?")
        stop = input("Nyomd meg a 'q' betűt a kilépéshez: ")
        if stop == 'q':
            break
        else:
            print("Akkor fojtassuk.")
            continue


def eurojackpot():
    pass
    run = True
    while run:
        szamok = list(range(1, 51))
        euro_nyeroszamok = random.sample(szamok, 5)
        szamok_bonus = list(range(1, 3))
        bonus_nyeroszamok = random.sample(szamok_bonus, 2)



        user_euro = []
        for i in range(5):
            user_euro.append(int(input("Kérlek írd be a nyerőszámaidat: ")))
            if user_euro[i] > 50 or user_euro == "":
                print("Csak az 1 és 50 közötti számok játszanak.")
                print("Kérlek próbáld újra")
                break



        user_bonus = []
        for i in range(2):
            user_bonus.append(int(input("Kérek kettő bónusz nyerőszámot: ")))
            if user_bonus[i] > 12 or user_bonus[i] == "":
                print("Csak az 1 és 12 közötti számok játszanak.")
                print("Kérlek próbáld újra")
                break

#def luxor():
#    pass


#def joker():
#    pass


def main():
    is_running = True
    while is_running:
        print("1. Ötös lotto.")
        print("2. Hatos lotto.")
        print("3. Skandináv lotto.")
#        print("4. Euro Jackpot lotto.")
        print("5. Kilép")
        #    print("6. Luxor.")
        #    print("7. Joker.")
        valasztas = input("Kérlek válassz a játékok közül(1-5): ")
        if valasztas == '1':
            otoslotto()
        elif valasztas == '2':
            hatoslotto()
        elif valasztas == '3':
            skandinavlotto()
#        elif valasztas == '4':
#            eurojackpot()
        elif valasztas == '5':
            print("Köszönjük hogy velünk tartott")
            is_running = False
        else:
            print("Ilyen választás nincs kérlek próbáld újra.")

if __name__ == '__main__':
    main()
