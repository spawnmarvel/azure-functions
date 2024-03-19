import os
import uuid
import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class KeyVaultWorker:

    def __init__(self):
        self.secret_client = None
        self.url = None

    def get_key(self):
        get_key = None
        logging.info("Azure Key vault, trying to connect")
        try:
            # Quickstart code goes here
            self.url = "https://keyvault001x01.vault.azure.net/"
            credential = DefaultAzureCredential()
            self.secret_client = SecretClient(vault_url=self.url, credential=credential)
            get_key = self.secret_client.get_secret("keyx01")
            logging.info("Azure Key vault get success")
        except Exception as ex:
            logging.error(ex)
        return get_key.value