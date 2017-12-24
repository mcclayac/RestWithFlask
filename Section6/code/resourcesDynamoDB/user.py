__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/13/17'
__revision__ = '$'
__revision_date__ = '$'



import sqlite3
from flask_restful import Resource
from flask_restful import reqparse
from modelsDynamoDB.user import UserModelDynamoDB
import psycopg2
from boto3.dynamodb.conditions import Key, Attr

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
        data = UserRegisterDynamoDB.parser.parse_args()

        if UserModelDynamoDB.find_by_username(data['username']):
            return {"message": "User '{}' already exists".format(data['username'])}, 400

        import boto3
        from boto3.dynamodb.conditions import Key, Attr

        # Get the service resource.
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        userTable = dynamodb.Table('users')

        import random
        number = random.randrange(0, 10000000)



        userTable.put_item(
            Item={
                'username': data['username'],
                'password': data['password'],
                'id': number,
            }
        )

        # connection = sqlite3.connect('sqlliteData.db')

        # try:
        #     connection = psycopg2.connect(
        #     "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        # except:
        #     print("I am unable to connect to the database")
        # cursor = connection.cursor()
        #
        # insert_sql = "INSERT INTO users (username, password) VALUES ( %s ,%s)"
        # cursor.execute(insert_sql, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()

        return {"message":"User created successfully"}, 201




















