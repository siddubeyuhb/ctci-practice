# Cracking the Coding Interview Q 2.6 Palindrome

# Reverse linked list and compare elements (till half of linked list)

import linkedlist


def palindrome(ll):
    linked, length = reversed_ll(ll)

    counter = 0
    while(ll and counter <= (length / 2) + 1):
        i = linked.pop()

        if(i == head.value):
            counter += 1
            ll = ll.next
        else:
            return False
    return True


def reversed_ll(ll):
    # O(N) time and O(N) space using a stack

    stack = []
    length = 0
    while(ll):
        stack.append(ll.value)
        length += 1
        ll = ll.next

    return stack, length


def reversed_ll_inplace(ll):
    # Returns the reversed linked list and its length
    # by reversing in place

    # Linked_List -> Linked_List  Int

    prev = None
    current = ll.head
    ahead = None
    counter = 0

    while current:
        ahead = current.next
        current.next = prev
        prev = current
        current = ahead
        counter += 1
    ll.head = prev

    return ll, counter
