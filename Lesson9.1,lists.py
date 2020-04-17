# Python data structures, April 1st 2020
# grouping data and storing under one variable name
# list

# lists use [] and are mutable
our_list = [27, 46, -5, 17, 99]
print(our_list)

# how many elements in the list
print(len(our_list))

# indexing list - note the first term is 0, second term is 1, last term is -1 (as seen boefore in string slicer)

# second term would be
our_list[1]

# slicing a list

# slice to include first term
our_list[0:1:1]

# or shorthand form
our_list[0:1]

# list within a list

our_list = [1, 2, [3, 4, 5], 6, 7, 8]
our_list[2]
our_list[2][0]

# create table: list of lists - 2 dimensional

our_table = [[1,2,3],[4,5,6],[7,8,9]]
our_table[2][1]

# slice does not change list, just a view














