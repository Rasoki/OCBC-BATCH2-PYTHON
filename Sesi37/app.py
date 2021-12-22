# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'

# my_generator()
# print(my_generator())

# print(list(my_generator()))

# #sisipan
# aa = '100'
# int_aa = int(aa)
# print(int_aa)

# def square(nums):
#     result = []
#     for num in nums:
#         result.append(num * num)

#     return result

# nums = [1,2,3,4,5]
# print(square(nums))

# function --> generator
# def square(nums):
#     for num in nums:
#         yield num * num

# nums = [1,2,3,4,5].__iter__()
# print(square(nums))

# square_generator = square(nums)
# for num in nums in square_generator:
#     print(num)

# print(square(nums).__next__())
# print(next(square(nums)))
# print(next(square(nums)))
# print(next(square(nums)))
# print(next(square(nums)))
# print(next(square(nums)))

# from typing import List


# List comprhension :
# squared_nums = [y * y for y in [1,2,3,4,5] ]
#                 # 1 * 1 = 1
#                 # 2 * 2 = 4
#                 # 3 * 3 = 9
#                 # 4 * 4 = 16
#                 # 5 * 5 = 25
# print(squared_nums)

# squared_nums = [y + 4 for y in range(7)]


# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'

# store_generator = my_generator()
# print( next(store_generator))
# print( next(store_generator))
# print( next(store_generator))
# def counter_generator(low, high):
#     while low <= high:
#        yield low
#        low += 1

# for i in counter_generator(5,10):
#   print(i, end=' ')

# from typing import List

# # #List comprhension to generator:
# # squared_nums = [y * y for y in [1,2,3,4,5]]
# squared_nums= (y * y for y in [1,2,3,4,5])
# print(squared_nums)
# print(next(squared_nums))
# print(next(squared_nums))
# print(next(squared_nums))
# print(next(squared_nums))
# print(next(squared_nums))

# def add_one(number):
#     return number + 1

# # function returns values based on the given arguments
# print( add_one(2))
# print( add_one(12))
# print( add_one(0))
# print( add_one(-9))

# def say_hello(name):
#     return f"Hello {name}"

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# a = greet_bob(say_hello)
# print(a)

# b = greet_bob(be_awesome)
# print(b)

# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# parent()

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child

# first = parent(1)
# print (first())

# def my_decorator(func):     
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)

# say_whee()


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee():
#     print("Whee!")

# @my_decorator
# def say_whee2():
#     print("Whee! Whee!")

# say_whee2()

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# waste_some_time(1)
waste_some_time(10000)