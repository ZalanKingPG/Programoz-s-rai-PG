"""
fruit = ["alma", "körte", "barack", "szilva"]
print(fruit)

fruit.append("szőlő") #hozzáfűzés lista végére

print(fruit[0]) #a lista első eleme
print(fruit[1]) #a lista második eleme
print(fruit[-1]) #a lista utolsó eleme
print(fruit[1:4]) #a lista 2.-3.-4. eleme eleme

fruit.append(5)
fruit.append(15)
print(fruit)
"""

"""
#töltsünk fel egy 50 elemű listát 1 és 100 közötti számokkal
import random

paros = 0
paratlan = 0
r_lista = []
for i in range(50):
    r_lista.append(random.randint(1, 100))
print(r_lista)
#hány db páros szám van közöttük

for c in range(len(r_lista)):
    if r_lista[c] % 2 == 0:
        paros += 1
print(paros)
"""

import random
nums = []

for i in range(50):
    nums.append(random.randint(-60, 100))
print(nums)

print("1. Feladat")
szorzat = 1
for i in range(len(nums)):
    szorzat *= nums[i]
print(f"A számok szorzata {szorzat}")



print("2. Feladat")
for i in reversed(range(len(nums))):
    if nums[i] % 5 == 0 or nums[i] % 7 == 0:
        print(f"Az utolsó 5-tel vagy 7-tel osztható szám indexe: {i}")
        break



print("3. Feladat")
for i in range(len(nums)):
    if nums[i] % 3 == 0 and nums[i] % 7 == 0:
        print(f"Az első 3-al és 7-el osztható szám indexe: {i}")
        break



print("4. Feladat")
van = False
for i in range(len(nums)):
    if nums[i] > 0:
        van = True
        break
if van == True:
    print("A listában nem minden szám negatív")
else:
    print("A listában minden szám negatív")



print("5. Feladat")
vane = False
for i in range(len(nums)):
    if nums[i] > 1 and nums[i] < 10:
        vane = True
        break
if vane == True:
    print(f"A listában van szám ami 1 és 10 közé esik: {nums[i]}")
else:
    print("A listában nincs olyan szám ami 1 és 10 közé esik")



print("6. Feladat")
tizennyolc = 0
for i in range(len(nums)):
    if nums[i] % 18 == 0:
        tizennyolc += 1
print(f"A listában {tizennyolc}db 18-al osztható szám van")



print("7. Feladat")
hely = 0
legkisebb = nums[i]
for i in range(len(nums)):
    if nums[i] < legkisebb:
        legkisebb = nums[i]
        hely = i
print(f"A legkisebb szám az {hely}. helyen áll  :{legkisebb}")



print("8. Feladat")
number = 1
for i in range(len(nums)):
    if nums[i] % 17 == 0 or nums[i] % 18 == 0:
        print(f"{nums[i]} négyzete: {nums[i] * nums[i]}")



print("9. Feladat")
szomszed = False
for i in range(1, len(nums) - 1):
    if nums[i] < 0 and nums[i - 1] > 0 and nums[i + 1] > 0:
        szomszed = True
        break
if szomszed == True:
    print("A listában van olyan negatív szám aminek mind két szomszédja pozitív")
else:
    print("A listában nincs olyan negatív szám aminek mind két szomszédja pozitív")


print("10. Feladat")
novekvo = True
for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        novekvo = False
        break
if novekvo == False:
    print("A lista nem szigorúan növekvő")
else:
    print("A lista szigorúan monoton növekvő")


print("11. Feladat")
paros = []
paratlan = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        paros.append(nums[i])
    else:
        paratlan.append(nums[i])
print(f"Páratlan elemű lista: {paratlan}")
print(f"Páros elemű lista: {paros}")