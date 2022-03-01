print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")


t += name2.count("t")
r += name2.count("r")
u += name2.count("u")
e += name2.count("e")

x = t + r + u + e

l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")

l += name2.count("l")
o += name2.count("o")
v += name2.count("v")
e += name2.count("e")

y = l + o + v + e

print(f"Your score is {x}{y} %")