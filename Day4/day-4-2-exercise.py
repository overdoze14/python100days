# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

max =  len(names) - 1

random_num = random.randint(0, max)

print(f"{names[random_num]} is going to buy the meal today!")