
import random

print('Jag(programmet) tänker på ett nummer mellan 1 till 10, gissa vilket det är!')
num = random.randint(1, 10)
user_num= None

while user_num != num:
    user_num = int(input('Gissa på ett nummer:'))
    
    if user_num == num:
        print('RÄTT! Bra gissat')
        break
    
    elif user_num < num:
        print(str(user_num) + ' är för lågt, gissa igen')
    
    elif user_num > num:
        print(str(user_num) + ' är för högt, gissa igen')
  
