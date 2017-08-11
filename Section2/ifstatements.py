__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/10/17'
__revision__ = '$'
__revision_date__ = '$'



# should_continue = True
# if should_continue:
#     print("Hello")
#
# known_people_python = ['John', 'Mary', 'Anna']
#
# person = input("Enter the person you know: ")
# if person in known_people_python:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))

# if person not in known_people_python:
#     print("You don't know this person")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Modify the method below to make sure only even numbers are returned.
# def even_numbers():
#     evens = []
#     for number in numbers:
#         if (number % 2 == 0 ):
#             evens.append(number)
#     return evens
#
# # print(even_numbers())
#
# if person == 'Tony':
#     print('Tony')
# elif person == 'Yosabelle':
#     print('Yosabelle')


## Exercise


def who_do_you_know():
    # ask the user for the people you know
    # Split the Sstring into a liist
    people = input("Type the people you know separated by , :")
    # people_list = people.split(',')
    # people_without_space = [person.strip().lower() for person in people_list]

    people_without_space = [person.strip().lower() for person in people.split(',')]

    return people_without_space
    #
    # people_without_space = []
    # for peep in people_list:
    #     people_without_space.append(peep.strip())
    # return people_without_space

def ask_user():
    #  Ask User for a name
    # See if their name is in the list of people they know
    # Print out they know the person

    person = input('Enter a Name :')
    people_list = who_do_you_know()
    print(people_list)

    if person.lower() in people_list:
        print("Yes you know {}!".format(person))
    else:
        print("No you don't know {}!".format(person))




# people_list = who_do_you_know()
ask_user()

