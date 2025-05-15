file = open("hegyekMo.txt", "r", encoding="utf-8")
sorok = file.readlines()
file.close()

class hegy:
    def __init__(self, hegycs, hegyseg, magassag):
        self.hegycs = hegycs
        self.hegyseg = hegyseg
        self.magassag = int(magassag)

hegyek = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    h = hegy(darabok[0], darabok[1], darabok[2])
    hegyek.append(h)
print(f"3. feladat: Hegycsúcsok száma: {len(hegyek)}db")
osszeg = 0
for i in range(len(hegyek)):
    osszeg += hegyek[i].magassag
print(f"4. feladat: A hegycsúcsok átlagos magassága: {osszeg / len(hegyek)}")
legm = 0
maxi = 0
for i in range(len(hegyek)):
    if hegyek[i].magassag > legm:
        legm = hegyek[i].magassag
        maxi = i
print(f"5. feladat: A legmagasabb hegycsúcs adatai: \n\tNév: {hegyek[maxi].hegycs} \n\tHegység: {hegyek[maxi].hegyseg} \n\tMagasság: {hegyek[maxi].magassag}")
bemagas = int(input("6. feladat: Kérek egy magasságot: "))
van = False
for i in range(len(hegyek)):
    if hegyek[i].hegyseg == "Börzsöny" and hegyek[i].magassag > bemagas:
        van = True
if van == True:
    print(f"\tVan {bemagas}m-nél magasabb hegycsúcs a Börzsönyben!")
else:
    print(f"\tNincs {bemagas}m-nél magasabb hegycsúcs a Börzsönyben!")
db = 0
for i in range(len(hegyek)):
    labm = hegyek[i].magassag * 3.280839895
    if labm > 3000:
        db += 1
print(f"7. feladat: A 3000 lábnál magasabb hegycsúcsok száma {db}db")
hegysegek = set()
for i in range(len(hegyek)):
    hegysegek.add(hegyek[i].hegyseg)
