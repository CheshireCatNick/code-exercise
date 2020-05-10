class Node:
    def __init__(self, key, val):
        self.prev = None
        self.val = val
        self.key = key
        self.next = None

class LRUCache:
    def moveToTail(self, node):
        if node.next == None:
            return
        prev = node.prev
        nxt = node.next
        if prev == None:
            # at head
            nxt.prev = None
            self.head = nxt        
        else:
            # in middle
            prev.next = nxt
            nxt.prev = prev
        self.tail.next = node
        node.next = None
        self.tail = node
        
    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.head = None
        self.tail = None
        self.data = {}
        
    def get(self, key: int) -> int:
        if key in self.data:
            self.moveToTail(self.data[key])
            return self.data[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if len(self.data) == 0:
            self.head = Node(key, value)
            self.tail = self.head
            self.data[key] = self.head
        else:
            if key in self.data:
                # update data
                self.moveToTail(self.data[key])
                self.data[key].val = value
            else:
                # add data
                if len(self.data) == self.maxCapacity:
                    # remove least used cache
                    self.data.pop(self.head.key)
                    if self.maxCapacity == 1:
                        self.put(key, value)
                        return
                    self.head = self.head.next
                    self.head.prev = None
                # append new data to tail
                n = Node(key, value)
                n.prev = self.tail
                self.tail.next = n
                self.tail = n
                self.data[key] = n

