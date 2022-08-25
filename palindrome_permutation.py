# Cracking the Coding Interview Q 1.4 Palindrome Permutation

def pali(stri):
    stri = stri.lower()
    table = {}

    for char in stri:
        if char == ' ':
            continue
        elif char in table:
            table[char] += 1
        else:
            table[char] = 1

    odd = 0
    for i in table.values():
        if i % 2 == 1:
            odd += 1

    if odd > 1:
        return False
    else:
        return True
    return table.values(), odd


print(pali('taco cat'))
print(pali('taco catta'))
print(pali('taco cati'))
