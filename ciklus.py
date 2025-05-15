"""
szam1 = int(input("Egy szám: "))

for i in range(1, szam1 + 1):
    if szam1 % i == 0:
        print(i)
"""

"""
#olvassunk be egy számot és írjuk ki hogy prím szám-e
szam2 = int(input("Irj be egy számot: "))
db = 0

for i in range(1, szam2 + 1,):
    if szam2 % i == 0:
      db = db + 1

if db == 2:
    print("Prímszám")
else:
    print("Nem prímszám")
"""

"""
#olvassuk be 10 számot írjuk ki az szorzatukat
osszeg = 1
for i in range(10):
    szam = int(input("Kérek egy számot: "))
    osszeg = osszeg * szam
print(osszeg)
"""

"""
#olvassunk be egy számotés irjuk ki a faktoriálisát
fakt = 1
szam = int(input("Kérek egy számot: "))
for i in range(1, szam + 1, 1):
    fakt = fakt * i
print(fakt)
"""

"""
#olvassuk be az n értékét írjuk ki az eső n db négyzetszámot
natural = 1
szam = int(input("Kérek egy számot: "))
for i in range(1, szam + 1, 1):
    print(i * i)
 """

"""
import time

time_set = int(input("Írd be az időt másodpercben: "))

for i in range(time_set, 1, -1):
    masodperc = i % 60
    perc = (i / 60) % 60
    ora = (i / 3600)
    print(f"{ora:02}:{perc:02}:{masodperc:02}")
    time.sleep(1)
"""

#kérjük be egy hét hőmérsékleteit, minden nampra irjuk ki hogy fagyott-e
#írjuk ki az átlagot is

osszeg = 0
week = 7
for i in range(week):
    temp = int(input("Írd be a heti hőnérsékleteket: "))
    osszeg += temp
    if temp < 0:
        print("A héten fagyott")
    else:
        print("Nem fagyott")
atlag = osszeg / 7
print(f"Atátlag hőmérséklet {atlag} fok")