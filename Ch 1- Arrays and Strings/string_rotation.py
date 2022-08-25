# Cracking the Coding Interview Q 1.9 String Rotation


def rotate(s1, s2):
    # is_Substring method can be replaced by 'in' method of python

    if((s2 in s1 * 2) and len(s1) == len(s2)):
        return True
    else:
        return False


print(rotate('erbottlewat', 'waterbottle'))
print(rotate('route', 'outer'))
print(rotate('route', 'eouter'))
