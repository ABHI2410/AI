class Stack:
    def __init__(self, items = None):
        self._items = []

        if items:
            for item in items:
                self.push(item)
    

    def push(self,item):
        self._items.append(item)
    

    def pop(self):
        try:
            item = self._items.pop()
            return item
        except:
            print('Stack is empty')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def len_stack(self):
        return len(self._items)
    
    def __repr__(self):
        return f'Stack(items={self._items})'


class Queue:
    def __init__(self, items = None):
        self._items = []

        if items:
            for item in items:
                self.push(item)
    

    def enqueue(self,item):
        self._items.append(item)
    

    def dequeue(self):
        try:
            item = self._items[0]
            self._items = self._items[1:]
            return item
        except:
            print('Stack is empty')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def len_queue(self):
        return len(self._items)
    
    def __repr__(self):
        return f'Queue(items={self._items})'


class PriorityQueue:
    def __init__(self, items = None):
        self._items = []

        if items:
            for item in items:
                self.push(item)
    

    def enqueue(self,item):
        self._items.append(item)
        self._items.sort(key = lambda x : x.cost)
    

    def dequeue(self):
        try:
            item = self._items[0]
            self._items = self._items[1:]
            return item
        except:
            print('Stack is empty')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def len_queue(self):
        return len(self._items)
    
    def __repr__(self):
        return f'Priority Queue(items={self._items})'