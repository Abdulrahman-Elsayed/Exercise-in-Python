"""Simulation: The Tortoise and the Hare"""

import random

print('BANG !!!!!')
print("AND THEY'RE OFF !!!!!")
print('')

tortoise_pos = 1
hare_pos = 1


while (tortoise_pos < 70 and hare_pos < 70):
    rand_num = random.randrange(1, 11)

    if rand_num in [1, 2]:
        tortoise_pos += 3
        hare_pos += 0
    elif rand_num in [3, 4]:
        tortoise_pos += 3
        hare_pos += 9 
    elif rand_num in [5]:
        tortoise_pos += 3
        hare_pos -= 12
    elif rand_num in [6, 7, 8]:
        tortoise_pos += 1
        hare_pos += 1
    elif rand_num in [9, 10]:
        tortoise_pos -= 6
        hare_pos -= 2  

    if tortoise_pos < 1:
        tortoise_pos = 1

    if hare_pos < 1:
        hare_pos = 1    

    if tortoise_pos == hare_pos:
        for i in range (1, tortoise_pos):
            print(' ', end='')  
        print('OUCH!!!')
    elif tortoise_pos > hare_pos:
        for i in range (1, hare_pos):
            print(' ', end='')  
        print('H', end = '')
        for i in range (1, tortoise_pos - hare_pos):
            print(' ', end='')  
        print('T')
    else:
        for i in range (1, tortoise_pos):
            print(' ', end='')  
        print('T', end = '')
        for i in range (1, hare_pos - tortoise_pos):
            print(' ', end='')  
        print('H')


print('')        
if tortoise_pos >= 70:
    print('TORTOISE WINS!!! YAY!!!')
else:
    print('Hare wins. Yuch.')
