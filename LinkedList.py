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

    def update(self, ind, item):
        if ind == -1:
            # try to find out if its because of the value is not equal or if its because it's the first time the linked_list has seen this
            current_node = self.head

            while current_node:
                if current_node.data and current_node.data[0] == item[0]:
                    # just update value then end
                    current_node.data[1] += item[1]
                    return
                else:
                    # otherwise continue the loop to the next node
                    current_node = current_node.next

            # if code reaches here, means the word doesn't exist in the LinkedList, so just simply append
            self.append(item)

        else:
            # otherwise find the node and update its value
            current_node = self.head
            copy_ind = ind

            while copy_ind != -1:
                current_node.next
                copy_ind -= 1

            current_node.data[1] += item[1]

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
