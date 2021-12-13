import time
import os
os.system('cls')
def gyertya (x):
    if (x==1):
        print(r"""  

           ___)__          
          | Béke |                    
          |      |
          |      |
          |      |
          '------'      

 """,)

    if (x==2):
        print(r"""  

           ___)__     ___)__     
          | Béke |   | Hit  |             
          |      |   |      |
          |      |   |      |
          |      |   |      |
          '------'   '------'   

 """,)

    if  (x==3):
         print(r"""  

           ___)__     ___)__      ___)__  
          | Béke |   | Hit  |    |Szeret|         
          |      |   |      |    |   -et|
          |      |   |      |    |      |
          |      |   |      |    |      |
          '------'   '------'    '------' 

 """,)

    elif  (x==4):
            print(r"""  

           ___)__     ___)__      ___)__      ___)__  
          | Béke |   | Hit  |    |Szeret|    |Remény|   
          |      |   |      |    |   -et|    |      |
          |      |   |      |    |      |    |      |
          |      |   |      |    |      |    |      |
          '------'   '------'    '------'    '------' 

 """,)
    else:
        print ("Maximum 5 gyertya van" )

Nap = input(' December Hanyadika van? ')
Nap = int(Nap)
Kari = 24-Nap
print(f"{Kari} Nap van még karacsonyig? ")
input(' Űss egy entert! ')
if (Kari<6):
    for x in range(4):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
elif (5<Kari<13):
      for x in range(3):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
elif (12<Kari<20):
      for x in range(2):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
else:
    
    os.system('cls')
    gyertya(1)
    time.sleep(1)

