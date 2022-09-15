# Cracking the Coding Interview Q 2.5 Sum Lists

# Part 1: Add the linked lists where digits are in reverse order
# Part 2: Add the linked lists with digits in proper forward order
import linkedlist


def sum_reverse(ll1, ll2):
    carry = 0
    sum_ll = None
    new_head = None
    while(ll1 or ll2):
        value_sum = carry

        if (ll1.next is not None):
            value_sum = ll1.value
            ll1 = ll1.next
        if(ll2.next is not None):
            value_sum = ll2.value
            ll2 = ll2.next

        new_node = Node(value_sum % 10)
        carry = value_sum // 10

        if sum_ll is None:
            sum_ll = new_node
            new_head = sum_ll
        else:
            sum_ll.next = new_node
            sum_ll = sum_ll.next

    if(carry > 0):
        sum_ll.next = Node(carry)

    return new_head
