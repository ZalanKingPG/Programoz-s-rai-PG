#olvassunk be dolgozatpontszámokat
#irjuk ki hogy hányas lett
#irjuk ki hogy mennyi lett az átlag és hogy hány otos lett
#adjuk meg a max pontszamot is

# 40% - 2
# 50% - 3
# 60% - 4
# 80% - 5


dolgozat_max = int(input("Hány pontos a dolgozat?: "))
osszeg = 0
db = 0

for i in range(100):
    pont = int(input("Hány pontot értél el?: "))

    if pont == -1:
        break
    else:
        db += 1
        szazalek = pont / dolgozat_max * 100
        if szazalek < 40:
            print("1-es")
            osszeg += 1
        elif szazalek < 50:
            print("2-es")
            osszeg += 2
        elif szazalek < 60:
            print("3-as")
            osszeg += 3
        elif szazalek < 80:
            print("4-es")
            osszeg += 4
        else:
            print("5-ös")
            osszeg += 5
atlag = osszeg / db
print(f"Az átlag: {atlag:02}")