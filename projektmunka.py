tabla = []
for i in range(10):
    sor = []
    for j in range(10):
        sor.append(" ")
    tabla.append(sor)
print(tabla)

player = "X"

while True:
    print("  0  1  2  3  4  5  6  7  8  9")

    for i in range(10):
        print(i, end="")
        for j in range(10):
            print(f"[{tabla[i][j]}]", end="")
        print()

    print(f"{player} játékos következik")

    sor = int(input("sor: "))
    oszlop = int(input("Oszlop: "))
    if tabla[sor][oszlop] == " ":
        tabla[sor][oszlop] = player
        db = 0
        max = 0
        for j in range(10):
            if tabla[sor][j] == player:
                db += 1
            else:
                if db > max:
                    max = db
                db = 0
        db = 0
        for i in range(10):
            if tabla[i][oszlop] == player:
                db += 1
            else:
                if db > max:
                    max = db
                db = 0
        if max == 5:
            print(f"{player} Győzött")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("Oda nem léphetsz")
