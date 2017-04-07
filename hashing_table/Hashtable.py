class Hashtable:
    colisionSolution = None

    def __init__(self):
        self.table = [None for _ in range(10)]
        self.colisionSolution = self.linearSolution

    def hashFunction(self,key):
        return key % len(self.table)

    def linearSolution(self,hashKey,numberOfTries):
        return hashKey + numberOfTries

    def quadraticSolution(self,hashKey,numberOfTries):
        return hashKey + numberOfTries*numberOfTries

    def resolveColision(self,hashKey):
        numberOfTries = 0
        colidedHashKey = hashKey
        while (self.table[hashKey] != None):
            numberOfTries = numberOfTries + 1
            hashKey = self.colisionSolution(colidedHashKey,numberOfTries)
            if hashKey >= len(self.table):
                hashKey = 0

            if numberOfTries >= len(self.table):
                return -1
        return hashKey

    def addItem(self,key):
        hashKey = self.hashFunction(key)
        hashKey = self.resolveColision(hashKey)

        if(hashKey != -1):
            self.table[hashKey] = key

        return hashKey

    def __repr__(self):
        return str(self.table)



