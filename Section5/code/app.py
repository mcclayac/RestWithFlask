__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/12/17'
__revision__ = '$'
__revision_date__ = '$'


from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from Section4.code.security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'MySecretKey'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /Auth


items = []

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
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # return({'item':None}, 404)

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # request_data = request.get_json()
        request_data = Item.parser.parse_args()

        item = {
            'name':name,
            'price':request_data['price']
        }
        items.append(item)
        return item, 201

    # @jwt_required()
    def delete(self, name):
        global items
        new_items_list = list(filter(lambda x: x['name'] != name, items))
        items = new_items_list
        return {'message':'item deleted'}

    # @jwt_required()
    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        # request_data = request.get_json()
        request_data = Item.parser.parse_args()

        if item is None:
            item = {
                'name': name,
                'price': request_data['price']
            }
            items.append(item)
        else:
            item.update(request_data)  # changes the data only if it matches 'price'
            # item['price'] = request_data['price']
            # return item, 201
        return (item), 201




class Items(Resource):
    def get(self):
        return ({'items': items})


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')


# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
#
# api.add_resource(Student, '/student/<string:name>')
#   http://127.0.0.1:5000/student/Tony

app.run(port=5000, debug=True)




