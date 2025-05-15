#olvassunk be egy számot
#print hog a szám páros vagypáratlan

"""
number = int(input("Kérek egy számot: "))

if number > 0:
    print("Páros")
elif number == 0:
    print(f"A beírt szám a {number}")
else:
    print("Páratlan")
"""

#olvassunk be 2 számot és irja ki a két szám közül a legynagyobbat
"""
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek még egy számot: "))

if szam1 > szam2:
    print(szam1)
elif szam2 > szam1:
    print(szam2)
else:
    print("A két szám egyenlő")
"""

"""
#Háromszög szerkeszthető-e
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a + b > c and a + c > b and b + c > a:
    print("Szerkeszthető háromszög")
else:
    print("Nem szerkeszthető háromszög")
"""

#Olvassuk be egy évszámot és dontsük el hogy szökőév-e

"""
date = int(input("Kérek egy évszámot: "))
if date % 4 == 0 and date % 100 != 0:
    print(f"{date} szökőév")
elif date % 400 == 0:
    print(f"{date} szökőév")
else:
    print(f"{date} nem szökőév")
 """

#Olvass be egy órát és az időpont alapján köszönjön a program
#6 - 10: reggelt
#11 - 17 napot
#18 - 22 estét
#23 - 5 éjszakát

"""
time = int(input("Hány óra van: "))

if time >= 6 and time <= 10:
    print("Reggelt")
elif time >= 11 and time <= 17:
    print("jó napot")
elif time >= 18 and time <= 22:
    print("estét")
else:
    print("éjszakát")
"""


#Input dolgozat száma calculate the grade (50 pont)
#40% 2 - 20p
#50% 3 - 25p
#60% 4 - 30p
#80% 5 - 40p

print("Összpönt 50")
grade = int(input("Hány pontot értél el: "))
gradepercentage = (grade / 50) * 100

if grade < 20 and grade > 0:
    print(f"{gradepercentage}% elégtelen")
elif grade <= 25 and grade > 20:
    print(f"{gradepercentage}% elégséges")
elif grade <= 30 and grade > 25:
    print(f"{gradepercentage}% közepes")
elif grade <= 40 and grade > 30:
    print(f"{gradepercentage}% jó")
else:
    print(f"{gradepercentage}% jeles")

