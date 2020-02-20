# -*- coding: utf-8 -*-
#!python3
# 컴퓨터사이언스 부트캠프  with 파이썬 연습파일입니다.


class Node:

    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self,data):
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
        return True if self.d_size==0 else False

    def size(self):
        return self.d_size


    def __del(self):
        print("data of {} is deleted".format(self.data))


    def append(self, data):
        #맨 마지막에 데이터를 삽입
        new_node = Node(data)
        
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.d_size += 1

        return None

    def search_target(self, target, start=0):

        if self.empty():
            return None
        pos = 0
        cur = self.head
        if pos >= start and target == cur.data:
            return cur.data, post
        
        while cur.next:
            pos += 1
            cur = cur.next
            if pos >= start and target == cur.data:
                return cur.data, pos

        return None, None

        return (data, pos)

    def search_pos(self, pos): 
        '''
        search_target(target, start =0 ) - > (data, post)
       ''' 
        if pos > self.size() - 1:
            return None

        cnt = 0 
        cur = self.head
        if cnt == pos:
            return cur.data
        while cnt < pos:
            cur = cur.next
            cnt += 1
        return cur.data

    

    def remove(self, target):
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
                bef.next = cur.next
                self.d_size -= 1
                return cur.data
        return None

def show_list(slist):
    if slist.empty():
        print('The list is empty')
        return
    for i in range(slist.size()):
        print('searching index: {}'.format(i))
        print(slist.search_pos(i), end = ' ')

if __name__ == "__main__":

    #slist = Linked_list()
    #print("데이터개수: {}".format(slist.size()))
    #show_list(slist)
    #print()
    #
    #slist.append(2)
    #print("데이터개수: {}".format(slist.size()))
    #show_list(slist)
    #print()
   
    #if slist.remove(1):
    #    print("데이터개수: {}".format(slist.size()))
    #    show_list(slist)
    #    
    #    print()


    #nlist = Linked_list()
    #nlist.append(5)
    #nlist.append(10)
    #nlist.append(6)
    #nlist.append(1)
    #nlist.append(2)
    #nlist.append(7)
    #nlist.append(99)
    #
    #print("Num of DATA: {}".format(nlist.size()))
    #show_list(nlist)
    #print()

    #if nlist.remove(2):
    #    print(nlist.size())
    #    show_list(nlist)
    #else:
    #    print('target not found')

    #if nlist.remove(2):
    #    print(nlist.size())
    #    show_list(nlist)
    #else:
    #    print('target not found')


    nlist = Linked_list()
    nlist.append(5)
    nlist.append(10)
    nlist.append(6)
    nlist.append(1)
    nlist.append(2)
    nlist.append(7)
    nlist.append(99)

    data1, pos1 = nlist.search_target(1)

    if data1:
        print('searched data : {} at pos<{}>'.format(data1, pos1))
    else:
        print('there is no such data')

    data2, pos2 = nlist.search_target(99, pos1 + 1)

    if data2:
        print('searched data : {} at pos<{}>'.format(data2, pos2))
    else:
        print('there is no such data')
