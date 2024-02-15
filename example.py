#!/usr/bin/env python3

"""
Example of linked list implementation
"""
from linked_lists import SLinkedList, DLinkedList
import time

# dll = DLinkedList()

# dll.add(50)
# dll.add(60)
# dll.add(70)
# dll.add(80)
# dll.add(90)
# dll.add(150)
# dll.add(160)
# dll.add(170)
# dll.add(180)
# dll.add(190)

# for x in dll:
#     print(x.data)

# # dll.print_sll()
# dll.print_dll()

start = time.perf_counter()
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

sll.reverse()
sll.print_sll()

# for x in sll.reversed_iterator():
#     if x.data == 90:
#         print(x.next.data)

print(f'Elapsed time: {time.perf_counter() - start:.6f} seconds')
# sll.print_sll()