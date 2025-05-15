import random
#B csoport
print("B csoport")
#Egy listába generálj 60 darab -90 és 70 közé eső számot!
nums = []
for i in range(60):
    nums.append(random.randint(-90, 70))
#A lista tartalmát írasd ki!
print(nums)
#Válaszolj az alábbi kérdésekre (minden feladat előtt írasd ki a feladat sorszámát):
#1. Írasd ki az első 6-tal vagy 7-tel osztható számot!
print("1. Feladat")
for i in range(len(nums)):
    if nums[i] % 6 == 0 and nums[i] % 7 == 0:
        print(f"A listában szereplő első 6-al vagy 7-el sztható szám: {nums[i]}")
        break
#2. Van-e számok között olyan, amely 0-nál kisebb, de -10-nél nagyobb?
print("2. Feladat")
van = False
for i in range(len(nums)):
    if nums[i] < 0 and nums[i] > -10:
        van = True
        break
if van == True:
    print("A listában van olyan szám ami kisebb mint 0 de nagyobb mint -10")
#3. Hány darab -70-nél kisebb szám van a sorozatban?
print("3. Feladat")
db = 0
for i in range(len(nums)):
    if nums[i] < -70:
        db += 1
print(f"A listában {db}db -70-nél kisebb szám van")
#4. Mi a legkisebb páratlan szám indexe?
min_index = -1
min_num = len(nums) + 1
for i in range(len(nums)):
    if nums[i] % 2 == 1 and nums[i] < min_num:
        min_num = nums[i]
        min_index = i
if min_index != -1:
    print(f"A legkisebb páratlan szám indexe: {min_index} ami a: {min_num}")
else:
    print("A listában nincs páratlan szám")
#5. Hány olyan szám van, amely kisebb az előtte és az utána álló számnál is?
db = 0
for i in range(1, len(nums) - 1):
    if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
        db += 1
print(f"A listában {db}db olyan szám van amely kisebb az előtte és utána lévő számnál")