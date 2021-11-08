from random import random
import time
import random
for i in range(3):
    lap1 = random.randint(1,11)
    print(lap1)
    time.sleep(1)
    if lap1 == 1:
        print(1)
        valasz = input('kérsz még?[i/n]')
