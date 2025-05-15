f = open("Snooker.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()
#1. Feladat
class Main:
    def __init__(self,hely, nev, orszag, nyeremeny):
        self.hely = int(hely)
        self.nev = nev
        self.orszag = orszag
        self.nyeremeny = int(nyeremeny)
adatok = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    a = Main(darabok[0], darabok[1], darabok[2], darabok[3])
    adatok.append(a)

#2. Feladat
print("2. Feladat")
print(f"\tA világranglistán szereplő játékosok száma: {len(adatok)}")
#3. Feladat
print("3. Feladat")
van = False
for i in range(len(adatok)):
    if adatok[i].orszag == "Magyarország":
        van = True
if van == True:
    print("\tVan magyar játékos a világranglistán.")
else:
    print("\tNincs magyar Játékos a világranglistán.")
#4. Feladat
print("4. Feladat")
osszossz = 0
kossz = 0
for i in range(len(adatok)):
    osszossz += adatok[i].nyeremeny
    if adatok[i].orszag == "Kína":
        kossz += adatok[i].nyeremeny
print(f"\tA kínai játékosok az ossznyeremény {kossz / osszossz * 100:.2f}%-át vitték haza")
#5. Feladat
print("5. Feladat")
for i in range(len(adatok)):
    if adatok[i].hely == 2:
        print(f"\tA világranglista 2. helyén áll: {adatok[i].nev}")
#6. Feladat
print("6. Feladat")
orszagok = set()
for i in range(len(adatok)):
    orszagok.add(adatok[i].orszag)
for i in orszagok:
    ossz = 0
    for j in range(len(adatok)):
        if i == adatok[j].orszag:
            ossz += adatok[j].nyeremeny
    print(f"\t{i} játékosai osszesen {ossz * 480}Ft-ot vittek haza.")