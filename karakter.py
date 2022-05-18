class karakter:
    def __init__(self, név, pont, email):
        self.név= név
        self.pont= pont
        self.email= email
lista=[]

for _ in range(3):
    név = input('Add meg a játékos nevét! ')
    pont = input('Add meg a karakterek pontszámát! ')
    email = input('Add meg az email címet! ')
    lista.append(karakter(név,pont,email))

leggyengép_karakter = lista[0]

for karakter in lista:
    print(karakter.név,karakter.pont,karakter.email)
    if karakter.pont < lista.pont:
        leggyengép_karakter = karakter
    print(leggyengép_karakter.név)

with open ('torlendo.txt','w' ,encoding='utf-8') as file:
    file.write(leggyengép_karakter.email)
