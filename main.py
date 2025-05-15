# Téglalap kiszámítása K, T

a_oldal = int(input("Téglalap (a) oldala: "))
b_oldal = int(input("Téglalap (b) oldala: "))
terulet = a_oldal * b_oldal
kerulet = 2 * (a_oldal + b_oldal)
print(f"(a)oldal = {a_oldal}, (b)oldal = {b_oldal}")
print(f"A terület {terulet}  cm2")
print(f"A kerület {kerulet}  cm")

#Kör kiszámítása K, T

sugar = int(input("Írja be a kör sugarát: "))
pi = 3.14
k_terulet = sugar * sugar * pi
k_kerulet = 2 * sugar * pi
print(f"A kör sugara {sugar}")
print(f"A kör kerülete {k_kerulet} cm")
print(f"A kör területe {k_terulet} cm2")