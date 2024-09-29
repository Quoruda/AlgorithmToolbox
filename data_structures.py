class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()            

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]            

    def size(self):
        return len(self.items)
    
class CircularStack:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.buffer = [None for _ in range(self.capacity)]
        self.index = 0
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def push(self, item):
        self.buffer[self.index] = item
        self.index = (self.index+1)%self.capacity
        if(self.size < self.capacity):
            self.size += 1
            
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        self.size -= 1
        self.index = (self.index-1)%self.capacity
        return self.buffer[self.index]        
            
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.buffer[(self.index-1)%self.capacity]            
        
    def __str__(self):
        content = "["
        for i in range(self.size):
            if i != 0:
                content+= ','
            content += str(self.buffer[(self.index+i)%self.capacity])
        content += "]"
        return content
    
class Queue:
    def __init__(self):
        self.buffer = []
        
    def enqueue(self, item):
        self.buffer.append(item)
    
    def dequeue(self):
        if self.is_empty(): 
            raise IndexError("Dequeue from an empty queue")
        item = self.buffer[0]
        self.buffer.pop(0)
        return item
            
    
    def size(self):
        return len(self.buffer)
    
    def next(self):
        return self.buffer[0]
    
    def is_empty(self):
        return len(self.buffer) == 0

class Link:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0
    
    def append(self, value):
        if self.size == 0:
            self.start = Link(value)
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = Link(value)
        self.size += 1
        
    def pop(self, index=0):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            value = self.start.value
            self.start = self.start.next
        else:
            current = self.start
            for i in range(index-1):
                current = current.next
            value = current.next.value
            current.next = current.next.next
        self.size -= 1
        return value
    
    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        current = self.start
        for i in range(index):
            current = current.next
        return current.value
        
    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
    def __str__(self):
        content = "["
        current = self.start
        while current is not None:
            if current != self.start:
                content += ','
            content += str(current.value)
            current = current.next
        content += "]"
        return content
    
    def index_of(self, value):
        current = self.start
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def insert(self, index, value):
        if index > self.size or index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            new_link = Link(value)
            new_link.next = self.start
            self.start = new_link
        else:
            current = self.start
            for i in range(index-1):
                current = current.next
            new_link = Link(value)
            new_link.next = current.next
            current.next = new_link
        self.size += 1
    
class DoubleLink:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0
    
    def append(self, value):
        if self.size == 0:
            self.start = DoubleLink(value)
            self.end = self.start
        else:
            new_link = DoubleLink(value)
            new_link.prev = self.end
            self.end.next = new_link
            self.end = new_link
        self.size += 1
        
    def pop(self, index=0):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            value = self.start.value
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            else:
                self.end = None
        elif index == self.size-1:
            value = self.end.value
            self.end = self.end.prev
            self.end.next = None
        else:
            if(index > self.size//2):
                current = self.end
                for i in range(self.size-1, index-1, -1):
                    current = current.prev
            else:          
                current = self.start
                for i in range(index-1):
                    current = current.next
            value = current.next.value
            current.next = current.next.next
            current.next.prev = current
        self.size -= 1
        return value
    
    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        if(index > self.size//2):
            current = self.end
            for i in range(self.size-1, index, -1):
                current = current.prev
        else:
            current = self.start
            for i in range(index):
                current = current.next
        return current.value
        
    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
    def __str__(self):
        content = "["
        current = self.start
        while current is not None:
            if current != self.start:
                content += ','
            content += str(current.value)
            current = current.next
        content += "]"
        return content
    
    def index_of(self, value):
        current = self.start
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def insert(self, index, value):
        if index > self.size or index < 0:
            raise IndexError("Index out of range")
        new_link = DoubleLink(value)
        if self.size == 0:
            self.end = new_link
            self.start = new_link
        elif index == 0:
            new_link.next = self.start
            self.start.prev = new_link
            self.start = new_link
        elif index == self.size:
            new_link.prev = self.end
            self.end.next = new_link
            self.end = new_link
        else:
            if(index > self.size//2):
                current = self.end
                for i in range(self.size-1, index-1, -1):
                    current = current.prev
            else:
                current = self.start
                for i in range(index-1):
                    current = current.next
            new_link.next = current.next
            new_link.prev = current
            current.next.prev = new_link
            current.next = new_link
        self.size += 1
