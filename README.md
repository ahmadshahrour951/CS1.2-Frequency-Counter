# CS 1.1 Frequency Counter

This project is mean to help assist the user to count the number of words given a .txt document is a cool print fashion in each line. (ex. and: 3, to: 1, the: 1, etc.)

This project uses three main classes:
- HashTable.py
- LinkedList.py
- Node.py

HashTable.py will hold the functionality of creating and managing a hash table by chaining. The chaining will essentially create LinkedList for every element in order to resolve collisions. It's child would be the LinkedList class. In HashTable you'll find 4 methods:
- create_arr: this function creates an array of LinkedLists, which is called in the constructor along with the size parameter.
- hash_func: this function determines the hash value/index of item with respect to the HashTable. In it, it uses the key given and measures the length of the key to determine its location.
- insert: this function inserts a new given element to the hashtable, it makes use of the hash_func and the LinkedList update method.
- print_key_values: this function 

LinkedList.py will hold the functioniailty of creating and managing a linked list. The basic functionility will include CRU (-D). It's child would be the Node class
- append: this function will reassign the head of the linked list to the item given.
- find: this function will return the index of the item within the linked list
- update: this function will update the item in the linked list with the item given
- length: this will determine the length of the linked list
- print_nodes: this will print all the nodes within the linkedlist

Node.py will hold the next pointer and the data value. This is the most basic element within the whole program.

This of course is only one way to create a hashmap, there are otherways like linear probing etc.