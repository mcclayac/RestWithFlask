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

class Item(Resource):
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

        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message" : "item '{}' does not exisit".format(name)}, 404



    @jwt_required()
    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {"message": "item '{}' already exisits".format(name)}, 400

        # item0 = ItemModel()

        # item1 = ItemModel('tony', 13.99)




        # if next(filter(lambda x: x['name'] == name, items), None) is not None:
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # request_data = request.get_json()
        request_data = Item.parser.parse_args()

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
        item = ItemModel.find_by_name(name)
        if item is None:
            return {"message": "item '{}' does not exisits".format(name)}, 400
        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        # connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()
        delete_sql = "DELETE from items where items.name = %s"
        cursor.execute(delete_sql, (name, ))
        connection.commit()
        connection.close()
        return ({"message":"Item '{}' has been deleted".format(name)})

    @jwt_required()
    def put(self, name):

        item = ItemModel.find_by_name(name)
        request_data = Item.parser.parse_args()
        updated_item = ""
        updated_item = ItemModel()
        updated_item.set_name(name)
        updated_item.set_price(request_data['price'])

        if item is None:
            try :
                item = updated_item.insertItem()
            except:
                return {"message":"Error Inserting item '{}' ".format(name)}, 500
        else:
            try:
                item = updated_item.updateItem()
            except:
                return {"message":"error updating item '{}' ".format(name)}, 500

        return (item.json()), 201



class Items(Resource):
    def get(self):
        # connection = sqlite3.connect('sqlliteData.db')
        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()
        select_sql = "select * from items"
        result = cursor.execute(select_sql)
        rows = cursor.fetchall()
        items = []
        if rows:
            for row in rows:
                items.append({"id": row[0], "name":row[1],"price":float(row[2])})

        connection.close()
        return {"items": items }


