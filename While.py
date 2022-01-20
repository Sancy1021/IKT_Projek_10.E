user = ["Alex", "Martin", "Sanyi", "Réka"]
list_size = len(user)  
chk = [False] * list_size 
print(f'\nAdd meg a {list_size} megfelelő nevet!\n')
while True: 
    name = input("Név? ")
    if not name in user: print('--- Nem megfelelő név! ÚJRA! ---')  
    continue 
    for i in range(list_size):  
        if name == user[i]:    
            print("...ok")
            chk[i] = True 
        if all(chk):
            print('\n---- Belépés engedélyezve: ----\nSziasztok',', '.join(user),'!','\n-------------------------------\n')    
            break