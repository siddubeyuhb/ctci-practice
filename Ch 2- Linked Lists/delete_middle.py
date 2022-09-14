# Cracking the Coding Interview Q 2.3 Delete Middle Node

# Delete a given node form the middle of the linked list

import linkedlist


def delete_middle(ll, node):
    prev = None
    curr = ll.head

    while(curr):
        if(node == curr):
            prev.next = curr.next
            break
        else:
            prev = curr
            curr = curr.next
