file = open("szavazatok", "r", encoding="utf-8")
sorok = file.readlines()
file.close()

# a körzet száma, ahol a jelölt indult; a jelölt által kapott szavazatok száma, a jelölt vezetékneve, a jelölt utóneve, a jelölt pártja
class info:
    def __init__(self, korzet, szsz, veznev, kernev, part):
        self.korzet = int(korzet)
        self.szsz = int(szsz)
        self. veznev = veznev
        self.kernev = kernev
        self.part = part

adatok = []
for i in range(len(sorok)):
    darabok = sorok[i].strip().split(" ")
    a = info(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4])
    adatok.append(a)

#1. Feladat
# Írasd ki, hogy hány jelölt indult a választáson.
print(f"1. feladat: A választáson {len(adatok)} jelölt indul")

#2. Feladat
#Számold és írasd ki, hogy hány jelöltet indított a "HEP" nevű párt.
db = 0
for i in range(len(adatok)):
    if adatok[i].part == "HEP":
        db += 1
print(f"2. feladat: A választáson {db} jelöltet indított a HEP párt")

#3. Feladat
#Állapítsd meg, és írasd ki, hogy az 7-es körzetben ki kapta a legkevesebb szavazatot.
legn = 1000
maxi = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 7 and adatok[i].szsz < legn:
        maxi = i
        legn = adatok[i].szsz
print(f"3. feladat: A 7-es körzetben {adatok[maxi].veznev} {adatok[maxi].kernev} a legkevesebb szavazatot")

#4. Feladat
#Összesítsd körzetenként a szavazatok számát, tehát melyik körzetben hányan szavaztak.
print("4. Feladat")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 1:
        max_szav += adatok[i].szsz
print(f"\tAz 1-es körzetben {max_szav} szavazat volt")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 2:
        max_szav += adatok[i].szsz
print(f"\tA 2-es körzetben {max_szav} szavazat volt")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 3:
        max_szav += adatok[i].szsz
print(f"\tA 3-as körzetben {max_szav} szavazat volt")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 4:
        max_szav += adatok[i].szsz
print(f"\tA 4-es körzetben {max_szav} szavazat volt")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 5:
        max_szav += adatok[i].szsz
print(f"\tAz 5-ös körzetben {max_szav} szavazat volt")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 6:
        max_szav += adatok[i].szsz
print(f"\tA 6-os körzetben {max_szav} szavazat volt")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 7:
        max_szav += adatok[i].szsz
print(f"\tA 7-es körzetben {max_szav} szavazat volt")
max_szav = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 8:
        max_szav += adatok[i].szsz
print(f"\tA 8-as körzetben {max_szav} szavazat volt")

#5. Feladat
#Készíts egy korzet01.txt nevű állományt, amely az 1-es körzet végeredményét tartalmazza. A fájlban soronként a
#jelölt teljes neve és az általa kapott szavazatok száma szerepeljen.
maxi = 0
legn = 0
for i in range(len(adatok)):
    if adatok[i].korzet == 1 and adatok[i].szsz > legn:
        maxi = i
        legn = adatok[i].szsz
file = open("korzet01.txt", "w", encoding="utf-8")
print(f"Az 1-es körzet végeredménye: \n\tA nyertes jelölt neve: {adatok[maxi].veznev} {adatok[maxi].kernev}\nAz általa kapott szavazatok száma: \n\t{adatok[maxi].szsz}", file = file)