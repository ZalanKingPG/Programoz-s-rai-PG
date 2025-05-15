class ember:
    def __init__(self, name, date, sex, height):
        self.name = name
        self.date = date
        self.sex = sex
        self.height = int(height)
zalan = ember("Justin Zalán", 2007, "male", 167)
print(zalan.name)
print(zalan.date)


adatok = input("Írja be egy ember adatait ;-vel elválasztva: ")
darabok = adatok.split(";")

e = ember(darabok[0], darabok[1], darabok[2], darabok[3])
print(e.name)

if zalan.height > e.height:
    print("Zalán a magasabb")
else:
    print(f"{e.name} magasabb")