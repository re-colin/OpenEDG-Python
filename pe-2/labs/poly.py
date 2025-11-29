class Queue():
    def __init__(self):
        print("Queue, init!")
        self.__queue = []

    def additem(self, val):
        print("Queue add!")
        self.__queue.append(val)

    def delete(self):
        del self.__queue[-1]



class Stack():
    def __init__(self):
        print("Stack, init!")
        self.__stack = []

    def additem(self, val):
        print("Stack add!")
        self.__stack.append(val)

    def delete(self):
        self.__stack.pop()


q1 = Queue()
s1 = Stack()

q1.additem(5)
q1.additem(3)
q1.additem(1)
q1.additem(2)

s1.additem(9)
s1.additem(1)
s1.additem(6)
s1.additem(4)

q1.additem(2)

# Inherits additem() method from Stack or Queue depending on arg ordering.
class NormalList(Stack, Queue):
    pass

    # def additem(self, val):
    #     print("List add.")
    #     self.__list.append(val)

    # def delete(self):
    #     self.__list.pop()

l1 = NormalList()

l1.additem(2)
l1.additem(5)
l1.additem(7)
l1.additem(9)

