class Queue():
    def __init__(self):
        self.__queue_list = []

    def pop(self): # Delete first value (index 0)
        del self.__queue_list[0]

    def push(self, val): # Append to queue
        self.__queue_list.append(val)


queue = Queue()

queue.push(6)
queue.push(7)
queue.push(6)
queue.push(8)
queue.push(7)
queue.push(2)

print(queue.__dict__) # {'_Queue__queue_list': [6, 7, 6, 8, 7, 2]}

queue.pop()
queue.pop()

print(queue.__dict__) # {'_Queue__queue_list': [6, 8, 7, 2]}

try:
    print(queue.__queue_list)
except AttributeError:
    print("Cannot access private variable queue_list.")


class Queue():
    def __init__(self):
        self.queue_list = []

    def pop(self): # Delete first value (index 0)
        del self.queue_list[0]

    def push(self, val): # Append to queue
        self.queue_list.append(val)

queue = Queue()

queue.push(6)
queue.push(7)
queue.push(6)
queue.push(8)
queue.push(7)
queue.push(2)

print(queue.queue_list) 