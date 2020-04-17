# input function

#ask user for name
#ask user for age
#ask user for city
#ask user for what they enjoy

#create output text

#print output test

name = input('what is your name?:')
print(name)

age = input('what is your age?:')
print(age)

what is your age: 4

# input is always string
# use + to concatenate

city = input('where do you live ')
print('I live in '+city)

# operations - concatenate, note must be same datatype

A = "beans"
B = "toast"
C = str(3)
D = 2
E = 3

#conacetante text
print(A+B+C)

#arithemtic
print (D+E)
print(D/E)
print(D**E)

#add variables

name = 'Jamie'
age = 43

string =' My name is {} and I am {}'.format(name,age)
print(string)