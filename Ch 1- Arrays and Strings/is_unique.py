## Cracking the Coding Interview Q 1.1 Is Unique 
def is_unique(string):
    # Str -> Bool
    # Done using Hash table (Dictionary)
    # in O(n) time

    table = {}
    for i in string:
        if i in table:
            return(print(False))
        else:
            table[i] = i
    print(True)


is_unique("abcd")
is_unique("abcda")
is_unique("aa")


def is_unique_regular(string):
	# Str -> Bool
	# Method 1: Complexity O(n^2)
	# Can be done using two loops for the first and 
	# all the subsequent characters
	# 
	# Method 2: 
