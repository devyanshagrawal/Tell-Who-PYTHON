import random

names = "Devyansh, Manisha, Mehar, Alok, Neha"

name_l = names.split(", ")

random_n = random.choice(name_l)

print(random_n + " is going to buy a milk.")