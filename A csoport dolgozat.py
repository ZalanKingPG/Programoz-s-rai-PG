#Egy robot csomagokat pakol, amelyek egy futószalagon érkeznek, a beérkező csomagokat tömeg alapján kell osztályoznia!
# Írj programot, amely billentyűzetről beolvassa az érkező csomagok tömegét (legfeljebb 50 db-ot), a felhasználó az adatbevitel
# végét a -1 beírásával jelezheti. A program írja ki, hogy a követező kategóriákból hány darab csomagot pakolt a gép:
# - könnyű : 10 kg-nál kisebb
# - közepes: 10 kg-nál nagyobb, de 50 kg-nál kisebb
# - nehéz: 50 kg-nál nagyobb
#A program írja ki azt is, hogy összesen hány kilogrammot pakolt át a robot, és hogy milyen nehéz volt a legkönnyebb csomag
konnyu = 0
kozepes = 0
nehez = 0
atlag = 0

for i in range(50):
    r_szam = int(input("Beérkező csomag súlya: "))
    atlag += r_szam
    if r_szam < 0:
        break
    else:
        if r_szam > 0 and r_szam < 10:
            konnyu += 1
        if r_szam < 50 and r_szam > 10:
            kozepes += 1
        else:
            nehez += 1

print(f"Könnyű csomagok száma: {konnyu}")
print(f"Közepes nehézségű csomagok száma: {kozepes}")
print(f"Nehéz csomagok száma: {nehez}")
print(f"A csomagok átlag nehézsége: {atlag // i}")
