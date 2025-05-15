file = open("gyakorlas txt", "r", encoding="utf-8")
sorok = file.readlines()
file.close()
nums = []
for i in range(len(sorok)):
    nums.append(int(sorok[i]))

# 1. van e a sotozatban 100-al osztható szám
van = False
for i in range(len(nums)):
    if nums[i] % 100 == 0:
        van = True
        break
if van == True:
    print("A sorozatban van 100-al osztható szám")

# 2. Írjuk ki az utolsó 7-tel osztható szám indexét!
for i in reversed(range(len(nums))):
    if nums[i] % 7 == 0:
        print(f"Az utolsó 7-el oszthtó szám {i}")
        break

#3. Írjuk ki az első 19-cel osztható szám indexét!
for i in range(len(nums)):
    if nums[i] % 19 == 0:
        print(f"Az első 19-el osztható szám indexe {i}")
        break

#4. Mennyi a sorozatban található számok átlagának a négyzete?
osszeg = 0
db = 0
for i in range(len(nums)):
    osszeg += nums[i]
    db += 1
atlag = osszeg / db
print(f"A sorozatban található számok átlagának a négyzete {atlag * atlag}")

#5. Igaz-e, hogy minden szám nagyobb, mint 10?
van = True
for i in range(len(nums)):
    if nums[i] < 10:
        van = False
        break
if van == False:
    print("A számsorban nem minden 10-nél nagyobb")
else:
    print("A számsorban minden szám 10-nél nagyobb")

#6. Hány 9-cel osztható szám található a sorozatban?
db = 0
for i in range(len(nums)):
    if nums[i] % 9 == 0:
        db += 1
print(f"A számsorban {db}db 9-el osztható szám van ")

#7. Írjuk ki a sorozatban található 15-tel osztható számok felét!
db = 0
for i in range(len(nums)):
    if nums[i] % 15 == 0:
        db += nums[i]
print(f"A számsorban található 15-el osztható számok összegének a fele {db / 2}")

#8. Hány eleme van a sorozatnak?
db = 0
for i in range(len(nums)):
    db += 1
print(f"A sorozat {db} elemű")

#9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?
van = False
for i in range(len(nums) - 1):
    if nums[i] < 0 and nums[i + 1] > 0:
        van = True
if van == True:
    print("A sorozatban van olyan negatív szám amelyet pozitív szám követ")

#10. Mennyi a sorozatban található legkisebb szám fele?
legkisebb = nums[0]
for i in range(len(nums)):
    if nums[i] < legkisebb:
        legkisebb = nums[i]

print(f"A sorozatban található legisebb szám fele: {legkisebb / 2}")

#11. Válogassuk szét két szövegfájlba a pozitív és a negatív számokat!
pozitiv = open("pozitív", "w", encoding="utf-8")
negativ = open("negatív", "w", encoding="utf-8")

for i in range(len(nums)):
    if nums[i] < 0:
        print(nums[i], file=negativ)
    else:
        print(nums[i], file=pozitiv)