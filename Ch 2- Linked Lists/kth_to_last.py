# Cracking the Coding Interview Question 2.2 Return k-th to last
# Return kth to last element of a singly linked list

def kth_last(ll, k):

    lead = lag = ll.head
    count = 0

    while(lead and lag):
        if count >= k:
            lead = lead.next
            lag = lag.next
            count += 1
        else:
            lead = lead.next
            count += 1

    return lag
