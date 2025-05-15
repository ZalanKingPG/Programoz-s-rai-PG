#dolgozat

print("A szobát Méterben számoljuk")
szoba_1 = int(input("A burkolni való szoba szélessége: "))
szoba_2 = int(input("A burkolni való szoba hosszúsága: "))

szoba_terulet = szoba_1 * szoba_2
print(f"A szoba {szoba_terulet}m2")

csempe_terulet = 20 * 20 / 10  #átváltottuk méterbe
csempe = int(input("Mennyi csempét vettél: "))
csempe_lefedettseg = csempe * csempe_terulet
print(f"A csempe területe {csempe_lefedettseg}m2")
csempe_need = (szoba_terulet - csempe_lefedettseg) / csempe_terulet
csempe_forsafe1 = csempe / 100 * 10
csempe_forsafe2 = csempe_need / 100 * 10

if szoba_terulet > csempe_lefedettseg:
    print("A szoba nem burkolható")
    print(f"A szoba {szoba_terulet / csempe_terulet}db csempépvel burkolható, szükség van még {csempe_need}db plusz {csempe_forsafe2} csempére a bisztonság kedvééret")
else:
    print(f"A szoba megoldható {csempe}db csempével plusz {csempe_forsafe1}db csempe az illesztések kedvéért")