import requests
import logging
import tempfile
from datetime import datetime
# Important libraries
from GetMapStatus.env import API_CONNECTION
from GetMapStatus.st_table import StorageTable


class Worker:

    def __init__(self):
        self.row = None
        self.read_config()

    def read_config(self):
        self.row =  API_CONNECTION
       

    def get_row(self):
        return self.row
    
    def get_all(self):
        stats = {}
        stats["Api version"] = "1.0"
        try:
            county = "https://ws.geonorge.no/kommuneinfo/v1/fylker"
            rv = requests.get(county, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            stats["Status Code"] = rv.status_code
        except Exception as ex:
            logging.error(ex)
        return stats