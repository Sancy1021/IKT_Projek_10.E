import time
import random
szam = int(input('Hany dobast kersz'))

for i in range(szam):
    x = random.randint(1,6)
    print(x)
    time.sleep(1)
    if x == 1:
        print (1)
    elif x == 2:
        print (2)
    elif x == 3:
        print (3)
    elif x == 4:
        print (4) 
    elif x == 5:
        print (5)
    else: 
        print (6)
