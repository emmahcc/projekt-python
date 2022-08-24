
import random

print('Jag(programmet) tänker på ett nummer mellan 1 till 10, gissa vilket det är!')
num = random.randint(1, 10)
user_num= None
number_guesses = 1

while user_num != num:
    try:
        user_num = int(input('Gissa på ett nummer:'))
    except (ValueError):
        print("Det var inte ett nummer!")
        user_num = int(input('Gissa på ett nummer:'))
    if user_num == num:
        print('RÄTT! Bra gissat. Du klarade det på '+ str(number_guesses) + ' försök.')
        number_guesses = number_guesses +1
        break
    elif user_num < num:
        print(str(user_num) + ' är för lågt, gissa igen')
        number_guesses = number_guesses +1
    elif user_num > num:
        print(str(user_num) + ' är för högt, gissa igen')
    number_guesses = number_guesses +1
