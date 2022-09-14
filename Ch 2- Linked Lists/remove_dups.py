# Cracking the Coding Interview Q 2.1 Remove Dups

# Remove duplicates from an unsorted linked list
import linkedlist


def remove(linked_list):
    unique = set()
    current = linked_list.next
    whatsbefore = None

    while(current):
        if current.value in unique:
            whatsbefore.next = current.next
        else:
            unique.add(current.value)
            whatsbefore = current
        current = current.next

    return linked_list
