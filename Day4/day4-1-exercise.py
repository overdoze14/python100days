#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

coin_side = random.randint(0, 1)

if coin_side == 0:
    print("Tails")
else:
    print("Heads ")