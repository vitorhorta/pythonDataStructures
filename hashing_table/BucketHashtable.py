from linkedList.LinkedList import LinkedList

class BucketHashtable:

    def __init__(self):
        self.table = [None for _ in range(31)]

    def hashFunction(self,key):
        return key % len(self.table)

    def addItem(self,key):
        hashKey = self.hashFunction(key)

        if self.table[hashKey] == None:
            self.table[hashKey] = LinkedList()
        self.table[hashKey].push(key)

        return hashKey

    def __repr__(self):
        retorno = ''
        for bucket in self.table:
            retorno = retorno + " " +str(bucket)
        return retorno



