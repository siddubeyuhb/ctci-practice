# Cracking the Coding Interview Q 1.3 URLify

def URLify(stri, num):
    # Replace all spaces in a string with '%20'
    # Str Num -> Str
    stri = stri.strip()	# Strip the first and last spaces 

    new_str = ''
    for i in stri:
        if i == ' ':
            new_str += '%20'
        else:
            new_str += i

    return(new_str)


print(URLify("Mr John Smith   ", 13))
print(len(URLify("Mr John Smith", 13)))
