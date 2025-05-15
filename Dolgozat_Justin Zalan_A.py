import random
#A csoport
print("A csoport")
#Egy listába generálj 40 darab -25 és 60 közé eső számot!
nums = []
for i in range(40):
    nums.append(random.randint(-25, 60))
#A lista tartalmát írasd ki!
print(nums)
#Válaszolj az alábbi kérdésekre (minden feladat előtt írasd ki a feladat sorszámát):
#1. Írasd ki az utolsó 7-tel és 5-tel osztható szám indexét!
print("1. Feladat")
for i in reversed(range(len(nums))):
    if nums[i] % 7 == 0 and nums[i] % 5 == 0:
        print(f"Az utolsó 5-el és 7-el osztható szám indexe: {i}")
        break
#2. Van-e számok között olyan, amely 12 és 18 közé esik?
van = False
print("2. Feladat")
for i in range(len(nums)):
    if nums[i] < 18 and nums[i] > 12:
        van = True
        break
if van == True:
    print("A listában van olyan szám ami 12 és 18 közés esik")
else:
    print("A listában nincs olyan szám ami 12 és 18 közé esik")
#3. Hány darab 3-mal osztható szám van a sorozatban?
print("3. Feladat")
db = 0
for i in range(len(nums)):
    if nums[i] % 3 == 0:
        db += 1
print(f"A listában {db}db 3-al osztható szám van")
#4. Melyik a legnagyobb páros szám?
max_p = []
for i in range(len(nums)):
    if nums[i] > 0 and nums[i] % 2 == 0:
        max_p.append(nums[i])
print(f"A listában szereplő legnagyobb páros szám: {max(max_p)}")
#5. Van-e olyan szám, amely osztója az előtte és az utána lévő számnak is?
van = False
for i in range(1, len(nums) - 1):
    if nums[i] != 0:
        if nums[i - 1] % nums[i] == 0 and nums[i + 1] % nums[i] == 0:
            van = True
if van == True:
    print("A listában van olyan szám amely osztója az előtte és utána lévő számnak")
else:
    print("A listában nincs olyan szám amely osztója az előtte és utána lévő számnak")
