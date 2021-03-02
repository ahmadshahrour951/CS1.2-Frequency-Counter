from LinkedList import LinkedList


class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    def create_arr(self, size):
        # This function uses the map method to generate an arrat of linkedlists
        return list(map(lambda x: LinkedList(), [None] * size))

    def hash_func(self, key):
        # This function is the logic to generate a key to store the item in a linked list, it uses length of the key and % to loop through the list if the length of key is larger than self.size
        return len(key) % self.size

    def insert(self, key, value):
        # This function will check if the value is in the linkedlist, if it is it will add to its current frequency, it is insnt it simply does an append. Refer to linked_list.find and .update
        item = [key, value]
        hash_key = self.hash_func(key)
        linked_list = self.arr[hash_key]
        linked_list.update(item)

    def print_key_values(self):
        # loops through the arr and through every linked list node to print the frequencies
        for linked_list in self.arr:
            if not linked_list.head:
                continue

            current = linked_list.head

            while current:
                print(current)
                current = current.next
