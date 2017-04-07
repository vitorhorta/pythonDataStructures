from node.Node import Node
class LinkedList:
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

    def getItem(self,value):
        node = self.head
        while (node != None):
            if(node.value == value):
                return node.value
            node = node.next
        return False

    def remove(self,position):
        value = self.head.value
        self.head = self.head.next
        return value

    def __getitem__(self, position):
        item = self.head
        for i in range(0,position):
            if item == None:
                return -1
            item = item.next

        if item == None:
            raise StopIteration

        return item.value

