
# https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme?view=azure-python
# https://github.com/Azure-Samples/storage-table-python-getting-started/blob/master/table_basic_samples.py#L57
#  Not same as for queue...

import logging
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableServiceClient, TableClient
from GetMapStatus.env import API_CONNECTION

class StorageTable():

    def __init__(self):
        self.table_service_client = None
        self.table_client = None

    def read_config(self):
        self.row =  API_CONNECTION

    def connect_table(self):
        try:
            logging.info("Azure Table storage, trying to table")
            # Quickstart code goes here
            account_url = "https://stacukgetcoinstatus.table.core.windows.net"
            default_credential = DefaultAzureCredential()
            self.table_service_client = TableServiceClient(account_url, credential=default_credential)
            # https://learn.microsoft.com/en-us/python/api/azure-data-tables/azure.data.tables.tableserviceclient?view=azure-python
            self.table_client = TableClient(account_url, "cointable", default_credential)
            logging.info("Azure Table storage, connection success")
        except Exception as ex:
            logging.error(ex)
        return self.queue_client
    
    def list_entities(self):
        self.connect_table()
        try:
            entities = list(self.table_client.list_entities)
            logging.info(str(entities))
            logging.info("Listing Azure Table storage")
        except Exception as ex:
            logging.error(ex)
