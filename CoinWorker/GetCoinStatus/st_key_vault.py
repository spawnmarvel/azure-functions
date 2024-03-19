import os
import uuid
import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class KeyVaultWorker:

    def __init__(self):
        self.secret_client = None
        self.url = "https://keyvault001x01.vault.azure.net/"

    def get_secret_tbl(self):
        get_key = None
        logging.info("Azure Key vault, trying to connect")
        try:
            # Quickstart code goes here
            credential = DefaultAzureCredential()
            self.secret_client = SecretClient(vault_url=self.url, credential=credential)
            get_key = self.secret_client.get_secret("coin-tbl")
            logging.info("Azure Key vault get success, tbl")
        except Exception as ex:
            logging.error(ex)
        return get_key.value
    
    def get_name_acc(self):
        get_key = None
        logging.info("Azure Key vault, trying to connect")
        try:
            # Quickstart code goes here
            credential = DefaultAzureCredential()
            self.secret_client = SecretClient(vault_url=self.url, credential=credential)
            get_key = self.secret_client.get_secret("coin-acc")
            logging.info("Azure Key vault get success, acc")
        except Exception as ex:
            logging.error(ex)
        return get_key.value
    

    def get_url_tbl(self):
        get_key = None
        logging.info("Azure Key vault, trying to connect")
        try:
            # Quickstart code goes here
            credential = DefaultAzureCredential()
            self.secret_client = SecretClient(vault_url=self.url, credential=credential)
            get_key = self.secret_client.get_secret("coin-url-tbl")
            logging.info("Azure Key vault get success, url tbl")
        except Exception as ex:
            logging.error(ex)
        return get_key.value
    
    def get_url_qu(self):
        get_key = None
        logging.info("Azure Key vault, trying to connect")
        try:
            # Quickstart code goes here
            credential = DefaultAzureCredential()
            self.secret_client = SecretClient(vault_url=self.url, credential=credential)
            get_key = self.secret_client.get_secret("coin-url-qu")
            logging.info("Azure Key vault get success, url qu")
        except Exception as ex:
            logging.error(ex)
        return get_key.value