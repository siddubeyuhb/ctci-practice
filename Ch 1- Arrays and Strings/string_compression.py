# Cracking the Coding Interview Q 1.6 String Compression

def comp(string):
    count = 0
    new_string = ''

    for i in range(len(string)):

        if i == 0:
            count = 1
            new_string += string[i]

        elif string[i] == string[i - 1]:
            count += 1

        else:
            new_string += str(count)
            count = 1
            new_string += string[i]

    new_string = new_string + str(count)

    if (len(string) <= len(new_string)):
        new_string = string

    return new_string


print(comp("abcdA"))
print(comp("aabcdA"))
print(comp("a"))
print(comp("abcddd"))
print(comp("aabcccccaaa"))
