__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'


from flask_restful import Resource, reqparse
from flask_jwt import  jwt_required
import sqlite3
import psycopg2


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

        item = self.find_by_name(name)
        if item:
            return item
        return {"message" : "item '{}' does not exisit".format(name)}, 404

    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('sqlliteData.db')
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
        if rows:
            row = rows[0]
            return {"item": {"id": row[0], "name": row[1], "price": float(row[2])}}
        else:
            return None



    @jwt_required()
    def post(self, name):
        item = self.find_by_name(name)
        if item:
            return {"message": "item '{}' already exisits".format(name)}, 400


        # if next(filter(lambda x: x['name'] == name, items), None) is not None:
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # request_data = request.get_json()
        request_data = Item.parser.parse_args()
        item = {
            'name':name,
            'price':request_data['price']
        }
        try:
            self.insert(item)
        except:
            return {"message":"An Error occurrred inserting the item."}, 500   # internal server error

        # item = self.find_by_name(name)

        return item, 201

    @classmethod
    def insert(cls, item):
        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        # connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        # insert_sql = "INSERT INTO items VALUES (null, %s, %s )"
        insert_sql = "INSERT INTO items (name,price) VALUES(%s,%s);"

        local_name = item['name']
        local_price = item['price']

        # local_name = 'computer'
        # local_price = 99.99

        result = cursor.execute(insert_sql, (local_name, local_price))

        connection.commit()
        connection.close()

    # @jwt_required()
    def delete(self, name):
        item = self.find_by_name(name)
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

    # @jwt_required()
    def put(self, name):

        item = self.find_by_name(name)
        request_data = Item.parser.parse_args()
        updated_item = ""
        if item:
            updated_item = {

                'name': name,
                'price': request_data['price']
            }
        else:
            updated_item = {
                'name': name,
                'price': request_data['price']
            }

        if item is None:
            try :
                item = self.insertItem(updated_item)
            except:
                return {"message":"Error Inserting item '{}' ".format(name)}, 500
        else:
            try:
                item = self.updateItem(updated_item)
            except:
                return {"message":"error updating item '{}' ".format(name)}, 500

        return (item), 201

    @classmethod
    def insertItem(cls, item):
        # connection = sqlite3.connect('sqlliteData.db')
        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()
        insert_sql = "INSERT into items (name, price) values (%s, %s)"
        cursor.execute(insert_sql, (item['name'],item['price']))
        connection.commit()

        item = Item.find_by_name(item['name'])
        connection.close()
        return item

    @classmethod
    def updateItem(cls, item):
        # connection = sqlite3.connect('sqlliteData.db')
        try:
            connection = psycopg2.connect(
            "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()
        update_sql = "UPDATE items SET name = %s, price = %s WHERE name = %s"
        cursor.execute(update_sql, (item['name'], item['price'], item['name']))
        connection.commit()
        item = Item.find_by_name(item['name'])
        connection.close()
        return item


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


