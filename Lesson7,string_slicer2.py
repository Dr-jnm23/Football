# how to find the index for a word in string

email= 'jamienmartin@gmail.com'

# find index for a specific word - gives numeric result
email.index('gmail.com')

# slice to find username before @
username = email[0:email.index('@')]

# slice to find domain after @
domain = email[email.index('@')+1:]

# use input
email2 = input('what is your email address? ').strip()

# display name and domain
message = 'My username is {} and my domain is {}'.format(username,domain)
print(message)