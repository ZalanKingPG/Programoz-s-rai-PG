file = open("EUcsatlakozas.txt", "r", encoding="utf-8")
sorok = file.readlines()
file.close()

class EU:
    def __init__(self, orszag, ev, honap, nap):
        self.orszag = orszag
        self.ev = int(ev)
        self.honap = int(honap)
        self.nap = int(nap)

adatok = []
for i in range(len(sorok)):
    darabok = sorok[i].strip().split(";")
    szeletek = darabok[1].split(".")
    a = EU(darabok[0], szeletek[0], szeletek[1], szeletek[2])
    adatok.append(a)

#3. Feladat
allam = 0
for i in range(len(adatok)):
    if adatok[i].ev < 2018:
        allam += 1
print(f"3. Feladat: EU tagállamainak száma: {allam} db")
#4. Feladat
allam = 0
for i in range(len(adatok)):
    if adatok[i].ev == 2007:
        allam += 1
print(f"4. Feladat: 2007-ben {allam} orszag csatlakozott.")
#5. Feladat
for i in range(len(adatok)):
    if adatok[i].orszag == "Magyarország":
        print(f"5. Feladat: Magyarország csatlakozásának dátuma: {adatok[i].ev}.{str(adatok[i].honap).zfill(2)}.{str(adatok[i].nap).zfill(2)}")
#6. Feladat
volt = False
for i in range(len(adatok)):
    if adatok[i].honap == 5:
        volt = True
if volt == True:
    print("6. Feladat: Májusban volt csatlakozás!")
else:
    print("6. Feladat: Májusban nem volt csatlakozás!")
#7. Feladat
maxev = 0
maxorszag = ""
for i in range(len(adatok)):
    if maxev < adatok[i].ev:
        maxev = adatok[i].ev
        maxorszag = adatok[i].orszag
print(f"7. Feladat: Legutoljára csatlakozott ország: {maxorszag}")
#8. Feladat
evek = set()
for i in range(len(adatok)):
    evek.add(adatok[i].ev)
for e in evek:
    db = 0
    for i in range(len(adatok)):
        if adatok[i].ev == e:
            db += 1
    print(f"8. Feladat: {e} - {db}")