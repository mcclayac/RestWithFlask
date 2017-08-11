


my_set = {1, 3, 5}
my_dic = {'name':'Tony','age':30, 'grades':[88,95,78]}
another_dic = {1:15, 2:75, 3:150}


lottery_player = {
    'name':'Tony',
    'numbers':(13,45,66,23,22)
}

universities = [
    {
        'name':'Oxford',
        'location':'uk'
    },
    {
        'name':'MIT',
        'location':'US'
    }
]

another_dic_in_dic = {
    'key': {
        'name':'Tony'
    }
}

sumNumbers = sum(lottery_player['numbers'])
print(sumNumbers)

lottery_player['name'] = 'Yosabelle'
