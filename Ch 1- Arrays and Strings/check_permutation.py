# Cracking the Coding Interview Q 1.2 Check Permutation

def check(str1, str2):
    # Make characters of the larger string as a dict
    # then for loop over the shorter string and check
    # if they belong in the dictrionary, if all of them do
    # then its a permutation, if they dont then its not

    # Str Str -> Bool

    table = {}
    if(len(str1) >= len(str2)):
        large = str1
        short = str2
    else:
        large = str2
        short = str1

    table = dict.fromkeys(large)

    for i in short:
        if i in table:
            continue
        else:
            return(print(False))
    return(print(True))


check("abcd", "ab")
check("abcd", "3")
check("abcd", "bd")
