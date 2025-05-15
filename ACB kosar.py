f = open("ACB kosar.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class ACB:
    def __init__(self, hazai, idegen, hazai_pont, idegen_pont, helyszín, időpont):
        self.hazai = hazai
        self.idegen = idegen
        self.hazai_pont = int(hazai_pont)
        self.idegen_pont = int(idegen_pont)
        self.helyszín = helyszín
        self.időpont = időpont


adatok = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    a = ACB(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5].split("-"))
    adatok.append(a)

#3. feladat
print("3. feladat")
hazai = 0
idegen = 0
for i in range(len(adatok)):
    if adatok[i].hazai == "Real Madrid":
        hazai += 1
    if adatok[i].idegen == "Real Madrid":
        idegen += 1
print(f"\tA Real Madrid hazai pályán: {hazai}, idegen pályán: {idegen} mérkőzést játszott le")
#4. feladat
print("4. feladat")
volt = False
for i in range(len(adatok)):
    if adatok[i].hazai_pont == adatok[i].idegen_pont:
        Volt = True
if volt:
    print(f"\tVolt döntetlen? igen")
else:
    print(f"\tVolt döntetlen? nem")
#5. feladat
print("5. feladat")
maxi = 0

for i in range(len(adatok)):
    if "Barcelona" in adatok[i].hazai:
        maxi = i
print(f"\tBareloniai csapat neve: {adatok[maxi].hazai}")
#6. feladat
print("6. feladat")
for i in range(len(adatok)):
    if adatok[i].időpont[0] == "2004" and adatok[i].időpont[1] == "11" and adatok[i].időpont[2] == "21":
        print(f"\t{adatok[i].hazai}-{adatok[i].idegen} ({adatok[i].hazai_pont}:{adatok[i].idegen_pont})")
#7. feladat
print("7. feladat")
helyek = set()
for i in range(len(adatok)):
    helyek.add(adatok[i].helyszín)
for i in helyek:
    szor = 0
    for j in range(len(adatok)):
        if adatok[j].helyszín == i:
            szor += 1
    if szor > 20:
        print(f"\t{i}: {szor}")