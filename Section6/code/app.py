__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/12/17'
__revision__ = '$'
__revision_date__ = '$'


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import boto3


# Security
from security import authenticate, identity

# Postgrsql Resources
from resources.user import  UserRegister
from resources.item import Item, Items

#  dynamoDB Resources
from resourcesDynamoDB.user import UserRegisterDynamoDB
from resourcesDynamoDB.item import ItemDynamoDB, ItemsDynamoDB


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'MySecretKey'

api = Api(app)

jwt = JWT(app, authenticate, identity)  # /Auth

# Postgrsql SQL
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

# DynamoDB Resoures
api.add_resource(ItemDynamoDB, '/itemDynamoDB/<string:name>')
api.add_resource(ItemsDynamoDB, '/itemsDynamoDB')
api.add_resource(UserRegisterDynamoDB, '/registerDynamoDB')


if __name__ == '__main__':
    from sqlAlchemy import db   #  SQL Alchemy Boot strap
    db.init_app(app)            #  SQL Alchemy Boot strap
    app.run(port=5000, debug=True)





