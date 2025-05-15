#1. feladat
f = open("vizibicikli.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()


#2. feladat
#3. feladat
class Kolcsonzes:
    def __init__(self, Nev, JAzon, EOra, EPerc, VOra, Vperc):
        self.Nev = Nev
        self.JAzon = JAzon
        self.EOra = EOra
        self.EPerc = EPerc
        self.VOra = VOra
        self.Vperc = Vperc
        self.Emp = EOra * 3600 + EPerc * 60
        self.Vmp = VOra * 3600 + Vperc * 60


#4. feladat
adatok = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    a = Kolcsonzes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    adatok.append(a)

#5. feladat
print(f"5. feladat: Napi kölcsönzések száma: {len(adatok)}")
#6. feladat
nev = input("6. feladat: Kérek egy nevet: ")
print(f"\t{nev} kölcsönzései")
for i in range(len(adatok)):
    if adatok[i].Nev == nev:
        print(f"\t{adatok[i].EOra}:{adatok[i].EPerc}-{adatok[i].VOra}:{adatok[i].Vperc}")
#7. feladat
be = input("7. feladat: Adjon meg egy időpontot óra:perc alakban: ")
for i in range(len(adatok)):
    if adatok[i].Emp
#8. feladat