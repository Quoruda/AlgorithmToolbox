class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()            

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]            

    def size(self) -> int:
        return len(self.items)
    
class CircularStack:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.buffer = [None for _ in range(self.capacity)]
        self.index = 0
        self.size = 0
        
    def is_empty(self) -> bool:
        return self.size == 0
    
    def is_full(self) -> bool:
        return self.size == self.capacity
    
    def push(self, item) -> None:
        self.buffer[self.index] = item
        self.index = (self.index+1)%self.capacity
        if(self.size < self.capacity):
            self.size += 1
            
    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        self.size -= 1
        self.index = (self.index-1)%self.capacity
        return self.buffer[self.index]        
            
    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.buffer[(self.index-1)%self.capacity]            
        
    def __str__(self) -> str:
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
        
    def enqueue(self, item) -> None:
        self.buffer.append(item)
    
    def dequeue(self) -> object:
        if self.is_empty(): 
            raise IndexError("Dequeue from an empty queue")
        item = self.buffer[0]
        self.buffer.pop(0)
        return item
            
    
    def size(self) -> int:
        return len(self.buffer)
    
    def next(self) -> object:
        return self.buffer[0]
    
    def is_empty(self) -> bool:
        return len(self.buffer) == 0

class Link:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0
        
    
    def append(self, value) -> None:
        if self.size == 0:
            self.start = Link(value)
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = Link(value)
        self.size += 1
        
    def pop(self, index=0) -> object:
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
    
    def getLink(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        current = self.start
        for i in range(index):
            current = current.next
        return current
    
    def get(self, index) -> object:
        return self.getLink(index).value
        
    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        content = "["
        current = self.start
        while current is not None:
            if current != self.start:
                content += ','
            content += str(current.value)
            current = current.next
        content += "]"
        return content
     
    def index_of(self, value) -> int:
        current = self.start
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def insert(self, index, value) -> None:
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
    
    def append(self, value) -> None:
        if self.size == 0:
            self.start = DoubleLink(value)
            self.end = self.start
        else:
            new_link = DoubleLink(value)
            new_link.prev = self.end
            self.end.next = new_link
            self.end = new_link
        self.size += 1
        
    def pop(self, index=0) -> object:
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
    
    def get(self, index) -> object:
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
        
    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        content = "["
        current = self.start
        while current is not None:
            if current != self.start:
                content += ','
            content += str(current.value)
            current = current.next
        content += "]"
        return content
    
    def index_of(self, value) -> int:
        current = self.start
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def insert(self, index, value) -> None:
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

class PriorityQueue:
    def __init__(self):
        self.prioritys = []
        self.items = []
        self.size = 0
    
    def enqueue(self, item, priority) -> None:
        if self.size == 0:
            self.prioritys.append(priority)
            self.items.append(item)
            self.size += 1
            return
        if priority >= self.prioritys[self.size-1]:
        
            self.prioritys.append(priority)
            self.items.append(item)
            self.size += 1
            return
        if priority < self.prioritys[0]:
            self.prioritys.insert(0, priority)
            self.items.insert(0, item)
            self.size += 1
            return
        
        imin = 0
        imax = self.size-1
        imid = (imax+imin)//2
        
        while imax-imin > 1:
            imid = (imax+imin)//2
            if self.prioritys[imid] <= priority:
                imin = imid
            else:
                imax = imid
        self.prioritys.insert(imax, priority)
        self.items.insert(imax, item)
        self.size += 1

    def is_empty(self) -> bool:
        return self.size == 0

    def dequeue(self) -> object:
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        self.size -= 1
        self.prioritys.pop()
        return self.items.pop()

    def __str__(self) -> str:
        content = "["
        for i, e in enumerate(self.items):
            if i != 0:
                content += ','
            content += str(e)
        content += "]"
        return content

    def get_size(self) -> int:
        return self.size
