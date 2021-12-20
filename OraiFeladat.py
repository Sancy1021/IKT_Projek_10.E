#1.feladat
print(" Jó napom van? ")
napom = input(" Milyen napod van? ")

if napom == "igen":
    print(" Jó napom van! ")
elif napom == "nem":
    print(" Rosz namop van! ")
else:
    print(" Sajnálom nem értem a válaszodat! ")

#2.feladat






#3.feladat
from random import randrange

Radnomszam = randrange (1,5)

print(" Adj meg egy számot! ")

Szam = int(input())

if Szam == Radnomszam:
    print(" A két szám egyezik! ")
elif Szam > Radnomszam:
    print(" A szám nagyobb mint  a random szám! ")
else:
    print(" A szám kisebb mint a random szám! ")




