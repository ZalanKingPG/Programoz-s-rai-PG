file = open("Berek2020", "r", encoding="utf-8")
sorok = file.readlines()
file.close()

class Main:
    def __init__(self, name, sex, reszleg, belepes, ber):
        self.name = name
        self.sex = sex
        self.reszleg = reszleg
        self.belepes = int(belepes)
        self.ber = int(ber)

adatok = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    a = Main(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4])
    adatok.append(a)

#3 Feladat
#Határozza meg és írja ki a képernyőre' hogy hrány dolgoző ad,atai találhatók a forrásállománybanl
dolg_szama = 0
for i in range(len(adatok)):
    dolg_szama += 1
print(f"3. feladat: Dolgozók száma: {dolg_szama} fő")

#4. Feladat
#Hatátozza meg és.írja ki a képernyőrc a 2O2O-as átlagbéreket! Az eredményl ezer forintban, egy tizedesjegyekre kerekítve jelenítse meg
ossz = 0
for i in range(len(adatok)):
    ossz += adatok[i].ber
atlag = round(ossz / len(adatok) / 1000, 1)
print(f"4. feladat: Bérek átlaga: {atlag} eFt")

#5. Feladat
#Kérje be egy részlegnevét a felhasználótól a minta szerint!
bereszleg = input("5. feladat: Kérem egy részleg nevét: ")
#6. Feladat
#Az e!őző feladatban megadott részlegen keresse meg és írja ki a legnagyobb bérrel (fizetéssel) rendelkező dolgozó adatait!
# Ha a megadott résileg n"* tet.iik a cégnél' akkor a ,l megadott részleg nem létezik a cégnél!,, feliratot jelenítse Á"gí Feltételezheti, hogy nem
# alakult ki ,,holtvelseny'' egy-egy részlegen doigozók fizetése
#között!
max = 0
maxi = 0
for i in range(len(adatok)):
    if adatok[i].ber > max and adatok[i].reszleg == bereszleg.lower():
        max = adatok[i].ber
        maxi = i

if max == 0:
    print("6. feladat: Nincs ilyen nevű részleg")
else:
    print("6. feladat: A legtöbbet kereső dolgozó a részlegen:")
    print(f"\tNév: {adatok[maxi].name}")
    print(f"\tNeme: {adatok[maxi].sex}")
    print(f"\tBelepés: {adatok[maxi].belepes}")
    print(f"\tBér: {adatok[maxi].ber}")

#7. Feladat Készítsen statisáikát az egyes részlegeken dolgozók számérő|l A részlegek kiírásanak
#sorrendje tetszőleges!
reszleg = set()
for i in range(len(adatok)):
    reszleg.add(adatok[i].reszleg)

print("7. feladat: Statisztika")
for r in reszleg:
    db = 0
    for i in range(len(adatok)):
        if adatok[i].reszleg == r:
            db += 1
    print(f"\t{r}: {db} fő")

file = open("asztalos.txt", "w", encoding="utf-8")
for i in range(len(adatok)):
    if adatok[i].reszleg == "asztalosműhely":
        print(f"{adatok[i].name}", file=file)
file.close()