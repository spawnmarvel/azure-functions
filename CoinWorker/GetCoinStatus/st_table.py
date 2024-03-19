
# https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme?view=azure-python
# https://github.com/Azure-Samples/storage-table-python-getting-started/blob/master/table_basic_samples.py#L57
#  Not same as for queue...

import logging
import uuid
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableServiceClient, TableClient
from azure.core.credentials import AzureNamedKeyCredential

from GetCoinStatus.st_key_vault import KeyVaultWorker

class StorageTable():

    def __init__(self):
        self.table_service_client = None
        self.table_client = None
        self.key = None
        self.acc_name = None
        self.acc_url = None
        self.keyvaultInstance = KeyVaultWorker()
        

    def get_key_tbl(self):
        logging.info("Azure Table storage, get key tbl")
        self.key = self.keyvaultInstance.get_secret_tbl()
    
    def get_name_st(self):
        logging.info("Azure Table storage, get name st")
        self.acc_name = self.keyvaultInstance.get_name_acc()

    def get_url_st(self):
        logging.info("Azure Table storage, url st")
        self.acc_url = self.keyvaultInstance.get_url_tbl()

    def connect_table(self):
        self.get_key_tbl()
        self.get_name_st()
        self.get_url_st()
        logging.info("Azure Table storage, trying to connect to table storage")
        try:
            # Quickstart code goes here
            default_credential = AzureNamedKeyCredential(self.acc_name, self.key)
            self.table_service_client = TableServiceClient(self.acc_url, credential=default_credential)
            # https://learn.microsoft.com/en-us/python/api/azure-data-tables/azure.data.tables.tableserviceclient?view=azure-python
            logging.info("Azure Table storage, connection success")
        except Exception as ex:
            logging.error(ex)
        return self.table_service_client

    def create_tabel(self):
        self.connect_table()
        logging.info("Azure Table storage, trying to create table")
        found = False
        try:
            new_table_name = "cointable01" 
            all_tables = self.table_service_client.list_tables()
            logging.info("All tables; " + str(all_tables))
            for table in all_tables:
                logging.info(table.name)
                if table.name == new_table_name:
                    logging.info(str(table.name) + " already exists")
                    found = True
                    break
            if not found:
                table_client = self.table_service_client.create_table(table_name=new_table_name)
                logging.info("Azure Table storage, success created table")
        except Exception as ex:
            logging.error(ex)

    def insert_entity(self, name, description, value):
        # https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme?view=azure-python#creating-entities
        self.connect_table()
        logging.info("Trying to insert to table")
        try:
            new_table_name = "cointable01"
            row_key = str(uuid.uuid4())
            my_entity = {
                 u'PartitionKey': name,
                 u'RowKey': row_key,
                 u'Description': description,
                 u'LastValue': value,

            }
            table_service_client = self.table_service_client
            table_client = table_service_client.get_table_client(table_name=new_table_name)
            enity = table_client.create_entity(entity=my_entity)
            logging.info("Success insert to table")
        except Exception as ex:
            logging.error(ex)

    def list_entities(self):
        self.connect_table()
        try:
            entities = list(self.table_service_client.list_tables())
            logging.info(str(entities))
            logging.info("Listing Azure Table storage")
        except Exception as ex:
            logging.error(ex)
