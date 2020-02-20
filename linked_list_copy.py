# -*- coding: utf-8 -*-
#!python3

class Node:

    def __init__(self, data=None):
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class Linked_list:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.d_size = 0

    def empty(self):
        return True if self.d_size == 0 else False

    def size(self):
        return self.d_size
    
    def __del(self):
        print("data of {} is deleted".format(self.data))

    def append(self, data):
        new_node = Node(data)
        if self.d_size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.d_size += 1
        
    def search_target(self, target, start=0):

        if self.empty():
            return None

        pos = 0
        cur = self.head

        if pos >= start and target == cur.data:
            return cur.data, pos
        
        while cur.next:
            pos += 1
            cur = cur.next
            if pos >= start and target == cur.data:
                return cur.data, pos
    
        return None, None

    def search_pos(self, pos):

        if pos > self.size() -1:
            return None

        cnt = 0
        cur = self.head
        if cnt == pos:
            return cur.data
        while cnt < pos:
            cnt +=1
            cur = cur.next
        return cur.data


    def remove(self, target):
        if self.empty():
            return None

        bef = self.head
        cur = self.head

        if target == cur.data:
            if self.size() == 1:
                self.head = None
        if self.empty():
            return None

        bef = self.head
        cur = self.head

        if target == cur.data:
            if self.size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.d_size -= 1

            return cur.data
        while cur.next:
            bef = cur
            cur = cur.next
            if cur.data == target:
                if cur == self.tail:
                    self.tail = bef
                bef.next = self.next
                self.d_size -= 1
                return cur.data
        print('no such value')
        return None

def show_list(slist):
    if slist.empty():
        print("This list is empty")
        return
    for i in range(slist.size()):
        #print("searching index: {}".format(i))
        print(slist.search_pos(i), end = '|')
    print('\n')

if __name__ == "__main__":

    slist = Linked_list()
    slist.append(5)
    slist.append(4)
    slist.append(3)
    slist.append(2)
    slist.append(1)
    slist.append(10)

    target_value, pos = slist.search_target(10)
    print("{} is located <{}>".format(target_value, pos))
    print(slist.size())
    show_list(slist)
    slist.remove(5)
    print(slist.size())
    show_list(slist)
    slist.remove(5)

