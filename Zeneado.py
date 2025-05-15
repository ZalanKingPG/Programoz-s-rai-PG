f = open("zeneado.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class zene:
    def __init__(self, ado, p, mp, eloado, cim):
        self.ado = int(ado)
        self.p = int(p)
        self.mp = int(mp)
        self.eloado = eloado
        self.cim = cim

adatok = []
for i in range(1, len(sorok)):
    darab = sorok[i].strip().split()
    cimek = " ".join(darab[3:])  # Összefűzzük a maradék részt
    z = zene(darab[0], darab[1], darab[2], darab[3], cimek)  # Javított objektum létrehozás
    adatok.append(z)

# 2. feladat: Adók és számaik
csatornak = set()
for i in range(len(adatok)):
    csatornak.add(adatok[i].ado)

for i in csatornak:
    adok = sum(1 for j in adatok if j.ado == i)
    print(f"Az {i}-es adóból {adok} db van.")

# 3. feladat: Eric Clapton első és utolsó szereplése
elso = -1
utolso = -1
for i in range(len(adatok)):
    if adatok[i].ado == 1 and adatok[i].eloado == "Eric Clapton":
        elso = i
        break

for j in reversed(range(len(adatok))):
    if adatok[j].ado == 1 and adatok[j].eloado == "Eric Clapton":
        utolso = j
        break

if elso != -1 and utolso != -1:  # Csak akkor számoljunk, ha mindkettőt megtaláltuk
    eltelt = 0
    for i in range(elso, utolso + 1):
        if adatok[i].ado == 1:
            eltelt += adatok[i].p * 60 + adatok[i].mp

    ora = eltelt // 3600
    eltelt %= 3600
    perc = eltelt // 60
    mp = eltelt % 60
    print(f"A két szám között {ora}:{perc}:{mp} telt el.")
else:
    print("Eric Clapton nincs az 1-es adón.")

# 4. feladat: Omega - Legenda előtti másik két szám keresése
hanyadik = -1
melyik = -1

for i in range(len(adatok)):
    if adatok[i].eloado == "Omega" and adatok[i].cim == "Legenda":
        melyik = adatok[i].ado
        hanyadik = i
        break

if hanyadik != -1:
    masik = -1
    for i in range(hanyadik - 1, -1, -1):
        if adatok[i].ado != melyik:
            print(f"{adatok[i].eloado} - {adatok[i].cim}")
            masik = adatok[i].ado
            break

    for i in range(hanyadik - 1, -1, -1):
        if adatok[i].ado != melyik and adatok[i].ado != masik:
            print(f"{adatok[i].eloado} - {adatok[i].cim}")
            break
else:
    print("Az Omega - Legenda nem található az adatokban.")

keres = input("Írja be a kérés szövegér: ")
f = open("keres.txt", "w", encoding="utf-8")
for i in range(len(adatok)):
    eloadodb = adatok[i].eloado.split()
    cimdb = adatok[i].cim.split()
    egybe = ""
    for j in range(len(eloadodb)):
        egybe += eloadodb[j].lower()
    for j in range(len(cimdb)):
        egybe += cimdb[j].lower()

    if egybe.find(keres) != -1:
        print(f"{adatok[i].eloado} - {adatok[i].cim}", file=f)
f.close()

osszido = 180
egeszora = 3600
for i in range(len(adatok)):
    if adatok[i].ado == 1:
        if osszido + adatok[i].p * 60 + adatok[i].mp + 60 < egeszora:
            osszido += (adatok[i].p * 60 + adatok[i].mp + 60)
        else:
            osszido = egeszora + 180 + (adatok[i].p * 60 + adatok[i].mp + 60)
            egeszora += 3600
ora = osszido // 3600
osszido = osszido % 3600
perc = osszido // 60
mp = osszido % 60
print(f"Az adás vége {ora}:{perc}:{mp}")