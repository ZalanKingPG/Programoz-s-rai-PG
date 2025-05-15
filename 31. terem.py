#szimuláljuk egy honapban esett csapadékmennyiséget
#0 - 20 mm közötti eső lehet egy nap
#osztályozzuk a napokat
# 0 mm : csapadékmentes
# 0 - 5 mm : gyenge eső
# 6 - 10 mm : eső
# 11 - 20 mm : vihar
#irjuk ki az atlagos csapadékmennyiséget
"""
import random

atlag = 0
mentes = 0
gyenge = 0
esos = 0
vihar = 0

for i in range(1,30 + 1):
    csapadek = random.randint(0, 20)
    atlag +=csapadek
    if csapadek == 0:
        print(f"{i}: {csapadek} mm ,csapadékmentes")
        mentes += 1
    elif csapadek > 0 and csapadek < 5:
        print(f"{i}: {csapadek} mm, gyenge eső")
        gyenge += 1
    elif csapadek > 5 and csapadek < 11:
        print(f"{i}: {csapadek} mm ,eső")
        esos += 1
    else:
        print(f"{i}: {csapadek} mm, vihar")
        vihar += 1
print(f"Az e havi átlag csapadémennyiség {atlag / 30} mm")
print(f"Csapadékmentes: {mentes}")
print(f"Gyenge eső: {gyenge}")
print(f"Esős: {esos}")
print(f"Viharos: {vihar}")
"""

"""
import random
szamok = []
for i in range(50):
    szamok.append(random.randint(1, 100))

#van e a számok között 5-el osztható

i = 0
while i < len(szamok) and szamok[i] % 5 != 0:
    i += 1
if i < len(szamok):
    print("Van benn 5-el osztható")
else:
    print("Nincs benne 5-el osztható")




van = False
for i in range(len(szamok)):
    if szamok[i] % 5 == 0:
        van = True
        break

if van == True:
    print("Van 5-el osztható szám")
else:
    print("Nincs 5-el osztható szám")
"""

