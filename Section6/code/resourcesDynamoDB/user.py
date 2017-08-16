__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/13/17'
__revision__ = '$'
__revision_date__ = '$'



import sqlite3
from flask_restful import Resource
from flask_restful import reqparse
from models.user import UserModel
import psycopg2


class UserRegisterDynamoDB(Resource):
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

        if UserModel.find_by_username(data['username']):
            return {"message": "User '{}' already exists".format(data['username'])}, 400

        # connection = sqlite3.connect('sqlliteData.db')

        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")
        cursor = connection.cursor()

        insert_sql = "INSERT INTO users (username, password) VALUES ( %s ,%s)"
        cursor.execute(insert_sql, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message":"User created successfully"}, 201




















