sor = open("szigetek.txt", "r", encoding="utf-8")

"""
flight_data = []
i = 0
while i < 1000:
    flight_data.append(int(sor.readline()))
    i += 1
print(flight_data)
"""
sorok = sor.readlines()
sor.close()

flight_data = []
for i in range(len(sorok)):
    flight_data.append(int(sorok[i].strip()))
print(flight_data)