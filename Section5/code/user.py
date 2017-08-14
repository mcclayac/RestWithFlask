__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/13/17'
__revision__ = '$'
__revision_date__ = '$'



import sqlite3
from flask_restful import Resource
from flask_restful import reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        query_string = "SELECT * " \
                       "FROM users " \
                       "where username = ?"
        result = cursor.execute(query_string, (username,))   #  argument must by a tuple
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        query_string = "SELECT * " \
                       "FROM users " \
                       "where id = ?"
        result = cursor.execute(query_string, (_id,))   #  argument must by a tuple
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User '{}' already exists".format(data['username'])}, 400

        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        insert_sql = "INSERT INTO users VALUES (NULL, ? ,?)"
        cursor.execute(insert_sql, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message":"User created successfully"}, 201




















