
#olvassunk be neveket és magasságokat
#legfeljebb 100-at
#a végát a 0 jelezze
#írjuk ki a legmagasabb illető magasságát és nevét

"""
maxname = ""
max = 0

for i in range(100):
    name = input("Név: ")
    height = int(input("magassága(cm): "))
    if height == 0:
        break
    else:
        if height > max:
            max = height
            maxname = name
print(f"A legmagasabb illető {name} aki {height}cm")
"""

#szimulaljunk 300 dobokockadobast
#irjuk ki hogy melyiket hanyzor obtuk

"""
import random

db1 = 0
db2 = 0
db3 = 0
db4 = 0
db5 = 0
db6 = 0

for i in range(300):
    dobas = random.randint(1, 6)
    if dobas == 1:
        db1 += 1
    elif dobas == 2:
        db2 += 1
    elif dobas == 3:
        db3 += 1
    elif dobas == 4:
        db4 += 1
    elif dobas == 5:
        db5 += 1
    else:
        db6 += 1
print(f"1: {db1}×")
print(f"2: {db2}×")
print(f"3: {db3}×")
print(f"4: {db4}×")
print(f"5: {db5}×")
print(f"6: {db6}×")
"""

#dobjunk fel 200szor penzermet
#irjuk ki az eredenyeket
#hányszor fej hányszor iras
#mennyi volt a leghosszabb fej streak
import random

fej = 0
iras = 0
streak = 0
maxstreak = 0

for i in range(200):
    dobas = random.randint(1, 2)
    if dobas == 1:
        fej += 1
        streak += 1
    elif dobas == 2:
        iras += 1
        if streak > maxstreak:
            maxstreak = streak
        streak = 0
print(f"Fej {fej}× esett, Írás {iras}× esett")
print(f"{maxstreak}× kaptunk egymás után fejet")

#program, mely kiírja az n-nél nem nagyobb páratlan számok összegét
"""
n = int(input("Kérek egy számot: "))
osszeg = 0

for i in range(1 ,n):
    if i % 2 == 1:
        osszeg += i

print(osszeg)
"""

#fibanacci elemek számolása

n = int(input("Kérek egy számot: "))
elozoelotti = 0
elozo = 1
print(elozoelotti)
print(elozo)

for i in range(n - 2):
    jelenlegi = elozo + elozoelotti
    print(jelenlegi)
    elozoelotti = elozo
    elozo = jelenlegi

