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