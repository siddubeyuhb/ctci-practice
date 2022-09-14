# Cracking the Coding Interview Q 2.7 Intersection

# Determine if two singly linked lists intersect
# Return the intersecting node or None if none exist

import linkedlist


def intersection(ll1, ll2):
    buffer = ""

    while(ll1):
        temp_pointer = ll1.next
        ll1.next = buffer
        ll1 = temp_pointer

    while(ll2):
        if(ll2.next == buffer):
            return ll2.next
        else:
            ll2 = ll2.next
    return None
