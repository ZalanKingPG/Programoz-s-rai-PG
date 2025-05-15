file = open("gödrök.txt", "r", encoding="utf-8")
sorok = file.readlines()
file.close()

class Main:
    def __init__(self, melyseg):
        self.melyseg = int(melyseg)

adatok = []
for i in range(len(sorok)):
    darabok = sorok[i].strip()
    a = Main(darabok[0])
    adatok.append(a)


#1. feladat
print("1. feladat")
print(f"A fájl adatainak száma: {len(adatok)}")
#2. feladat
print("2. feladat")
be = int(input("Adjon meg egy távolságértéket! "))
for i in range(len(adatok)):
    if i + 1 == be:
        print(f"\tEzen a helyen a felszín {adatok[i].melyseg} méter mélyen van.")
#3. feladatű
talaj = 0
for i in range(len(adatok)):
    if adatok[i].melyseg == 0:
        talaj += 1
print(f"Az érintetlen terület aránya {talaj / len(adatok) * 100:.2f}%")
#4. feladat
f = open("godrok.txt", "w", encoding="utf-8")
gsz = 0
print("4. feladat")
for i in range(len(adatok) - 1):
    if adatok[i].melyseg != 0:
        print(f"{adatok[i].melyseg} ", file=f, end="")
    if adatok[i].melyseg != 0 and adatok[i + 1].melyseg == 0:
        print("", file=f)
        gsz += 1
f.close()
#5. feladat
print("5. feladat")
print(f"A gödrök száma: {gsz}")
#6. fealdat A
print("6. feladat\na)")
if adatok[be - 1].melyseg == 0:
    print("Az adott helyen nincs gödör.")
else:
    i = be
    while adatok[i].melyseg != 0 and i >= 0:
        i -= 1
    eleje = i + 1
    i = be
    while adatok[i].melyseg != 0 and i < len(adatok):
        i += 1
    vege = i - 1
    print(f"A gödör eleje: {eleje + 1}, a gödör vége: {vege + 1}")
    print("b)")
    maxmelyseg = 0
    maxhely = 0
    for i in range(eleje, vege + 1):
        if adatok[i].melyseg > maxmelyseg:
            maxmelyseg = adatok[i].melyseg
            maxhely = i
    melyul = True
    for i in range(eleje, maxhely):
        if adatok[i].melyseg > adatok[i + 1].melyseg:
            melyul = False
    for i in range(maxhely, vege):
        if adatok[i].melyseg < adatok[i + 1].melyseg:
            melyul = False
    if melyul:
        print("A gödör folyamatosan mélyül")
    else:
        print("A gödör nem folyamatosan mélyül.")
    print(f"c)\nA legmélyebb pont {maxmelyseg} méter")
    #D
    terfogat = 0
    for i in range(eleje, vege + 1):
        terfogat += adatok[i].melyseg * 10
    print(f"d)\nA gödör térfogata {terfogat} m^3.")