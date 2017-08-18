__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'


import sqlite3
import psycopg2
from sqlAlchemy import db


# psycopg2global dbConnectString = "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'"


try:
    connection = psycopg2.connect( dbConnectString )
        # "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
except:
    print ("I am unable to connect to the database")



class UserModelSQLAlchemy(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('sqlliteData.db')
        global dbConnectString
        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
            print("pycopq2 : Connected")

        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()

        query_string = "SELECT * FROM users where username =%s"
        cursor.execute(query_string, (username,))   #  argument must by a tuple
        rows = cursor.fetchall()
        if rows:
            row = rows[0]
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


    @classmethod
    def find_by_id(cls, _id):
        global dbConnectString
        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        # connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        query_string = "SELECT * " \
                       "FROM users " \
                       "where id = %s"
        result = cursor.execute(query_string, (_id,))   #  argument must by a tuple
        rows = cursor.fetchall()
        row = rows[0]
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


