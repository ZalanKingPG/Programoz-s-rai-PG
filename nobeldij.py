f = open("nobeldij.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class Main:
    def __init__(self, ev, tipus, keresztnev, vezeteknev):
        self.ev = int(ev)
        self.tipus = tipus
        self.keresztnev = keresztnev
        self.vezeteknev = vezeteknev
#2. Feladat
adatok = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    a = Main(darabok[0], darabok[1], darabok[2], darabok[3])
    adatok.append(a)
#3. Feladat
for i in range(len(adatok)):
    if adatok[i].keresztnev == "Arthur B." and adatok[i].vezeteknev == "McDonald":
        print(f"3. Feladat: {adatok[i].tipus}")
        break
#4. Feladat
for i in range(len(adatok)):
    if adatok[i].ev == 2017 and adatok[i].tipus == "irodalmi":
        print(f"4. Feladat: {adatok[i].keresztnev} {adatok[i].vezeteknev}")
        break
#5. Feladat
print("5. Feladat: ")
for i in range(len(adatok)):
    if adatok[i].ev >= 1990 and adatok[i].vezeteknev == "":
        print(f"\t{adatok[i].keresztnev}")
#6. Feladat
print("6. Feladat")
for i in range(len(adatok)):
    if adatok[i].vezeteknev.count("Curie") > 0:
        print(f"{adatok[i].ev}: {adatok[i].keresztnev} {adatok[i].vezeteknev} ({adatok[i].tipus})")
#7. Feladat
print("7. Feladat")
nobel = set()
for i in range(len(adatok)):
    nobel.add(adatok[i].tipus)
for i in nobel:
    ossz = 0
    for j in range(len(adatok)):
        if i == adatok[j].tipus:
            ossz += 1
    print(f"{i}: {ossz} hadb")
#8. Feladat
f = open("orvosi.txt", "w", encoding="utf-8")
for i in range(len(adatok)):
    if adatok[i].tipus == "orvosi":
        print(f"{adatok[i].ev}: {adatok[i].keresztnev} {adatok[i].vezeteknev}", file=f)