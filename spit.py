#input 3 adat
# megtenni kívánt km
# uzemanyag tank merete
# az auto fogyasztasa
# hany kilometert tehet meg az auto
# kell e tankolni az ut alatt

"""
distance = int(input("Megtenni kívánt Km: "))
gastank = int(input("Üzemanyag tank mérete: "))
fogyasztas = int(input("Fogyasztás(Liter / 100Km): "))


megteheto_kilometer = gastank / fogyasztas * 100

print(f"Megtehető kilóméterek: {megteheto_kilometer}")

if distance < megteheto_kilometer:
    print("Nem kell tankolni az út alatt")
else:
    print("Az út nem tehető meg tankolás nélkül")
"""

#olvasssuk be a szoba szélességét és hosszát
#hány doboz parketta van
#1 doboz hány négyzetméterre elég
#hány doboz kell az egészhez
#venni kell-e még és mennyit



sz_szelesseg = int(input("A szoba szélessége: "))
sz_magassag = int(input("A szoba hossza: "))
doboz1 = int(input("Mennyi dobozunk van: "))
doboz2 = int(input("1 doboz parketta hány m2 re elég: "))

szoba_m2 = sz_magassag * sz_szelesseg
osszdoboz = doboz1 * doboz2
dobozneed = (szoba_m2 - osszdoboz) / doboz2

print(f"A szoba {szoba_m2} négyzetméteres")
print(f"{osszdoboz} négyzetnéter padlózható")

if szoba_m2 > osszdoboz:
    print(f"A szoba nem parkettázható {doboz1} mennyiségű dobozzal")
    print(f"Kell még {dobozneed} mennyiségű doboz")
else:
    print("A szoba parkettázható")