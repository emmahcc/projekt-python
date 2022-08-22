
import random
import string

#lowercase = bool(input('Tillåt små bokstäver (j/n)?'))
#uppercase = (input('Tillåt stora bokstäver (j/n))'))
#numbers = str(input('Tillåt siffror?'))
#Spec_char = str(input('Tillåt specialtecken?'))

char_low = list(string.ascii_lowercase)
char_up = list(string.ascii_uppercase)
dig = list(string.digits)
spec = list(string.punctuation)
print('Generera ditt lösenord här')
password = []
user_length = int(input('Lösenordets längd:'))
lowercase = input('Tillåt små bokstäver (ja/nej)?')
uppercase = input('Tillåt stora bokstäver (ja/nej))')
numbers = input('Tillåt siffror? (ja/nej)')
spec_char = input('Tillåt specialtecken? (ja/nej)')
alla  = []

if lowercase == 'ja':
    alla += char_low
if uppercase =='ja':
    alla += char_up
if numbers == 'ja':
    alla += dig
if spec_char == 'ja':
    alla += spec
        
for i in range(user_length):

    random.shuffle(alla)
    password.append(random.choice(alla))
    
print(''.join(password))
