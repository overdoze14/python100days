#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pass_letter = ''
pass_symbol = ''
pass_number = ''

len_letters = len(letters)
len_symbols = len(symbols)
len_numbers = len(numbers)

for i in range(1, nr_letters+1):
    pass_letter += letters[random.randint(0,len_letters-1)]

for i in range(1, nr_symbols+1):
    pass_symbol += symbols[random.randint(0,len_symbols-1)]

for i in range(1, nr_numbers+1):
    pass_number += numbers[random.randint(0,len_numbers-1)]

password = pass_letter + pass_symbol + pass_number

print(f"Easy level password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters_count = nr_letters
numbers_count = nr_numbers
symbols_count = nr_symbols

password2 =''

for i in range(1, nr_letters + nr_numbers + nr_symbols + 1):
    if letters_count != 0 and numbers_count != 0 and symbols_count != 0:
        lns = random.randint(1,3)
    elif letters_count == 0 and numbers_count == 0:
        lns = 3
    elif letters_count == 0 and symbols_count == 0:
        lns = 2
    elif symbols_count == 0 and numbers_count == 0:
        lns = 1
    elif letters_count == 0:
        lns = random.randint(2,3)
    elif numbers_count == 0:
        lns = random.randrange(1,4,2)
    elif symbols_count == 0:
        lns = random.randint(1,2)
    
    if lns == 1:
        password2 += letters[random.randint(0,len_letters-1)]
        letters_count -= 1
    elif lns == 2:
        password2 += numbers[random.randint(0,len_numbers-1)]
        numbers_count -= 1
    else:
        password2 += symbols[random.randint(0,len_symbols-1)]
        symbols_count -= 1

print(f"Hard level password: {password2}")