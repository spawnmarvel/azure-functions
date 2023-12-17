import requests
import logging
import tempfile
from datetime import datetime
# Important libraries
from GetMapStatus.env import API_CONNECTION


class Worker:

    def __init__(self):
        self.row = None
        self.read_config()

    def read_config(self):
        self.row =  API_CONNECTION
       

    def get_row(self):
        return self.row