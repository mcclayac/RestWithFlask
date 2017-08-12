


def my_method(arg1, arg2):
    return arg1 + arg2


def my_list_addition(list_arg):
    return sum(list_arg)


myList = [5, 8, 9]

# print(my_list_addition(myList))


def my_long_method(*args):
    return sum(args)


# print(my_long_method(3, 5, 7, 9,33))
# print(my_long_method(3, 5, 7, 9,33,55,77,88,99))



def what_arekwargs(*args, **kwargs):
    print(args)
    print(kwargs)

def what_arekwargs2(name, location):
    print(name)
    print(location)



what_arekwargs(12, 34, 56, name='Tony', location="UK")

what_arekwargs2(location='UK', name='Lisa')

