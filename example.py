#!/usr/bin/env python3

"""
Example of linked list implementation
"""
from linked_lists import SLinkedList, DLinkedList

dll = DLinkedList()

dll.add(50)
dll.add(60)
dll.add(70)
dll.add(80)
dll.add(90)
dll.print_dll()
data4 = dll.index(3)
print(data4.prev)

# sll = SLinkedList()

# sll.add(50)
# sll.add(60)
# sll.add(70)
# sll.add(80)
# sll.add(90)
# sll.print_sll()
# print(sll.len)
# print(sll.index(0))
# print(sll.index(1))
# index = sll.search(40)
# print(sll.len)