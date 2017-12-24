__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/13/17'
__revision__ = '$'
__revision_date__ = '$'


from resources.user import UserModel
from resourcesDynamoDB.user import  UserModelDynamoDB


# users = [
#     User(1, 'tony','pascal')
# ]
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = UserModel.find_by_username(username)        # PostgrsqlDB User Model
    userDynamoDB = UserModelDynamoDB.find_by_username(username)  # aws Dynamo DB User Model
    # user = username_mapping.get(username, None)
    if userDynamoDB and userDynamoDB.password  == password:
        return userDynamoDB

def identity(payload):
    user_id = payload['identity']
    # user = UserModel.find_by_id(user_id)       # PostgrsqlDB User Model
    user = UserModelDynamoDB.find_by_id(user_id) # aws Dynamo DB User Model
    # user = userid_mapping.get(user_id, None)
    return user



# users = [
#     {
#         'id':1,
#         'name':'bob',
#         'password':'javajava'
#     }
# ]

# username_mapping = { 'bob': {
#     'id': 1,
#     'name': 'bob',
#     'password': 'javajava'
#     }
# }

# userid_mapping = { 1: {
#     'id': 1,
#     'name': 'bob',
#     'password': 'javajava'
#     }
# }
