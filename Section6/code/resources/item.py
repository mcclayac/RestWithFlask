__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'


from flask_restful import Resource, reqparse
from flask_jwt import  jwt_required
import sqlite3


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
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        select_sql = "SELECT * FROM items where name = ?"
        result = cursor.execute(select_sql, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"item": {"id": row[0], "name": row[1], "price": row[2]}}



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
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        insert_sql = "INSERT INTO items VALUES (null, ?, ? )"
        result = cursor.execute(insert_sql, (item['name'], item['price']))

        connection.commit()
        connection.close()

    # @jwt_required()
    def delete(self, name):
        item = self.find_by_name(name)
        if item is None:
            return {"message": "item '{}' does not exisits".format(name)}, 400
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()
        delete_sql = "DELETE from items where items.name = ?"
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
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()
        insert_sql = "INSERT into items (id, name, price) values (null, ?, ?)"
        cursor.execute(insert_sql, (item['name'],item['price']))
        connection.commit()

        item = Item.find_by_name(item['name'])
        connection.close()
        return item

    @classmethod
    def updateItem(cls, item):
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()
        update_sql = "UPDATE items SET name = ?, price = ? WHERE name = ?"
        cursor.execute(update_sql, (item['name'], item['price'], item['name']))
        connection.commit()
        item = Item.find_by_name(item['name'])
        connection.close()
        return item


class Items(Resource):
    def get(self):
        connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()
        select_sql = "select * from items"
        result = cursor.execute(select_sql)
        items = []
        for row in result:
            items.append({"id": row[0], "name":row[1],"price":row[2]})

        connection.close()
        return {"items": items }


