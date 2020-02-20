#!python3

class Node:
    def __init__(self, data=None):
        #노드는 데이터 부분과 다음 노드를 가르키는 참조를 포함
        self.head = None
        self.tail = None
        self.d_size = 0
        self.__data = data
        self.__next = None

    def __del(self):
        print("data of {} is deleted".format(self.data))


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

    def append(self, data):
        #맨 마지막에 데이터를 삽입
        return None

    def search_target(target, start=0):

        return (data, pos)

    def search_pos(pos):
        return data

    def remove(target):
        return data

    def empty():
        return True if self.d_size==0 else False

    def size():
        return self.d_size
