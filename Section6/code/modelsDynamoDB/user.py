__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'


# import sqlite3
# import psycopg2
# from sqlAlchemy import db
import boto3
import decimal



# psycopg2global dbConnectString = "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'"


# try:
#     connection = psycopg2.connect( dbConnectString )
#         # "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
# except:
#     print ("I am unable to connect to the database")



class UserModelDynamoDB():

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        import boto3
        from boto3.dynamodb.conditions import Key, Attr

        # Get the service resource.
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        userTable = dynamodb.Table('users')

        response = userTable.scan(
            FilterExpression=Attr('username').eq(username)
        )
        users = response['Items']
        user = None

        if len(users) != 0 :
            user = users[0]

        arg_id = int(user["id"])
        arg_userName = user["username"]
        arg_password = user["password"]

        userModel = UserModelDynamoDB(arg_id, arg_userName, arg_password)

        return userModel


    @classmethod
    def find_by_id(cls, _id):
        import boto3
        from boto3.dynamodb.conditions import Key, Attr

        # Get the service resource.
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        userTable = dynamodb.Table('users')

        response = userTable.scan(
            FilterExpression=Attr('id').eq(_id)
        )
        users = response['Items']
        user = None

        if len(users) != 0:
            user = users[0]

        arg_id = int(user["id"])
        arg_userName = user["username"]
        arg_password = user["password"]

        userModel = UserModelDynamoDB(arg_id, arg_userName, arg_password)

        return userModel
        # return user

        # connection = sqlite3.connect('sqlliteData.db')
        # cursor = connection.cursor()
        #
        # query_string = "SELECT * " \
        #                "FROM users " \
        #                "where id = %s"
        # result = cursor.execute(query_string, (_id,))   #  argument must by a tuple
        # rows = cursor.fetchall()
        # row = rows[0]
        # if row:
        #     # user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user


