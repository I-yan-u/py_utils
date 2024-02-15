#!/usr/bin/env python3
""" Personal linked list implementation """


class Node:
    """Data structure
    """
    id = 0
    def __init__(self, data=None, prev=None, next=None) -> None:
        Node.id += 1
        self.id = f'n-{Node.id}'
        self.data = data
        if next != None:
            self.next = next
            self.next_id = next.id
        else:
            self.next = None
            self.next_id = None
        if prev != None:
            self.prev = prev
            self.prev_id = prev.id
        else:
            self.prev = None
            self.prev_id = None

    def __str__(self):
        return f'{self.prev.data}<--{self.data}-->{self.next.data}'
    
    def data(self):
        return f'{self.data}'
    

class SLinkedList:
    """My personal implementation of a singly linked list.
    """

    def __init__(self):
        self.head = Node()
        self.len = 0
        self.iter_count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iter_count < self.len:
            node = self.index(self.iter_count)    
            self.iter_count += 1
            return node
        else:
            # self.iter_count = 0
            raise StopIteration

    def add(self, data):
        temp_node = Node(data)
        temp = self.head
        if temp.data == None:
            self.head.data = data
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = temp_node
        self.len += 1
    
    def pop(self):
        if self.head.data is None and self.head.next is None:
            raise IndexError('Cannot pop from an empty list')
        if self.head.next is None:
            self.head.data = None
        else:
            temp = self.head
            temp2 = None
            while temp.next is not None:
                temp2 = temp
                temp = temp.next
            temp2.next = None
            temp.data = None
        self.len -= 1

    def insert(self, data, index):
        if index > self.len:
            raise IndexError('Cannot insert beyond indexable length of list')
        if index < 0:
            raise IndexError('Invalid Index, must be greater or equal to 0 and less that length of list')
        if index == 0:
            temp = Node(data, None, self.head)
            self.head = temp
        else:
            temp1 = self.head
            temp = Node(data)
            count = 0
            while temp1.next is not None:
                temp3 = temp1
                temp1 = temp1.next
                count += 1
                if index == count:
                    temp3.next = temp
                    temp.next = temp1
            count += 1
            if index == count:
                temp1.next = temp
        self.len += 1

    def remove(self, index):
        if index >= self.len:
            raise IndexError('Cannot delete beyond indexable length of list')
        if index < 0:
            raise IndexError('Invalid Index, must be greater or equal to 0 and less that length of list')
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            count = 0
            while temp.next is not None:
                temp3 = temp
                temp = temp.next
                count += 1
                if index == count:
                    temp3.next = temp.next
                    temp.next = None
            count += 1
            temp3 = temp
            if index == count:
                temp3.next = None
        self.len += 1

    def search(self, data):
        temp = self.head
        index = 0
        if temp.data is None and temp.next is None:
            raise IndexError('Empty list')
        if temp.data == data:
            return index
        while temp.next is not None:
            temp = temp.next
            index += 1
            if temp.data == data:
                return index
        index += 1
        if temp.data == data:
            return index
        else:
            return None
        
    def index(self, index):
        if index >= self.len:
            raise IndexError('Cannot peek beyond indexable length of list')
        if index < 0:
            raise IndexError('Invalid Index, must be greater or equal to 0 and less that length of list')
        temp = self.head
        count = 0
        while temp.next is not None:
            if index == count:
                return temp.data
            temp = temp.next
            count += 1
        if index == count:
            return temp.data

    def print_sll(self):
        temp = self.head
        data_str = ''
        if temp.next is None:
            print(temp.data)
        else:
            while temp.next is not None:
                data_str += f'->{temp.data}'
                temp = temp.next
            data_str += f'->{temp.data}'
            print(data_str[2:])


class DLinkedList:
    """My personal implementation of a doubly linked list.
    """

    def __init__(self):
        self.head = Node()
        self.len = 0

    def add(self, data):
        temp_node = Node(data)
        temp = self.head
        if temp.data == None:
            self.head.data = data
        else:
            while temp.next is not None:
                temp = temp.next
            temp_node.prev = temp
            temp.next = temp_node
        self.len += 1

    def search(self, data):
        temp = self.head
        index = 0
        if temp.data is None and temp.next is None:
            raise IndexError('Empty list')
        if temp.data == data:
            return index
        while temp.next is not None:
            temp = temp.next
            index += 1
            if temp.data == data:
                return index
        index += 1
        if temp.data == data:
            return index
        else:
            return None

    def print_dll(self):
        temp = self.head
        data_str = ''
        if temp.next is None:
            print(temp.data)
        else:
            while temp.next is not None:
                data_str += f'<->{temp.data}'
                temp = temp.next
            data_str += f'<->{temp.data}'
            print(data_str[3:])

    def index(self, index):
        if index >= self.len:
            raise IndexError('Cannot peek beyond indexable length of list')
        if index < 0:
            raise IndexError('Invalid Index, must be greater or equal to 0 and less that length of list')
        temp = self.head
        count = 0
        while temp.next is not None:
            if index == count:
                return temp
            temp = temp.next
            count += 1
        count += 1
        if index == count:
            return temp