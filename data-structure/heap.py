class Heap:
    def getParent(self, i):
        return i // 2
    def getLeft(self, i):
        c = 2 * i
        return c if c < len(self.storage) else -1
    def getRight(self, i):
        c = 2 * i + 1
        return c if c < len(self.storage) else -1
    def swap(self, i, j):
        t = self.storage[i]
        self.storage[i] = self.storage[j]
        self.storage[j] = t
    
    def show(self):
        print(self.storage)

    def pop(self):
        if len(self.storage) == 1: return None
        elif len(self.storage) == 2: return self.storage.pop()
        val = self.storage[1]
        self.storage[1] = self.storage.pop()
        now = 1
        lc = self.getLeft(now)
        rc = self.getRight(now)
        while not (lc == -1 and rc == -1):
            if lc == -1:
                bc = rc       
            elif rc == -1:
                bc = lc
            else:
                bc = lc if self.storage[lc] > self.storage[rc] else rc
            if self.storage[bc] < self.storage[now]:
                break
            self.swap(bc, now)
            now = bc
            lc = self.getLeft(now)
            rc = self.getRight(now)
        return val
        
    def push(self, val):
        self.storage.append(val)
        now = len(self.storage) - 1
        parent = self.getParent(now)
        while (not now == 1) and (self.storage[now] > self.storage[parent]):
            self.swap(now, parent)
            now = parent
            parent = self.getParent(now)
            
    def __init__(self):
        self.storage = [-1]

heap = Heap()
heap.push(10)
heap.push(15)
heap.push(26)
heap.push(30)
heap.push(25)
heap.show()
print(heap.pop())
heap.show()
print(heap.pop())
heap.show()
print(heap.pop())
heap.show()