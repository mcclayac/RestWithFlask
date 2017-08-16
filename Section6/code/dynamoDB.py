


import boto3
import decimal

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

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


from random import randint

primary_key = randint(1, 10000)

s = str(56.88)

itemTable.put_item(
   Item={
        'id': primary_key,
        'name': 'sink',
       'price': decimal.Decimal(s)
    }
)

