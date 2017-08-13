__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/13/17'
__revision__ = '$'
__revision_date__ = '$'


from Section4.code.user import User


users = [
    User(1, 'tony','pascal')
]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

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

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    user = userid_mapping.get(user_id, None)
    return user




