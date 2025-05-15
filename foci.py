file = open("foci.txt", "r", encoding="utf-8")
sorok = file.readlines()
file.close()

class game:
    def __init__(self, merkozes, hazai_gol, vendeg_gol, elso_f, masodik_f, hazai_csapat, vendeg_csapat):
        self.merkozes = int(merkozes)
        self.hazai_gol = int(hazai_gol)
        self.vendeg_gol = int(vendeg_gol)
        self.elso_f = int(elso_f)
        self.masodik_f = int(masodik_f)
        self.hazai_csapat = hazai_csapat
        self.vendeg_csapat = vendeg_csapat

adatok = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(" ")
    a = game(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6])
    adatok.append(a)

#2. Feladat
beford = int(input("Írja be egy fordulónak a számát: "))
for i in range(len(adatok)):
    if adatok[i].merkozes == beford:
        print(f"{adatok[i].hazai_csapat}-{adatok[i].vendeg_csapat}: {adatok[i].hazai_gol}-{adatok[i].vendeg_gol} ({adatok[i].elso_f}-{adatok[i].masodik_f})")

#3. Feladat
for i in range(len(adatok)):
    if adatok[i].elso_f > adatok[i].masodik_f and adatok[i].elso_f < adatok[i].masodik_f:
        print(f"{adatok[i].merkozes} {adatok[i].hazai_csapat}")

    if adatok[i].elso_f < adatok[i].masodik_f and adatok[i].elso_f > adatok[i].masodik_f:
        print(f"{adatok[i].merkozes} {adatok[i].vendeg_csapat}")

#4. Feladat
csapat = input("Írja be egy csapat nevét: ")
lott = 0
kapott = 0

#5. Feladat
for i in range(len(adatok)):
    if adatok[i].hazai_csapat == csapat:
        lott += adatok[i].hazai_gol
        kapott += adatok[i].vendeg_gol
    if adatok[i].vendeg_csapat == csapat:
        lott += adatok[i].vendeg_gol
        kapott += adatok[i].hazai_gol
print(f"Lőtt: {lott}")
print(f"Kapott: {kapott}")

#6. Feladat
van = False
for i in range(len(adatok)):
    if adatok[i].hazai_csapat == csapat and adatok[i].hazai_gol < adatok[i].vendeg_gol:
        print(f"A csapat először a {adatok[i].vendeg_csapat}-től kapott ki")
        van = True
        break
if van == False:
    print("A csapat otthon veretlen maradt")

#7. Feladat
eredmeny = set()
for i in range(len(adatok)):

print(eredmeny)