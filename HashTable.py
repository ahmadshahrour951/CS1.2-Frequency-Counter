from LinkedList import LinkedList


class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    def create_arr(self, size):
        # This function uses the map method to generate an arrat of linkedlists
        return list(map(lambda x: LinkedList(), [None] * size))
