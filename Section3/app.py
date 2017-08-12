__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/12/17'
__revision__ = '$'
__revision_date__ = '$'


from flask import Flask

store = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# stores = [{
#     'name': 'My Store',
#     'items': [{'name':'my item', 'price': 15.99 }]
# }]


app = Flask(__name__)
#
# @app.route('/')   # 'http://www.google/'
# def home():
#     return "Hell, World"

# POST - used to recieve data
# GET - Used to send data back only


# POST /store: {name:}
@app.route('/store', methods=['POST'])
def create_store(storeName):
    pass

# GET /store/<string:name>
@app.route('/store/<sring:name>', methods=['GET'])
def store_details(name):
    pass


# GET /store
@app.route('/store', methods=['GET'])
def get_stores(storeName):
    pass


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    pass


app.run(port=5000)


