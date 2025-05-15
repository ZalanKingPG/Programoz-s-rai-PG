#Egy különleges kamrában extrém hőmérsékletek hatását tesztelik. -200 és 3000 fok közötti  értékeket képes a kamra előállítani.
# Szimuláljuk véletlen számokkal a kamra hőmérsékletét, összesen 150 mérési eredményt állítsunk elő. Számoljuk meg, hogy a
# következő kategóriákba eső értékek hányszor fordultak elő a mérés során:
#- extrém hideg : -50 alatt
#- elviselhető: -50 és 80 fok között
#- extrém meleg: 80 fok felett
#A program írja még ki, hogy mennyi volt a mért átlaghőmérséklet, és hogy mennyi volt a legmagasabb mért érték!
import random

extrem_hideg = 0
elviselheto = 0
extrem_meleg = 0
highest = 0
atlag = 0

for i in range(150):
    random_szam = random.randint(-200, 3000)
    atlag += random_szam
    if random_szam < -50:
        extrem_hideg += 1
    if random_szam > -50 and random_szam <= 80:
        elviselheto += 1
    else:
        extrem_meleg += 1
    if random_szam > highest:
        highest = random_szam
print(f"Extrém hideg: {extrem_hideg}")
print(f"Elviselhető: {elviselheto}")
print(f"Extrém meleg: {extrem_meleg}")
print(f"A legmagasabb mért hőmérséklet: {highest} ceslius")
print(f"A mért átlaghőmérséklet: {highest // i}")
