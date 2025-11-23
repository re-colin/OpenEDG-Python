# __init__ method/function is ran implicitly.
# __ prefixed variables become private; only visible from within the class.
class Stack():
    def __init__(self):
        self.__stack = []
    
    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        del self.__stack[-1]

    def show_stack(self):
        print(self.__stack)

s1 = Stack()
s1.push(2)
s1.push(3)
s1.push(7)

# Attempting to access a private variable raises AttributeError.
try: 
    print(s1.stack)
except AttributeError:
    print("s1.stack variable private to Stack.")

# To show data from your class, either create a custom function within it that shows what you want:
s1.show_stack()  # [2,3,7]

# Or access the __dict__ variable.
# See m3-oop-3.py for __dict__ info.
print(Stack.__dict__)
print(s1.__dict__)