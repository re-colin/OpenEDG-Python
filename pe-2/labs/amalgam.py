# Playground.
# A queue class that uses inheritance. (Linear - A<-B<-C)
# Lambda functions, generators, closures. 

class QueueDefine():
    def __init__(self):
        self.__queue = []
        print("Queue list init here.")


# super() on its own returns the current class if its not inherited from another class.
class QueueModify(QueueDefine):
    def __init__(self):
        super().__init__()
        print("Queue operations here!")

    def enqueue(self, val):
        self._QueueDefine__queue.append(val)

    def dequeue(self):
        del self._QueueDefine__queue[0]


class QueueRead(QueueModify):
    def __init__(self):
        super().__init__()
        print("Queue read ops here!")

    def show_queue(self):
        return self._QueueDefine__queue

    def peek(self):
        return self._QueueDefine__queue[0]  


# q1 = QueueDefine()
q2 = QueueModify()

q2.enqueue(2)
q2.enqueue(3)
q2.enqueue(7)
q2.enqueue(9)
q2.enqueue(4)

# print("q1 queue:", q1._QueueDefine__queue)
print("q2 queue:", q2._QueueDefine__queue) # Since show_queue isnt in the class.
q2.dequeue()
q2.dequeue()

print("q2 queue:", q2._QueueDefine__queue)

q3 = QueueRead()

q3.enqueue(5)
q3.enqueue(9)
q3.enqueue(3)
q3.enqueue(7)

print("q3 queue:", q3.show_queue())

class QueueExtras():
    pass