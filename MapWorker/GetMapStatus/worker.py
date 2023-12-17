import requests
import logging
import tempfile
from datetime import datetime
# Important libraries


class Worker:

    def __init__(self):
        self.row = None
        self.read_config()

    def read_config(self):
        try:
            dir_path = tempfile.gettempdir()
            file = dir_path + "\key.txt"
            with open(file, "r") as r:
                row = r.readline()
                self.row = "jumpo"
                logging.info(str(row))
        except FileNotFoundError as ex:
            logging.error(ex)

    def get_row(self):
        return self.row