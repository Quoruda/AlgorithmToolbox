class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

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
        if self.size > 0:
            self.size -= 1
            self.index = (self.index-1)%self.capacity
            return self.buffer[self.index]   
        else:
            raise IndexError("Pop from an empty stack")
            
    def peek(self):
        if self.size > 0:
            return self.buffer[(self.index-1)%self.capacity]
        else:
            raise IndexError("Peek from an empty stack")
        
    def __str__(self):
        content = "["
        for i in range(self.size):
            if i != 0:
                content+= ','
            content += str(self.buffer[(self.index+i)%self.capacity])
        content += "]"
        return content
    
