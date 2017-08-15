__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'




import sqlite3
import psycopg2

try:
    connection = psycopg2.connect("dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
except:
    print ("I am unable to connect to the database")


# connection = sqlite3.connect('sqlliteData.db')
cursor = connection.cursor()

create_user_table = \
    "CREATE TABLE IF NOT EXISTS users (" \
    "   id INTEGER PRIMARY KEY, " \
    "   username text, " \
    "   password text " \
    ")"
cursor.execute(create_user_table)


create_item_table = \
    "CREATE TABLE IF NOT EXISTS items (" \
    "  id INTEGER PRIMARY KEY, " \
    "  name text, " \
    "  price real " \
    ")"
cursor.execute(create_item_table)

insert_item_sql = \
    "INSERT INTO items values (NULL, 'test', 10.99)"
cursor.execute(insert_item_sql)




connection.commit()
connection.close()


