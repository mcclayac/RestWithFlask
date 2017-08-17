


import boto3
import decimal


# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
itemTable = dynamodb.Table('items')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
# print(itemTable.creation_date_time)


# from random import randint
#
# primary_key = randint(1, 10000)
#
# s = str(56.88)
#
# itemTable.put_item(
#    Item={
#         'id': primary_key,
#         'name': 'sink',
#        'price': decimal.Decimal(s)
#     }
# )

#
# dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
# itemTable = dynamodb.Table('items')
# from boto3.dynamodb.conditions import Attr
# response = itemTable.scan(
#     # FilterExpression=Attr('name').eq('bed')
# )
# items = list(response['Items'])
#
# for item in items:
#     name = item['name']
#     _id = item['id']
#     price = item['price']
#     print('ID : {}  Name : {}  Price : {}'.format(_id, name, price))
#


# if items:
#     print("Got something")
#     item = items[0]
#     name = item['name']
#     _id = item['id']
#     price = item['price']
#     print('ID : {}  Name : {}  Price : {}'.format(_id, name, price))
# else:
#     print('Got nothing')
#
# print('-----------------------')
# print(items)

# dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
# itemTable = dynamodb.Table('items')
#
# aDec = decimal.Decimal(99.88)
# itemTable.update_item(
#     Key={
#         'id': 2,
#         'name': 'chair'
#     },
#     UpdateExpression='SET price = :val1',
#     ExpressionAttributeValues={
#         ':val1': aDec
#     }
# )


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
itemTable = dynamodb.Table('items')
from boto3.dynamodb.conditions import Attr

item = itemTable.get_item(
    partition_key='2',
    sort_key='chair'
)
item['price'] = decimal.Decimal(99.99)

#
# response = itemTable.scan(
#     # FilterExpression=Attr('name').eq('chair')
# )
# items = list(response['Items'])
#
# for item in items:
#     name = item['name']
#     _id = item['id']
#     price = item['price']
#     print('ID : {}  Name : {}  Price : {}'.format(_id, name, price))
# #