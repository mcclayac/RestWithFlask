__author__ = 'anthonymcclay'
__project__ = 'RestWithFlask'
__date__ = '8/14/17'
__revision__ = '$'
__revision_date__ = '$'



import psycopg2

# Internal Representation
class ItemModel:
    def __int__(self):
        self.name = ""
        self.price = 0
        self.id = 0

    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':float(self.price)
        }

    def set_id(self, _id):
        self.id = _id

    def set_price(self, price):
        self.price = price

    def set_name(self, name):
        self.name = name

    @classmethod
    def find_by_name(cls, name):
        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")
        cursor = connection.cursor()

        select_sql = "SELECT * FROM items where name = %s;"
        result = cursor.execute(select_sql, (name,))
        rows = cursor.fetchall()
        connection.close()
        if rows:
            row = rows[0]
            item = ItemModel()
            item.set_name(row[1])
            item.set_id(row[0])
            item.set_price(row[2])
            return item
        else:
            return None



    def insert(self):
        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        # connection = sqlite3.connect('sqlliteData.db')
        cursor = connection.cursor()

        # insert_sql = "INSERT INTO items VALUES (null, %s, %s )"
        insert_sql = "INSERT INTO items (name,price) VALUES(%s,%s);"

        local_name = self.name
        local_price = self.price

        cursor.execute(insert_sql, (local_name, local_price))

        connection.commit()
        connection.close()


    def insertItem(self):
        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()
        insert_sql = "INSERT into items (name, price) values (%s, %s)"
        cursor.execute(insert_sql, (self.name, self.price))
        connection.commit()

        item = ItemModel.find_by_name(self.name)
        connection.close()
        return item


    def updateItem(self):

        try:
            connection = psycopg2.connect(
                "dbname='restfulAPIFlask' user='restfulapi' host='localhost' password='11javajava'")
        except:
            print("I am unable to connect to the database")

        cursor = connection.cursor()
        update_sql = "UPDATE items SET name = %s, price = %s WHERE name = %s"
        cursor.execute(update_sql, (self.name, self.price, self.name))
        connection.commit()
        item = ItemModel.find_by_name(self.name)
        connection.close()
        return item

