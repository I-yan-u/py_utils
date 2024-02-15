#!/usr/bin/env python3

"""
Example of linked list implementation
"""
from linked_lists import SLinkedList, DLinkedList

sll = SLinkedList()

sll.add(50)
sll.add(60)
sll.add(70)
sll.add(80)
sll.add(90)
sll.add(150)
sll.add(160)
sll.add(170)
sll.add(180)
sll.add(190)

for x in sll:
    print(x)

sll.print_sll()
# data2 = dll.index(1)
# data3 = dll.index(2)
# data4 = dll.index(3)
# print(data2)
# print(data3)
# print(data4)

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