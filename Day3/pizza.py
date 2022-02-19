print("Welcome to Pyzza Deliveries!")
size = input("What size pizza do you want? S, M, L ")
add_peperony = input("Do you want pepperoni? Y, N ")
extra_cheese = input("Do you want extra cheese? Y, N ")

#Small pizza: $15
#Medium pizza: $20
#Large pizza: $25
#Pepperony for small pizza: +$2
#Pepperony for medium or large pizza: +$3
#Extra cheese for any size pizza: +$1

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_peperony == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"You final bill is: ${bill}")