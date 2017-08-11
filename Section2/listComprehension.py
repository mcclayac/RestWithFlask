__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/10/17'
__revision__ = '$'
__revision_date__ = '$'


my_list = [0,1,2,3,4]

an_equal_list = [x for x in range(5)]  # list [0.1.2.3.4]

print(my_list)
print(an_equal_list)

multiple_list = [x * 3 for x in range(5)]
print(multiple_list)


print(8 % 3)
even_list = [n for n in range(20) if n % 2 == 0]
print(even_list)

people_you_know = ["Rolf", "John","Anna", "GREG"]
normalized_people = [person.strip().lower() for person in people_you_know]

print(normalized_people)
