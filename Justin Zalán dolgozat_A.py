f = open("Schumacher.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class formula:
    def __init__(self, date, grandprix, position, laps, points, team, status):
        self.date = date
        self.grandprix = grandprix
        self.position = int(position)
        self.laps = int(laps)
        self.points = int(points)
        self.team = team
        self.status = status

verseny = []
for i in range(1, len(sorok)):
    darabok1 = sorok[i].strip().split("-")

    darabok = sorok[i].strip().split(";")
    a = formula(darabok[0].split("-"), darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6])
    verseny.append(a)

#1. feladat
print("1. feladat")
print(f"\tAz állományban {len(verseny)}db adat található")
#2. feladat
print("2. feladat")
ossz = 0
db = 0
for i in range(len(verseny)):
    ossz += verseny[i].points
    db += 1
print(f"\tMichael Schumacher átlagosan {ossz / db:.3} pontot szerzett pályafutása során")
#3. feladat
print("3. feladat")
legj = 100000
for i in range(len(verseny)):
    if verseny[i].team == "Mercedes" and verseny[i].position < legj and verseny[i].position > 0:
        legj = verseny[i].position
print(f"\tA Mercedes színeiben Michael Schumacher legjobb helyezése {legj}. volt")
#4. feladat
print("4. feladat")
csapatok = set()
for i in range(len(verseny)):
    csapatok.add(verseny[i].team)

for i in csapatok:
    ossz = 0
    for j in range(len(verseny)):
        if verseny[j].team == i:
            ossz += verseny[j].points
    print(f"\t{i}: {ossz}")
#bonusz
print("BÓNUSZ")
db = 0
for i in range(len(verseny)):
    if int(verseny[i].date[0]) < 2000 and int(verseny[i].date[0]) > 1989 and verseny[i].status == "Finished":
        db += 1
print(f"\tMicheal Schumacher a 90-es éveben {db} alkalommal ért célba")