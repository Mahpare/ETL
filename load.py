from pymongo import MongoClient
import pandas as pd

class LoadMongoDB:
    def __init__(self, user, password, host, db_name, port='27017', authSource='admin'):
        self.user= user
        self.password= password
        self.host= host
        self.port= port
        self.db_name = db_name
        self.authSource = authSource
        self.uri = 'mongodb://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.db_name + '?authSource=' + self.authSource

        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print("Mongo DB is created!")
        except Exception as e:
            print("Connection Unsuccessful!! ERROR!!'")
            print(str(e))

    # Function to insert data in DB, could handle Python dictionary and Pandas dataframes
    def insert_into_db(self,data,collection):
        if isinstance(data, pd.DataFrame):
            try:
                self.db[collection].insert_many(data.to_dict('records'))
            except Exception as e:
                print("insertion error")
                print(e)
        else:
            try:
                self.db[collection].insert_many(data)
            except Exception as e:
                print("insertion error")
                print(e)

    def read_from_db(self,collection):
        try:
            df = pd.DataFrame(self.db[collection].find())
            print("read data")
            return df
        except Exception as e:
            print(e)



