
lotter_player_dict = {
    'name':'Rolf',
    'numbers':(5,9,12,3,1,21)
}


class lotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)


# player_one = lotteryPlayer('Rolf')
# player_two = lotteryPlayer('Tony')
#
# player_one.numbers = (1,2,3,6,7,8)
#
# print(player_one.name)
# print(player_two.name)

# print(player_one.numbers)
# print(player_one.total())

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        print('I am going to school')
        print('I am a {}'.format(cls))

    @staticmethod
    def walking_home():
        print("I Am walking home")


        # {} .'.format(self.school))


anna = Student('Anna', 'MIT')
rolf = Student('Rolf', 'Oxford')
anna.go_to_school()
rolf.go_to_school()

anna.walking_home()
rolf.walking_home()

Student.go_to_school()
Student.walking_home()

# anna.marks.append(56)
# anna.marks.append(71)
# print(anna.marks)
# print(anna.average())

class store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name':name, 'price':price}
        self.items.append(item)


    def stock_price(self):
        # Metod should add up each item in price and return the total
        total = sum([item['price'] for item in self.items])
        return total

        # total = 0;
        # for item in self.items:
        #     total += item['price']
        # return total

# wallyWorld = store('WallWorld')
# wallyWorld.add_item('bike', 123)
# wallyWorld.add_item('bed', 56)
# print(wallyWorld.stock_price())

