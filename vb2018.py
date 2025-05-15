f = open("vb2018.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class VB:
    def __init__(self,varos, nev1, nev2, ferohely):
        self.varos = varos
        self.nev1 = nev1
        self.nev2 = nev2
        self.ferohely = int(ferohely)

vb = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    a = VB(darabok[0], darabok[1], darabok[2], darabok[3])
    vb.append(a)

#3. feladat
print("3. feladat")
print(f"\tA mérkőzéseket {len(vb)} különböző stadionban játszották.")
#4. feladat
print("4. feladat")
legk = 100000000
ii = 0
for i in range(len(vb)):
    if vb[i].ferohely < legk:
        legk = vb[i].ferohely
        ii = i
print(f"\tA legkevesebb férőhellyel rendelkező stadion adatai: {vb[ii].varos} {vb[ii].nev1} {vb[ii].nev2} {vb[ii].ferohely}")
#5. feladat
print("5. feladat")
atlag = 0
for i in range(len(vb)):
    atlag += vb[i].ferohely
print(f"\tA stadionok férőhellyének átlaga: {round(atlag / len(vb), 1)}")
#6. feladat
print("6. feladat")
db = 0
for i in range(len(vb)):
    if vb[i].nev2 != "n.a.":
        db += 1
print(f"\t{db} darab stadionnak van lternatív neve")
#7. feladat
print("7. feladat")
