from node.Node import Node
class Queue:
    head = None
    tail = None
    size = 0

    def push(self,value):
        if(self.size == 0):
            self.tail = Node(value)
            self.head = self.tail
            self.size = self.size + 1
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size = self.size + 1


    def __str__(self):
        nodes = []
        node = self.head
        while(node != None):
            nodes.append(node.value)
            node = node.next
        return str(nodes)

    def peek(self):
        return self.head.value

    def remove(self):
        if(self.head == None):
            return None
        value = self.head.value
        self.head = self.head.next
        if(self.head == None):
            self.tail = None
        self.size = self.size - 1
        return value

    def printRemoving(self):
        nodes = []
        while (self.head != None):
            node = self.remove()
            nodes.append(node)
        print(nodes)
