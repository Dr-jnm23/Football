# we introduced strings in lesson 1, now we will manipulate them
# casting

# used to change variable type, so we can force datatype to be integer, float or string

x = str(2)
type(x)

# can also print WITHOUT changing type

y = 3
print(str(y))
type(y)

# broken strings
# below is invalid syntax
# can fix THREE ways

#method 1 = mixed quotes
z = 'Jamie's''

# method 2 use triple quote
z = '''Jamie's'''
z1 = "Jamie's"

# method 3 escape character
z = 'Jamie\'s'

# string concatenation (must all be string variable)
test_concat = 'hello' + ' world'

# lower case
#z.lower()

# upper case
#z.upper()

# title case
#z.title()