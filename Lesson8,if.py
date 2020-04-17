#logical operators

# ==, >=, <=, !=

# not == not = , as = is for assignment

#define variable and write if function

num1 = 100
num2 = 150

if num1>num2:
    print("num1 is bigger than num2")
elif num2>num1:
    print("num1 is bigger than num2")
else:
    print("both numbers are equal")

#logic gate operators

x = 10
y = 20

if not (x > y):
    print("if not worked")

if (x>10 and y>15):
    print("if and worked")

if (x>10 or y>15):
    print("if or worked")

# can reverse any function with a not