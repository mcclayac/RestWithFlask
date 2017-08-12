__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/12/17'
__revision__ = '$'
__revision_date__ = '$'


import functools
import time

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function")

# my_function()


def timer(func):
    @functools.wraps(func)
    def timer_func():
        start = time.time()
        print("Start Timer : " + str(start))
        func()
        end = time.time()
        print("End Timer : " + str(end))
        print("Elapse Time : " + str((end - start)))
    return timer_func

@timer
def my_long_function():
    print("I wonder how Long ?")


# my_long_function()

#############

#
# def decorator_with_arguements(number):
#     def my_decorator(func):
#         @functools.wraps(func)
#         def function_that_runs_func(num):
#             print("In the decorator " + str(number))
#             func(num)
#             print("after the decorator " + str(number))
#         return function_that_runs_func
#     return my_decorator



def decorator_with_arguements(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator " + str(number))
            func(*args, **kwargs)
            print("after the decorator " + str(number))
        return function_that_runs_func
    return my_decorator


@decorator_with_arguements(56)
def my_Function_too(num, num2):
    print("Hell - my fucntion_too " + str(num) + " " + str(num2))

my_Function_too(44, 33)



