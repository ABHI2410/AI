
## implementation of Stack Data Structure
class Stack:

    ## initializing Stack if items are provided in by default EMPTY stack is initialized
    def __init__(self, items = None):
        self._items = []

        ## if items are provided to be added into the stack use loop to go through each item and add it to stack
        if items:
            for item in items:
                self.push(item)
    
    ## function to add items to stack
    def enqueue(self,item):
        self._items.append(item)
    
    ## function to remove items from stack
    def dequeue(self):
        try:
            item = self._items.pop()
            return item
        except:
            print('Stack is empty')
    
    ## function to check if stack is empty or not 
    def is_empty(self):
        return len(self._items) == 0
    
    ## function to find out the size of stack
    def len_queue(self):
        return len(self._items)
    
    ## function to represent stack if asked to print
    def __repr__(self):
        return f'Stack(items={self._items})'


## implementation of  Queue Data Structure
class Queue:

    ## initializing  Queue if items are provided in by default EMPTY  Queue is initialized
    def __init__(self, items = None):
        self._items = []

         ## if items are provided to be added into the  Queue use loop to go through each item and add it to  Queue
        if items:
            for item in items:
                self.push(item)
    
    ## function to add items to  Queue
    def enqueue(self,item):
        self._items.append(item)
    
    ## function to remove items from  Queue
    def dequeue(self):
        try:
            item = self._items[0]
            self._items = self._items[1:]
            return item
        except:
            print('Queue is empty')
    
    ## function to check if  Queue is empty or not 
    def is_empty(self):
        return len(self._items) == 0
    
    ## function to find out the size of  Queue
    def len_queue(self):
        return len(self._items)
    
    ## function to represent  Queue if asked to print
    def __repr__(self):
        return f'Queue(items={self._items})'


## implementation of Priority Queue Data Structure
class PriorityQueue:

    ## initializing Priority Queue if items are provided in by default EMPTY Priority Queue is initialized
    def __init__(self, items = None):
        self._items = []
        
         ## if items are provided to be added into the Priority Queue use loop to go through each item and add it to Priority Queue
        if items:
            for item in items:
                self.enqueue(item)
    
    ## function to add items to Priority Queue
    def enqueue(self,item):
        self._items.append(item)
        self._items.sort(key = lambda x : x.cost)

    ## function to remove items from Priority Queue
    def dequeue(self):
        try:
            item = self._items[0]
            self._items = self._items[1:]
            return item
        except:
            print('Priority Queue is empty')
    
    ## function to check if Priority Queue is empty or not 
    def is_empty(self):
        return len(self._items) == 0
    
    ## function to find out the size of Priority Queue
    def len_queue(self):
        return len(self._items)
    
    ## function to represent Priority Queue if asked to print
    def __repr__(self):
        return f'Priority Queue(items={self._items})'


## implementation of Priority Queue Data Structure
class PriorityQueue1:

    ## initializing Priority Queue if items are provided in by default EMPTY Priority Queue is initialized
    def __init__(self, items = None):
        self._items = []

         ## if items are provided to be added into the Priority Queue use loop to go through each item and add it to Priority Queue
        if items:
            for item in items:
                self.enqueue(item)
    
    ## function to add items to Priority Queue
    def enqueue(self,item):
        self._items.append(item)
        self._items.sort(key = lambda x : x.heuristic)

    ## function to remove items from Priority Queue
    def dequeue(self):
        try:
            item = self._items[0]
            self._items = self._items[1:]
            return item
        except:
            print('Priority Queue is empty')
    
    ## function to check if Priority Queue is empty or not 
    def is_empty(self):
        return len(self._items) == 0
    
    ## function to find out the size of Priority Queue
    def len_queue(self):
        return len(self._items)
    
    ## function to represent Priority Queue if asked to print
    def __repr__(self):
        return f'Priority Queue(items={self._items})'