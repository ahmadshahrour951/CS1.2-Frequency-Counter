from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def find(self, item):
        current = self.head

        found = False
        counter = 0

        while current != None and not found:

            if current.data == item:
                found = True
            else:
                current = current.next
                counter += 1

        if found:
            return counter
        else:
            return -1

    def update(self, item):
        current = self.head

        # loop through every node in the linkedlist, if we find the key then update and stop otherwise continue
        while current != None:
            if current.data[0] == item[0]:
                current.data[1] += item[1]
                return
            else:
                current = current.next
        
        # if we reach here that means we didnt find the item[key] in any node within the linkedlist, so just append
        self.append(item)

    def length(self):
        if self.head == None:
            return 0
        else:
            counter = 1
            current = self.head
            while(current.next):
                current = current.next
                counter += 1
            return counter

    def print_nodes(self):
        current = self.head

        if current == None:
            print('The linked list is empty.')
        else:
            for i in range(self.length()):
                print(f'Node {i}: {current.data}')
                current = current.next
