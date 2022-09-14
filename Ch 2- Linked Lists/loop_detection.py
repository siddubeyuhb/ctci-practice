# Cracking the Coding Interview Q 2.8 Loop Detection

# Given a circular linked list, return the node at
# the begenning of the loop

import linkedlist


def loop(ll):
    # O(N) time and O(1) space complexity

    point = ""  # temporary node where all pointers point

    while(ll):

        if(ll.next == point):
            return ll.next.val

        else:
            temp_pointer = ll.next
            ll.next = point
            ll. temp_pointer
    return None
