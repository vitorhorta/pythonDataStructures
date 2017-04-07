from node.Node import Node
class Stack:
    head = None

    def push(self,value):
        if(self.head == None):
            self.head = Node(value)
            return
        self.head = Node(value,self.head)

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
        value = self.head.value
        self.head = self.head.next
        return value

    def printRemoving(self):
        nodes = []
        while (self.head != None):
            node = self.remove()
            nodes.append(node)
        print(str(nodes))