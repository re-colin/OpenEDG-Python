class Queue():
    def __init__(self):
        __queue = []

    def __enqueue(self, val):
        self.__queue.insert(0, val)

    def __dequeue(self):
        del self.__queue[0]


# Subclass extending operation of Queue class
class QueueDataOps(Queue):
    def __init__(self):
        super().__init__(self)

    def __show_queue(self):
        return self.__queue

    def __peek_queue(self):
        return self.__queue[0]


q1 = QueueDataOps()