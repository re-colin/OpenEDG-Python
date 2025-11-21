## METHOD RESOLUTION ORDER (MRO)
# Not all inheritance makes sense.

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
# class Bottom(Top, Middle): # MRO - This code order is incompatible with the class structure.
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# Diamond inheritance
# Uncertainty.
# Here, Middle_Right was asked for first, so Middle_Right's m_middle is the one that will be invoked.
class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Right, Middle_Left):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# Exceptions part 2
# 'else' block is executed only when no exception occurs in the 'try' block.
# naturally it has to be placed after the last except branch.
# Exceptions are classes.
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError as zd:
        print("Division failure.")
        print(zd)
        print(zd.__str__)
        return None
    else:
        print("Everything went fine.")
        return n
    finally:
        print("This part always executes.")
    
print(reciprocal(2))
print(reciprocal(0))

# This also means all built-in exceptions form a hierarchy of classes.
# This tree can be expanded recursively.
for subclass in BaseException.__subclasses__():
    print(subclass, subclass.__name__)