f = open("jaror.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class Main:
    def __init__(self, o, p, mp, rsz):
        self.o = int(o)
        self.p = int(p)
        self.mp = int(mp)
        self.rsz = rsz


adatok = []
for i in range(len(sorok)):
    darabok = sorok[i].strip().split(" ")
    a = Main(darabok[0], darabok[1], darabok[2], darabok[3])
    adatok.append(a)

print(f"Az ellenőrtést végzők legalább {adatok[-1].o - adatok[0].o + 1} órát dolgoztak")

for i in range(len(adatok)):
    if adatok[i].o != adatok[i - 1].o:
        print(f"{adatok[i].o} óra: {adatok[i].rsz}")

motor = 0
busz = 0
kamion = 0
szgk = 0
for i in range(len(adatok)):
    if adatok[i].rsz[0] == "B":
        busz += 1
    elif adatok[i].rsz[0] == "M":
        motor += 1
    elif adatok[i].rsz[0] == "K":
        kamion += 1
    else:
        szgk += 1
print(f"Busz: {busz}\nMotor: {motor}\nKamion: {kamion}\nSzemélyi gépjármű: {szgk}")

maxido = 0
eleje = 0
vege = 0
for i in range(len(adatok) - 1):
    ido1 = adatok[i].o * 3600 + adatok[i].p * 60 + adatok[i].mp
    ido2 = adatok[i + 1].o * 3600 + adatok[i + 1].p * 60 + adatok[i + 1].mp

    eltelt = ido2 - ido1
    if eltelt > maxido:
        maxido = eltelt
        eleje = i
        vege = i + 1
print(f"A leghosszabb forgalommentes időszak: {adatok[eleje].o}:{adatok[eleje].p}:{adatok[eleje].mp} - {adatok[vege].o}:{adatok[vege].p}:{adatok[vege].mp}")

keresett = input("Írjon be egy rendszámot: ")
