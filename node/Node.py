class Node:
    value = None
    next = None

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __add__(self, other):
        return self.value + other.value