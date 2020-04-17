# Arithmetic operations
# BODMAS applies, can override with brackets
# five main operators:  + - * / **

x=8+2
y=100*2
z=100 * (2 + 2)

#power symbol **
p=10**2

#modulo / remainder / like modular arithemtic in Maths
q=10%3

# can represent complex numbers as well using j, need to specify 1
r = 1j
s=(-1)**(0.5)

#####################

# import the random library, this is included in python
import random

# set the starting health
Health = 50
print(Health)

# create difficulty, set to easy (1), or higher value for higher difficulty as the denominator
Diff = 3

# generate the health potion value (include difficulty as denominator), specify integer
# this uses the random integer function over a defined range 25->50

potion_health = int(random.randint(25,50) / Diff)
print(potion_health)

# add the health potion to the original health
Health = Health+potion_health
print(Health)

# EXTRA not part of lesson
# rounding

x = round(2.2)

# this makes the type of the number an integer

# floor division, round down to nearest integer

b = 9//2

# operands

a = 1
b = 2
print(a==b)
# will be false

print(a>b)
# will be false

print(b<a)
# will be true

# also >=, <=, <>,

#logical
