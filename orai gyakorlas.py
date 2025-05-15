import random

szamok = []
for i in range(40):
    szamok.append(random.randint(-50,80))
print(szamok)

print("1. Feladat")
atlag = 0
for i in range(len(szamok)):
    atlag += szamok[i]
print(f"A listában szereplő számok átlaga {atlag / len(szamok)}")


print("2. Feladat")
hely = 0
for i in reversed(range(len(szamok))):
    if szamok[i] % 9 == 0 and szamok[i] % 5 == 0:
        print(f"Az utolső 9-el és 5-el osztható szám indexe: {i}")
        break


print("3. Feladat")
szam = 0
for i in range(len(szamok)):
    if szamok[i] % 2 == 0 or szamok[i] % 7 == 0:
        szam = szamok[i]
        break
print(f"Az első 2-vel vagy 7-el osztahtő szám az a: {szam}")


print("4. Feladat")
van = True
for i in range(len(szamok)):
    if szamok[i] % 2 != 0 :
        van = False
        break
if van == False:
    print("A listában nem minden szám páros.")
else:
    print("A listában minden szám páros.")


print("5. Feladat")
van = False
for i in range(len(szamok)):
    if szamok[i] > 70:
        van = True
        break
if van == True:
    print("A listában van olyan szám amely nagyobb mint 70.")
else:
    print("A listába nincs olyan szám amely nagyob mint 70.")


print("6. Feladat")
db = 0
for i in range(len(szamok)):
    if szamok[i] < 2:
        db += 1
print(f"A listában {db}db negatív szám található")


print("7. Feladat")
legnagyobb = []
for i in range(len(szamok)):
    if szamok[i] % 4 == 0:
        legnagyobb.append(szamok[i])
print(f"A sorozatban a legnagyobb 4-el osztható szám az a: {max(legnagyobb)}")


print("8. Feladat")
darab = 0
for i in range(1, len(szamok) - 1):
    if szamok[i] > szamok[i - 1] and szamok[i] > szamok[i + 1]:
        darab += 1
print(f"{darab} lokáslis csúcs van a listában")

print("9. Feladat")
hossz = 0
for i in range(len(szamok)):
    if szamok[i] == szamok[i + 1]:
        hossz += 1
    else:
        hossz = 1
print(f"A listában van egy {hossz} hosszú egyforma számokbó álló combo")

print("10 Feladat")
van = True
for i in range(len(szamok)):
    if szamok[i] > szamok[i - 1]:
        van = False
        break
if van == False:
    print("A lista nem szigorúan monoton csökkenő")
else:
    print("A lista szigorúan monoton csökkenő")

print("11. Feladat")
poz = []
neg = []
for i in range(len(szamok)):
    if szamok[i] > 0:
        poz.append(szamok[i])
    else:
        neg.append(szamok[i])
print(poz)
print(neg)