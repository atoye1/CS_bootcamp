#!python3
# -*- coding: utf-8 -*-

from linked_list import Node

class Node:

    def __init__(self, data):

        self.next = None
        self.prev = None
        self.data = data
    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.container = list() 

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def peek(self):
        return self.container[-1]

class Queue(Stack):

    def pop(self):
        value = self.container[0]
        self.container = self.container[1:]
        return value
    
if __name__ == "__main__":
    s = Queue()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    
    while not s.empty():
        data = s.pop()
        print(data, end = ' | ')
