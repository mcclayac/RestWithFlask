__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/12/17'
__revision__ = '$'
__revision_date__ = '$'


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import  UserRegister
from resources.item import Item, Items


app = Flask(__name__)
app.secret_key = 'MySecretKey'

api = Api(app)

jwt = JWT(app, authenticate, identity)  # /Auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)





