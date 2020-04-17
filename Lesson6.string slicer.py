WORD = 'ALUMINIUM FOIL'

#IMMUTABLE STRING
# SYNTAX IS [START: END : SKIP]

# 1st to 3rd, interval one
WORD[0:4:1]

# 1st to 3rd, interval one, shorthand
WORD[0:4]

# 1st to 4th, alternate
WORD[0:5:2]

# last to 3rd from last
WORD[-1:-4:]

# 8th to 5th
WORD [9:5:-1]

# shorthand = 5th onwards
WORD [4:]

# shorthand = 1st four
WORD [:4]



