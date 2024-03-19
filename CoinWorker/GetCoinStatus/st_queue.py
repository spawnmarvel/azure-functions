import os
import uuid
import logging
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

from GetCoinStatus.st_key_vault import KeyVaultWorker

# https://learn.microsoft.com/en-us/azure/storage/queues/storage-python-how-to-use-queue-storage?tabs=python%2Cenvironment-variable-windows#overview

class StorageQueue:

    def __init__(self):
        self.queue_client = None
        self.acc_url = None
        self.keyvaultInstance = KeyVaultWorker()


    def get_url_st(self):
        logging.info("Azure Table storage, url qu")
        self.acc_url = self.keyvaultInstance.get_url_qu()

    def connect_queue(self):
        self.get_url_st()
        logging.info("Azure Queue storage, trying to connect")
        try:
            
            # Quickstart code goes here
            default_credential = DefaultAzureCredential()
            self.queue_client = QueueClient(
                self.acc_url, queue_name="coinqueue", credential=default_credential)
            logging.info("Azure Queue storage, connection success")
        except Exception as ex:
            logging.error(ex)
        return self.queue_client

    def send_msg(self, message):
        self.connect_queue()
        try:
            self.queue_client.send_message(message)
            logging.info("Sent msg to Azure Queue storage")
        except Exception as ex:
            logging.error(ex)
    
    def get_queue_length(self):
        self.connect_queue()
        try:
            properties = self.queue_client.get_queue_properties()
            count = properties.approximate_message_count
            logging.info("Get msg count Azure Queue storage")
        except Exception as ex:
            logging.error(ex)
        rv = str(count)
        return rv

    def read_msg(self):
        stats = []
        self.connect_queue()
        try:
            messages = self.queue_client.peek_messages()
            for peek_msg in messages:
                stats.append(peek_msg.content)
            logging.info("Reading msg from Azure Queue storage")
        except Exception as ex:
            logging.error(ex)
        return stats

    def receieve_msg(self):
        stats = []
        self.connect_queue()
        try:
            messages = self.queue_client.receive_messages()
            for peek_msg in messages:
                stats.append(peek_msg.content)
                # self.queue_client.delete_message(peek_msg.id, peek_msg.pop_receipt)
            logging.info("Reading msg from Azure Queue storage")
        except Exception as ex:
            logging.error(ex)
        return stats
