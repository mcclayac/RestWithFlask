__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'



import psycopg2
from sqlAlchemy import db
import boto3
import decimal



# dbConnectString = "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'"

90

class ItemModelTony():
    def __init__(self, uID, name, price):
        self.name = name
        self.price = price
        self.id = uID

    def setPrimaryKey(self):
        from random import randint

        primary_key = randint(1, 10000)
        self.id = primary_key


    def dynamoDBjson(self):
        sPrice = str(self.price)
        return {
            'id':self.id,
            'name':self.name,
            'price':decimal.Decimal(sPrice)
        }

    def json(self):
        fPrice = float(self.price)
        sID = int(self.id)
        return {
            'id':sID,
            'name':self.name,
            'price':fPrice
        }

    def setPrice(self, price):
        self.price = price

    def insert(self):
        import boto3
        import decimal

        # Get the service resource.
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        # Instantiate a table resource object without actually
        # creating a DynamoDB table. Note that the attributes of this table
        # are lazy-loaded: a request is not made nor are the attribute
        # values populated until the attributes
        # on the table resource are accessed or its load() method is called.
        itemTable = dynamodb.Table('items')

        print(itemTable.creation_date_time)

        creationDate = itemTable.creation_date_time


        self.setPrimaryKey()
        jsonItem = self.dynamoDBjson()

        itemTable.put_item(Item=jsonItem)

        jsonResult = self.json()

        return jsonResult


    def itemSave(self):
        import boto3
        import decimal

        # Get the service resource.
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        # Instantiate a table resource object without actually
        # creating a DynamoDB table. Note that the attributes of this table
        # are lazy-loaded: a request is not made nor are the attribute
        # values populated until the attributes
        # on the table resource are accessed or its load() method is called.
        itemTable = dynamodb.Table('items')

        print(itemTable.creation_date_time)

        creationDate = itemTable.creation_date_time

        jsonItem = self.dynamoDBjson()

        itemTable.put_item(Item=jsonItem)

        jsonResult = self.json()

        return jsonResult

    @classmethod
    def find_by_name(cls, itemName):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        # Instantiate a table resource object without actually
        # creating a DynamoDB table. Note that the attributes of this table
        # are lazy-loaded: a request is not made nor are the attribute
        # values populated until the attributes
        # on the table resource are accessed or its load() method is called.
        itemTable = dynamodb.Table('items')

        # itemName = self.name

        from boto3.dynamodb.conditions import Attr
        response = itemTable.scan(
            FilterExpression=Attr('name').eq(itemName)
        )
        items = list(response['Items'])

        if items:
            # print("Got something")
            item = items[0]
            name = item['name']
            _id = item['id']
            price = item['price']

            aItemModelTony = ItemModelTony(_id, name, price)
            return aItemModelTony
            # print('ID : {}  Name : {}  Price : {}'.format(_id, name, price))
        else:
            return None

    def itemDelete(self):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        itemTable = dynamodb.Table('items')

        itemTable.delete_item(
            Key={
                'id': self.id,
                'name': self.name
            }
        )







# Internal Representation
class ItemModelDynamoDB():
    def __int__(self, aUniqueID, name, price):
        self.name = name
        self.price = price
        self.id = aUniqueID

    # def __int__(self):
    #     self.name = ""
    #     self.price = 0
    #     self.id = 0

    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':float(self.price)
        }

    def set_id(self, _id):
        self.id = _id

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return float(self.price)

    def set_name(self, name):
        self.name = name

    def dyanmoInsert(self):

        import boto3
        import decimal

        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')

        # Instantiate a table resource object without actually
        # creating a DynamoDB table. Note that the attributes of this table
        # are lazy-loaded: a request is not made nor are the attribute
        # values populated until the attributes
        # on the table resource are accessed or its load() method is called.
        itemTable = dynamodb.Table('items')

        from random import randint

        primary_key = randint(1, 10000)
        jsonItem = self.json()

        itemTable.put_item(Item=jsonItem)

        return jsonItem



    @classmethod
    def find_by_name(cls, name):
        global dbConnectString
        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")
        cursor = connection.cursor()

        select_sql = "SELECT * FROM items where name = %s;"
        result = cursor.execute(select_sql, (name,))
        rows = cursor.fetchall()
        connection.close()
        # if rows:
        #     row = rows[0]
        #     # item = ItemModel()
        #     item.set_name(row[1])
        #     item.set_id(row[0])
        #     item.set_price(row[2])
        #     return item
        # else:
        return None



    def insert(self):
        global dbConnectString
        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        # connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        # insert_sql = "INSERT INTO items VALUES (null, %s, %s )"
        insert_sql = "INSERT INTO items (name,price) VALUES(%s,%s);"

        local_name = self.name
        local_price = self.price

        cursor.execute(insert_sql, (local_name, local_price))

        connection.commit()
        connection.close()


    def insertItem(self):
        global dbConnectString
        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")

        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()
        insert_sql = "INSERT into items (name, price) values (%s, %s);"

        str_name = self.name
        float_price = float(self.price)

        # cursor.execute(insert_sql, ('duck', 12.33))
        cursor.execute(insert_sql, (str_name, float_price))
        connection.commit()

        # item = ItemModel.find_by_name(self.name)
        connection.close()
        # return item
        return None


    def updateItem(self):
        global dbConnectString

        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()

        str_name = self.name
        float_price = self.get_price()

        update_sql = "UPDATE items SET name = %s, price = %s WHERE name = %s;"
        cursor.execute(update_sql, (str_name, float_price, str_name))
        connection.commit()
        # item = ItemModel.find_by_name(self.name)
        item = None
        connection.close()
        return item

