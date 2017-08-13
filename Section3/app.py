__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/12/17'
# anna = WorkingStudent("Anna", "Oxford", 20.00)
# kim = anna.friend("kim","Oxfor")

__revision__ = '$'
__revision_date__ = '$'


from flask import Flask, jsonify, request, render_template

stores = [
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


@app.route('/')
def home():
    return render_template('index.html')


# POST /store: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)



# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def store_details(name):
    # return jsonify({'store' : stores[name]})
    # Iterate over stores
    # if store  name matches, return it
    # if non match, return an erro message
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message' : 'Error: No stores match'})


# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores' : stores})


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if (store['name'] == name):
            request_data = request.get_json()
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message' : 'Store not found'})



# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    for store in stores:
        if (store['name'] == name):
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Error: No stores/items match'})


app.run(port=5000)


