__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/12/17'
__revision__ = '$'
__revision_date__ = '$'


def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

# print(methodception(add_two_numbers))

# print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 484, 88, 31, 55, 44]

new_list = list(filter(lambda x: x != 13, my_list))
print(new_list)

def not_thirteen(x):
    return x != 13

new_list = list(filter(not_thirteen, my_list))
print('-- not thirteen function ---- ')
print(new_list)



new_list = list(filter(lambda x: x % 2 == 0, my_list))
print('---- Even List ------')
print(new_list)


new_list = list(filter(lambda x: x % 2 == 1, my_list))
print('---- Odd List ------')
print(new_list)


value1 = (lambda x: x * 3)(5)
def f(x):
    return x * 3

value2 = f(5)

print('----------------------------------')
print(value1)
print(value2)

print([x for x in my_list if x != 13])
print('-------- Even List --------')
print([x for x in my_list if x % 2 == 0])

print('-------- Odd List --------')
print([x for x in my_list if x % 2 == 1])



