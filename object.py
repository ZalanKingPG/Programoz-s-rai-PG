#osztály létrehozása
class Auto:
    #Konstruktor (az objektum inicializálására szolgál)
    def __init__(self, marka, modell, evjarat):
        self.marka = marka
        self.modell = modell
        self.evjarat = evjarat

    #Metódus az autó leírásához
    def leiras(self):
        return f"{self.evjarat} {self.marka} {self.modell}"

    #Metódus az autó indításához
    def inditas(self):
        return f"A(z) {self.marka} {self.modell} motorja elindult!"

#Objektumok létrehozása az osztály alapján
auto1 = Auto("Toyota", "Corolla", "2020")
auto2 = Auto("Ford", "Focus", "2018")

#Attribútumok elérése
print(auto1.marka)
print(auto2.evjarat)

#Metódusok meghívása
print(auto1.leiras())
print(auto2.inditas())



class Zalan:
    def __init__(self, vezeteknev, keresztnev, honap, szulev, nap, eletkor,):
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.honap = honap
        self.szulev = szulev
        self.eletkor = eletkor
        self.nap = nap

    def __str__(self):
        return (f"Név: {self.vezeteknev} {self.keresztnev} Születési dátum: {self.szulev} {self.honap} {self.nap}"
                f"Kor: {self.eletkor}")


szulev = int(input("Add meg a születési évedet: "))
honap = int(input("Add meg a születési hónapodat(számmal): "))
nap = int(input("Add meg hanyadikán születtél: "))
eletkor = int(input("Add meg az életkorodat: "))
vezeteknev = input("Add meg a vezetéknevedet: ")
keresztnev = input("Add meg a keresztnevedet: ")

felhasznalo = Zalan(vezeteknev, keresztnev, szulev, honap, nap, eletkor)


print("\nLétrehozott felhasználó adatai:")
print(Zalan)