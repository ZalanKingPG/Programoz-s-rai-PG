#generáljunk 500db 1 és 10000 közötti számot
#hány páros és hány páratlan szám van köztük
#mennyi az 5-tel oszthatő számok átlaga
#melyik a legkisebb sorolt szám
"""
import random
paros = 0
paratlan = 0
legkisebb = 0
ot = 0
otszam = 0
min = 10001

for i in range(500):
    random_szam = random.randint(1, 10000)
    if random_szam % 2 == 0:
        paros += 1

    else:
        paratlan += 1

    if random_szam % 5 == 0:
        otszam += random_szam
        ot += 1

    if random_szam < min:
        min = random_szam

print(f"Páros: {paros}")
print(f"Páratlan: {paratlan}")
print(f"Az 5-el osztható számok átlaga {otszam / ot}")
print(f"A legkisebb szám: {min}")
"""

#python feladatsor

#1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
#legkisebb értéket ezek közül!

szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy számot: "))
szam3 = int(input("Kérek egy számot: "))

if szam1 < szam2 and szam1 < szam3:
    print(f"A legkisebb szám: {szam1}")
elif szam2 < szam1 and szam2 < szam3:
    print(f"A legkisebb szám: {szam2}")
else:
    print(f"A legkisebb szám: {szam3}")

#2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy
#három különböző értéket kapott-e!

szam4 = int(input("Kérek egy számot: "))
szam5 = int(input("Kérek egy számot: "))
szam6 = int(input("Kérek egy számot: "))

if szam4 == szam6 and szam4 == szam5:
    print("A beírt számok egyeznek!")
elif szam5 == szam4 and szam5 == szam6:
    print("A beírt számok egyeznek!")
elif szam6 == szam4 and szam6 == szam5:
    print("A beírt számok egyeznek!")
else:
    print("A beírt számok nem egyeznek!")

#3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
#érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

