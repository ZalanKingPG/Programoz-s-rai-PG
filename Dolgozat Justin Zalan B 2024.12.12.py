file = open("be1.txt", "r", encoding="utf-8")
sorok = file.readlines()
file.close()
nums = []
for i in range(len(sorok)):
    nums.append(int(sorok[i]))
print(nums)

#1. Hány 30-nál nagyobb szám van a sorozatban?
db = 0
for i in range(len(nums)):
    if nums[i] > 30:
        db += 1
print(f"A sorozatban {db}db 30-nál nagyobb szám van")
#2. Írjuk ki az utolsó 9-cel vagy 15-tel osztható szám indexét!
for i in reversed(range(len(nums))):
    if nums[i] % 9 == 0 or nums[i] % 15 == 0:
        print(f"Az utolsó 9-cel vagy 15-el osztható szám az a {nums[i]}")
        break
#3. Mennyi a sorozatban található számok szorzatának a fele?
szorzat = 1
for i in range(len(nums)):
    szorzat *= nums[i]
print(f"A sorozatban található számok szorzatának a fele {szorzat / 2}")
#4. Melyik a legnagyobb szám a -10-nél kisebbek közül?
legkisebb = 10000000
for i in range(len(nums)):
    if nums[i] < -10 and nums[i] < legkisebb:
        legkisebb = nums[i]
print(f"A sorozatban található -10-nél kisebb található legkiebb szám {legkisebb}")
#5. Készíts egy "ki.txt" állományt, amelyben a sorozat páros tagjainak a kétszerese szerepeljen!
paros = open("ki1.txt", "w", encoding="utf-8")
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        print(nums[i] * 2, file=paros)