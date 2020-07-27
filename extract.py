# a class that handles different data sources for extraction purpose.
# OOP’s methodology = keeping our code modular or loosely coupled.

import pandas as pd
import json
import requests

class Extract:
    def __init__(self):
        # opens file and returns A JSON object contains data in the form of key/value pair.
        self.datasource= json.load(open('dataSourceConfig.json'))
        self.api = self.datasource['data_sources']['api']
        self.csv_path= self.datasource['data_sources']['csv']

    def getApiData(self,api_name):
        api_url = self.api[api_name]
        api_data = requests.get(api_url)
        # response.json() will convert json data into Python dictionary.
        return api_data.json()

    def getCsvData(self,csv_name):
        csv_file =self.csv_path[csv_name]
        df= pd.read_csv(csv_file)
        return df



