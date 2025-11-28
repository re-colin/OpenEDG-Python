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

class QueueExtras(QueueDefine):
    def __init__(self):
        super().__init__()
        print("Extras here! :)")

    def multiply_queue(self, queue, by):
        __nqueue = []
        for i in range(len(queue)):
            __nqueue.append(queue[i] * by)
        return __nqueue

    def generate_queue(self, queue):
        for i in range(len(queue)):
            yield queue[i]     


q4 = QueueExtras()

queue = [2, 4, 5, 9]

gq = q4.generate_queue(queue)

# Perform an operation and copy result via list comprehension
l = [queue[i]-1 for i in range(len(queue))]
print(l)

qcopy = []
print(gq)
for gi in gq:
    print(gi)

print(QueueExtras.__dict__)
print(q4.__dict__)

nq = q4.multiply_queue(queue, 4)
print(nq)