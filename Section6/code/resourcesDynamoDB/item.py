__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'


from flask_restful import Resource, reqparse
from flask_jwt import  jwt_required
import sqlite3
import psycopg2
from models.item import ItemModel

import boto3

# Dynamo DB Models
from modelsDynamoDB.item import ItemModelDynamoDB, ItemModelTony






class ItemDynamoDB(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="price - connot be left blank")

    # ensure that only 'price' is passe dthrough in the json payload
    # ensure that the type is a float
    # make sure it is required


    @jwt_required()
    def get(self, name):


        item = ItemModelTony.find_by_name(name)
        if item:
            return item.json()
        return {"message" : "item '{}' does not exisit".format(name)}, 404



    @jwt_required()
    def post(self, name):

        #  check is already exists
        # item = ItemModel.find_by_name(name)
        # if item:
        #     return {"message": "item '{}' already exisits".format(name)}, 400

        # item0 = ItemModel()
        # item1 = ItemModel('tony', 13.99)
        #

        # Parse the data from the Resource
        request_data = ItemDynamoDB.parser.parse_args()

        itemTony = ItemModelTony(0,name,request_data['price'] )
        itemJson = itemTony.insert()

        return itemJson



        # if next(filter(lambda x: x['name'] == name, items), None) is not None:
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # request_data = request.get_json()
        request_data = ItemDynamoDB.parser.parse_args()

        item2 = ItemModel()
        item2.set_name(name)
        item2.set_price(request_data['price'])

        try:
            item2 = item2.insertItem()
        except:
            return {"message":"An Errr occurrred inserting the item."}, 500   # internal server error

        instanceOfType = type(item2)
        # item = self.find_by_name(name)
        print(type(item2))


        return item2.json() , 201



    @jwt_required()
    def delete(self, name):
        item = ItemModelTony.find_by_name(name)
        if item is None:
            return {"message": "item '{}' does not exisits".format(name)}, 400

        item.itemDelete()
        return {"message" : "{} has been deleted".format(name)}



    @jwt_required()
    def put(self, name):


        item = ItemModelTony.find_by_name(name)
        if item is None:
            return {"message" : "item '{}' does not exisit".format(name)}, 404

        request_data = ItemDynamoDB.parser.parse_args()
        item.setPrice(request_data['price'])

        json = item.itemSave()

        return json




class ItemsDynamoDB(Resource):
    def get(self):

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        itemTable = dynamodb.Table('items')
        from boto3.dynamodb.conditions import Attr
        response = itemTable.scan(
            # FilterExpression=Attr('name').eq('bed')
        )
        items = list(response['Items'])

        ItemModelTonyList = []
        jsonResponse = []


        for item in items:
            name = item['name']
            _id = item['id']
            price = item['price']
            print('ID : {}  Name : {}  Price : {}'.format(_id, name, price))
            aItemModelTony = ItemModelTony(_id, name, price)
            ItemModelTonyList.append(aItemModelTony)
            jsonResponse.append(aItemModelTony.json())

        print(jsonResponse)
        return {"items" : jsonResponse }



        # try:
        #     connection = psycopg2.connect(
        #     "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        # except:
        #     print("I am unable to connect to the database")
        #
        # cursor = connection.cursor()
        # select_sql = "select * from items"
        # result = cursor.execute(select_sql)
        # rows = cursor.fetchall()
        # items = []
        # if rows:
        #     for row in rows:
        #         items.append({"id": row[0], "name":row[1],"price":float(row[2])})
        #
        # connection.close()
        # return {"items": items }


