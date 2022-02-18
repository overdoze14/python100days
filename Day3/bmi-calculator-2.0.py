# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

"""
It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.

https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36
"""

bmi = weight / (height * height)

if bmi <= 18.5:
    result = "are underweight"
elif bmi <= 25: 
    result = "have a normal weight"
elif bmi <= 30: 
    result = "are slightly overweight"
elif bmi <= 35: 
    result = "are obese"
else: 
    result = "are clinically obese"

bmi = "{:.2f}".format(bmi)

print(f"Your BMI is {bmi}, you {result}.")