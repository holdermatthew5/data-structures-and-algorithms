from linked_list import Node, LinkedList
import re

class Hash():
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size

    def get_hash(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum % self.size

    def add(self, key, value):
        index = self.get_hash(key)
        if not self.table[index]:
            self.table[index] = LinkedList(Node([key,value]))
        else:
            linked_list = self.table[index]
            linked_list.add([key,value])

    def get(self, key):
        index = self.get_hash(key)
        if not self.table[index]:
            return None
        else:
            bucket_keys = [key[0] for key in self.table[index].display()]
            if key in bucket_keys:
                return self.table[index].head.data[1]

    def contains(self, key):
        index = self.get_hash(key)
        if not self.table[index]:
            return False
        else:
            if key in [key[0] for key in self.table[index].display()]:
                return True
        return False