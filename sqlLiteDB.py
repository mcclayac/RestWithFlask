

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# create_table = "CREATE TABLE users(" \
#                "id int," \
#                "username text," \
#                "password text)"
#
# cursor.execute(create_table)


# user = (1, 'jose', 'abcd')
# user = (2, 'tony', 'javajava')
insert_query = "INSERT INTO users VALUES (?,?,?)"
# cursor.execute(insert_query, user)

# users = [
#     (3, 'kim', 'javajava'),
#     (4, 'lisa', 'javajava'),
#     (5, 'tom', 'javajava'),
#     (6, 'tyanne', 'javajava'),
#     (7, 'yosabelle', 'javajava')
# ]
# cursor.executemany(insert_query, users)



select_query = " select * from users"
for row in cursor.execute(select_query):
    print(row)
    print(row[0])
    print(row[1])
    print(row[2])




connection.commit()
connection.close()





