"""
file = open("be.txt", "r", encoding="utf-8")

a = int(file.readline())
b = int(file.readline())

file.close()

osszeg = a + b

f = open("ki.txt", "w", encoding="utf-8")
print(osszeg, file=f)

f.close()
"""


#páros és páratlan számok

nums = open("szamok", "r", encoding="utf-8")
sor = nums.readline()
nums.close()

darabok = sor.split()
szamok = []
for i in range(len(darabok)):
    szamok.append(int(darabok[i]))

paros = open("paros", "w", encoding="utf-8")
paratlan = open("paratlan", "w", encoding="utf-8")

for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        print(szamok[i], file=paros)
    else:
        print(szamok[i], file=paratlan)
paros.close()
paratlan.close()
