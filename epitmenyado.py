f = open("epitmenyado.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()
elsosor = sorok.pop(0)
darabok = elsosor.strip().split()
adoA = int(darabok[0])
adoB = int(darabok[1])
adoC = int(darabok[2])


class Main:
    def __init__(self, adosz, utca, hsz, sav, terulet):
        self.adosz = adosz
        self.utca = utca
        self.hsz = hsz
        self.sav = sav
        self.terulet = int(terulet)


adatok = []
for i in range(len(sorok)):
    darabok = sorok[i].strip().split()
    a = Main(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4])
    adatok.append(a)

#2. feladat
print(f"2. feladat: {len(adatok)} db telek adatai találhatóak az állományban")
#3. feladat
be = input("Írjon be egy adószámot: ")
volt = False
for i in range(len(adatok)):
    if adatok[i].adosz == be:
        print(f"3. feladat: {adatok[i].utca} utca {adatok[i].hsz}")
        volt = True
if volt == False:
    print("Nem szerepel az adatállományban")
#4. feladat
def ado(sav, terulet):
    if sav == "A":
        fizetendo = adoA * terulet
    if sav == "B":
        fizetendo = adoB * terulet
    if sav == "C":
        fizetendo = adoC * terulet
    if fizetendo < 10000:
        return 0
    else:
        return fizetendo
#5. feladat
dbA = 0
dbB = 0
dbC = 0
osszadoA = 0
osszadoB = 0
osszadoC = 0
for i in range(len(adatok)):
    if adatok[i].sav == "A":
        dbA += 1
        osszadoA += ado(adatok[i].sav, adatok[i].terulet)
    if adatok[i].sav == "B":
        dbB += 1
        osszadoA += ado(adatok[i].sav, adatok[i].terulet)
    if adatok[i].sav == "C":
        dbC += 1
        osszadoA += ado(adatok[i].sav, adatok[i].terulet)
