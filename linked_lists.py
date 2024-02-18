from typing import Optional

class Node:
    """Data structure
    """
    id = 0
    def __init__(self, data: Optional[str] = None, prev: Optional['Node'] = None, next: Optional['Node'] = None) -> None:
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

    def __str__(self) -> str:
        prev = self.prev.data if self.prev != None else None
        next = self.next.data if self.next != None else None
        return f'{prev}<--{self.data}-->{next}'
    
    def data(self) -> str:
        return f'{self.data}'
    

class SLinkedList:
    """My personal implementation of a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
        len (int): The length of the linked list.
        iter_count (int): The count used for iteration over the linked list.
    """

    def __init__(self) -> None:
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

    def len(self) -> int:
        return self.len

    def add(self, data: str) -> None:
        temp_node = Node(data)
        temp = self.head
        if temp.data == None:
            self.head.data = data
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = temp_node
        self.len += 1
    
    def pop(self) -> None:
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

    def insert(self, data: str, index: int) -> None:
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

    def remove(self, index: int) -> None:
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

    def search(self, data: str) -> Optional[int]:
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
        
    def index(self, index: int) -> Node:
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
        if index == count:
            return temp
        
    def reverse(self) -> None:
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reversed(self) -> None:
        len = self.len
        temp = self.head
        new = SLinkedList()
        for i in range(len, 0, -1):
            temp = self.index(i-1)
            new.add(temp.data)
        return new


    def print_sll(self) -> None:
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

    Attributes:
        head (Node): The head node of the linked list.
        len (int): The length of the linked list.
        iter_count (int): The current iteration count for iterating over the linked list.

    Methods:
        __init__(): Initializes a new instance of the DLinkedList class.
        __iter__(): Returns the iterator object for the linked list.
        __next__(): Returns the next node in the iteration.
        add(data: str): Adds a new node with the specified data to the end of the linked list.
        search(data: str) -> Optional[int]: Searches for the first occurrence of the specified data in the linked list.
        print_dll(): Prints the data of all nodes in the linked list.
        index(index: int) -> Node: Returns the node at the specified index in the linked list.
    """
    
    def __init__(self) -> None:
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
            raise StopIteration

    def add(self, data: str) -> None:
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

    def search(self, data: str) -> Optional[int]:
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

    def print_dll(self) -> None:
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

    def index(self, index: int) -> Node:
        if index >= self.len:
            raise IndexError('Cannot peek beyond indexable length of list')
        if index < 0:
            raise IndexError('Invalid Index, must be greater or equal to 0 and less than the length of the list')
        temp = self.head
        count = 0
        while temp.next is not None:
            if index == count:
                return temp
            temp = temp.next
            count += 1
        if index == count:
            return temp