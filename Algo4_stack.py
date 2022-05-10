   

class StackNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class Stack:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        if self.root is None: return True
        else: return False
    
    def push(self,key):
        new = StackNode(key)
        new.next = self.root
        self.root = new
        #print(new.key) # print pushed key
    
    def pop(self):
        if self.isEmpty():
            return "error"
        temp = self.root
        self.root = self.root.next
        popped = temp.key
        print(popped) #print key that was popped
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.key



N = int(input())
operations = []

stack = Stack()

for i in range(N):

    str = input()
    if str == "PO":
        stack.pop()

    else:
        str, key = str.split()
        stack.push(key)



#stack.push(5)
#stack.push(2)
#stack.push(3)
#stack.push(6)
#stack.push(1)
#stack.pop()
#stack.pop()
#stack.pop()
#stack.pop()
