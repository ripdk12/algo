class QueueNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class Queue:
    def __init__(self):
        self.tail = None
    
    def isEmpty(self):
        if self.tail is None: return True
        else: return False
    
    def enQueue(self, key):
        new = QueueNode(key)
        new.next = self.tail
        self.tail = new

    def deQueue(self):
        if self.isEmpty():
            return


N = int(input())

stack = Queue()

for i in range(N):

    str = input()
    if str == "PO":
        stack.pop()

    else:
        str, key = str.split()
        stack.push(key)
