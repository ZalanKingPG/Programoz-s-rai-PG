#a játékos gondol egy számra 1-1000 között

print("Írj be egy számot 1 és 1000 között: ")
e = 1
u = 1000
k = (e + u) // 2

for i in range(1000):
    valasz = input(f"A szám a(z) {k}?(i/n) ")
    if valasz == "i":
        print(f"A számod a(z) {valasz}")
        break
    else:
        valasz = input(f"A szám nagyobb mint a(z) {k}?(i/n) ")
        if valasz == "i":
            e = k + 1
        else:
            u = k - 1
        k = (e + u) // 2