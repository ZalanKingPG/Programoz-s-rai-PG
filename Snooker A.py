f = open("Snooker.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()
#1. Feladat
class Main:
    def __init__(self, hely, nev, orszag, nyeremeny):
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
print(f"\tA világranglistán {len(adatok)} ember áll")
#3. Feladat
print("3. Feladat")
van = False
for i in range(len(adatok)):
    if adatok[i].orszag == "Belgium":
        van = True
        break
if van == True:
    print("\tVan belga játékos a világranglistán.")
else:
    print("\tNincs belega játékos a világranglistán.")
#4. Feladat
print("4. Feladat")
wossz =0
db = 0
for i in range(len(adatok)):
    if adatok[i].orszag == "Wales":
        wossz += adatok[i].nyeremeny
        db += 1
print(f"\tA wales-i versenyzők átlagban {wossz / db:.2f} pénzt vittek haza")
#5. Feladat
print("5. Feladat")
legk = 100000000000000
maxi = 0
for i in range(len(adatok)):
    if adatok[i].nyeremeny < legk:
        legk = adatok[i].nyeremeny
        maxi = i
print(f"\tA legkevesebbet kereső játkos a világranglistán: {adatok[maxi].nev}")
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
    print(f"\t{i} versenyzői {ossz * 480}Ft-ot vittek haza")