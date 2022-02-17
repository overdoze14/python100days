# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

if age > 90:
    print("You are dead, sorry) This programm can calculate left time for people younger then 90")
    exit()
years = 90 - age
months = int( years * 12 )
weeks = years * 52
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left")