f = open("ceges autok.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class mozgas:
    def __init__(self, nap, ido, rsz, azon, km, beki):
        self.nap = int(nap)
        self.ido = ido
        self.rsz = rsz
        self.azon = int(azon)
        self.km = int(km)
        self.beki = int(beki)

mozgasok = []

for i in range(len(sorok)):
    darabok = sorok[i].strip().split()
    m = mozgas(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    mozgasok.append(m)
#2. Feladat
print("2. Feladat")
for i in reversed(range(len(mozgasok))):
    if mozgasok[i].beki == 0:
        print(f"{mozgasok[i].nap}. nap rendszám {mozgasok[i].rsz}")
        break
#3. Feladat
print("3. Feladat")
benap = int(input("Írja be egy nap sorszámt: "))
print(f"Forgalom a {benap}. napon: ")
for i in range(len(mozgasok)):
    if mozgasok[i].nap == benap:
        print(f"{mozgasok[i].ido} {mozgasok[i].rsz} {mozgasok[i].azon} {'be' if mozgasok[i].beki == 1 else 'ki'}")
#4. Feladat
print("4. Feladat")
kih = 0
beh = 0
for i in range(len(mozgasok)):
    if mozgasok[i].beki == 0:
        kih += 1
    else:
        beh += 1
kint = kih - beh
print(f"A hónap végén {kint} autó volt kint")
#5. Feladat
print("5. Feladat")
rendszamok = set()
for i in range(len(mozgasok)):
    rendszamok.add(mozgasok[i].rsz)
for r in rendszamok:
    for i in range(len(mozgasok)):
        if mozgasok[i].rsz == r:
            elso = mozgasok[i].km
            break
    for i in reversed(range(len(mozgasok))):
        if mozgasok[i].rsz == r:
            utolso = mozgasok[i].km
            break
    megtett = utolso - elso
    print(f"{r} {megtett} km")
#6. Feladat
maxkm = 0
maxazon = 0
for i in range(len(mozgasok)):
    if mozgasok[i].beki == 0:
        for j in range(i + 1, len(mozgasok)):
            if mozgasok[j].azon == mozgasok[i].azon:
                megtett = mozgasok[j].km - mozgasok[i].km
                break
        if megtett > maxkm:
            maxkm = megtett
            maxazon = mozgasok[i].azon
print(f"Leghosszabb út: {maxkm}km, személy: {maxazon}")
#7. Feladat
bersz = input("Írjon be egy rendszámot: ")
f = open(bersz + "_menetlevel.txt", "w", encoding="utf-8")
for i in range(len(mozgasok)):
    if mozgasok[i].rsz == bersz and mozgasok[i].beki == 0:
        print(f"{mozgasok[i].azon}\t{mozgasok[i].nap}. {mozgasok[i].ido}\t{mozgasok[i].km} km\t", end="", file=f)
    if mozgasok[i].rsz == bersz and mozgasok[i].beki == 1:
        print(f"{mozgasok[i].nap}. {mozgasok[i].ido}\t{mozgasok[i].km} km\t", file=f)
f.close()