# indexing and searching 26th Feb

#search for word, value error if not found
# 0 is first position
x = 'happy birthday'
x.index('birthday')
x.index('hello')

# search for word, no value error
x.find('hello')
x.find('happy')
x.find(' ')

# search - outputs first result for multiples
y = 'happy happy'
y.index('happy')

#strip
z = '000hello000'
z.strip('0')

#can use lstrip, rstrip
# strip will remove spaces
#can use strip together with input

# string length
len(x)

# replace text

replace_test = 'Green'
print(replace_test.replace('G','B'))

#split text

split_test = 'Hello, world'
print(split_test.split(','))

