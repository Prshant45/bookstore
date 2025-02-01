# print("hello world")

# """
# conditional operator
# arithmetic operator
# logical operator
# bitwise operator


# """

# #type and isinstanc

# class A:
#     pass

# class B(A):
#     pass


# obj = B()

# print(type(obj))
# print(isinstance(obj, A))
# a = "helloworld"
# print(a[::-1])
# for ch in a:
#     print(ch, end= " ")
#     if ch == "a":
#         print("finds a")
#     elif ch == "b":
#         print("finds b")
#     else:
#         print("others")

import time
from datetime import datetime



def dec(func):
    def inner(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        diff = time.time() - before
        print(diff)
        return value
    return inner

# func2 = func
# print(func())
@dec
def func():
    print("I am here")
    time.sleep(2)

# inner_func = dec(func)
# inner_func()
func()

# generator
from typing import List

def square(list1: List[int]):
    for i in list1:
        yield i ** 2

list1 = [2, 3, 4]
squares = square(list1)
print(type(squares))
for i in squares:
    print(i)

list2 = [i**2 for i in list1]
print(list2)

#C
# class A
# {
#     int sum(int a, int b)
#     {
#         return a + b;
#     }
#     double sum(double a, double b)
#     {
#         return a + b;
#     }
# }


class A:
    def __init__(self):
        pass

    def sum(self, a, b):
        return a + b

class B(A):
    def __init__(self):
        pass

    def sum(self, a, b):
        return a * b


a = A()
print(a.sum(10, 10))
print(a.sum(10.2, 10.2))

class C(A):

    def __init__(self):
        super().__init__()
    
    def sum(self, a, b):
        return a - b
    
class D(A):

    def __init__(self):
        super().__init__()
        self.a = B() # composition # tightly coupled
        self.b = None #
    
    # injection method # loosely coupled
    def inject(self, b):
        self.b = b


d = D().inject(D())
