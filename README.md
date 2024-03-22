# azure-functions
Testing and learning Azure functions

## Docs


Best practices for reliable Azure Functions

https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices?tabs=python


One of the key features of Azure Functions is its integration with other Azure services, such as Azure Storage.
When creating an Azure Functions App, a dedicated storage account is also created, the Functions App relies on the storage for various operations such as trigger management and logging.

https://learn.microsoft.com/en-us/azure/azure-functions/


## visuals

https://follow-e-lo.com/2023/12/12/azure-function-python/

## MS Learn Python Azure Functions samples

When creating a new functions here are the options:

* Azure Blob Storage trigger
* Azure Cosmos DB trigger
* Durable Functions activity
* Durable Functions entity
* Durable Functions HTTP starter
* Durable Functions orchestrator
* Azure Event Grid trigger
* Azure Event Hub trigger
* HTTP trigger
* Kafka output
* Kafka trigger
* Azure Queue Storage trigger
* RabbitMQ trigger
* Azure Service Bus Queue trigger
* Azure Service Bus Topic trigger
* Timer trigger

MS Learn:

* Sample: Load data from SQL using Python and Azure Functions
* Getting the list of Resource Groups using Azure Functions
* Data Cleaning Pipeline
* etc
https://learn.microsoft.com/en-us/samples/browse/?products=azure-functions&languages=python

## How to steps as an example with CoinWorker Http trigger (Queue/Table operations) and Firi API

* API for data, https://developers.firi.com
* Create an rg and add an azure function
* Function name must be the same as the function you will create.
* Select linux, Python, code consumption (serverless) and create a storage account
* Application insight will be enable later
* Deployment disable, git will be enabled later, now we just push with ps1
* Queue: st_queue.py
* * Identity, set the function app identity to be system assigned
* * On the storage account IAM, add role assignment function app identity to Storage Queue Data Contributor (Allows for read, write, and delete access to Azure Storage queues and queue messages)
* pip install azure-storage-queue 
* pip install azure-identity
* Put all imports or libs in requirements.txt

update 19.03.2024 for table

* add a secret in a key vault and retrive the secret for later use for the table connection.
* https://blog.nillsf.com/index.php/2020/09/16/connect-azure-functions-securely-to-key-vault-using-vnet-integration-and-private-link/
* https://medium.com/@dssc2022yt/accessing-azure-key-vault-secrets-with-azure-functions-2e651980f292

* Table: st_table.py
* * Identity, set the function app identity to be system assigned
* * On the storage account IAM, add role assignment function app identity to Storage Table Data Contributor (Allows for read, write, and delete access to Azure Storage tables and table messages)

Note! Use correct security with auth-level, this is just an example.

## Azure Functions Core Tools auth levels

-authlevel	Lets you set the authorization level for an HTTP trigger. Supported values are: 

* function
* anonymous 
* admin. 


https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference?tabs=v2#func-new

Example e-lo
https://github.com/spawnmarvel/azure-automation/tree/main/azure-5-functions

## Azure Queue credentials

* Shared Key
* Connection String
* Shared Access Signature Token
* Managed identity

https://learn.microsoft.com/en-us/python/api/overview/azure/storage-queue-readme?view=azure-python


## Create function project

https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=windows%2Cbash%2Cazure-cli&pivots=python-mode-decorators


```ps1
# A git repos was create first
# Thegit repos was cloned in azure-functions
cd c:\giti2023\azure-functions

# Run the func init command as follows to create a functions project
func init CoinWorker

Use the up/down arrow keys to select a worker runtime:python
Found Python version 3.10.7 (py).

cd coinWorker

```
## Create function (options)

```ps1
# Create a function
func new

Use the up/down arrow keys to select a template:
Azure Blob Storage trigger
Azure Cosmos DB trigger
Durable Functions activity
Durable Functions entity
Durable Functions HTTP starter
Durable Functions orchestrator
Azure Event Grid trigger
Azure Event Hub trigger
HTTP trigger
Kafka output
Kafka trigger
Azure Queue Storage trigger
RabbitMQ trigger
Azure Service Bus Queue trigger
Azure Service Bus Topic trigger
Timer trigger

# Create function oneliner

func new --name GetCoinStatus --template "HTTP trigger" --authlevel "anonymous"

# Start the function locally
func start

# Visit URL
http://localhost:7071/api/GetCoinStatus

This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.

```

## Publish function to az from Github repos

```ps1
# Publish is
az login --tenant

# still in \CoinWorker>
func azure functionapp publish GetCoinStatus

func azure functionapp publish GetCoinStatus --python
# Can't determine project language from files. Please use one of [--csharp, --javascript, --typescript, --java, --python, --powershell, --custom]
# Your Azure Function App has 'FUNCTIONS_WORKER_RUNTIME' set to 'python' while your local project is set to 'None'.

[...]
Deployment successful. deployer = Push-Deployer deploymentPath = Functions App ZipDeploy. Extract zip. Remote build.
Remote build succeeded!
Syncing triggers...

# Now visit URL

https://getcoinstatus.azurewebsites.net

# append /api/function name

This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.


```

## Update function

* Put all imports or libs in requirements.txt
* Add the code inside function name folder, worker.py, st_queue.py
* Test it, you might need to az login if much dependencies
* Publish it

Example

```py
# _init_.py
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    workerInstance = Worker()
    # [...]
    li = [sol_status, dot_status, xrp_status, ada_status, coinmarket, length_of_queue]
    return func.HttpResponse(str(li), mimetype="text/json")

# st_queue.py
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

# requirements.txt
# Do not include azure-functions-worker in this file
# The Python Worker is managed by the Azure Functions platform
# Manually managing azure-functions-worker may cause unexpected issues

azure-functions
# extra
requests
azure-storage-queue 
azure-identity
```


## Log stream

In the function app you can log the stream and view the running result

## Log and diagnostics settings

* Use logging.level as normal in the code
* Create a log analytics workspace
* On the function app go to Diagnostic settings, enable it.
* Enable Function Application Logs to destination select the loganalytics workspace


Set up https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitor-log-analytics?tabs=python

General https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview


## Kusto

https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries

Visuals at https://follow-e-lo.com/2023/12/12/azure-function-python/

* The take operator is perfect for this task, because it returns a specific number of arbitrary rows.
* You’ll use the project operator to define which columns you want to see in the output and also to define new columns on the fly on the tabular.

```kusto
FunctionAppLogs
| project TimeGenerated, HostInstanceId, Message
| where Message == "SOLNOK:"
| take 2
```

## Logic app and alerts

* Create a logic app, consumption plan
* Http trigger to run the request
* Create mail alert on log statment

https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/tutorial-log-alert

## Azure Table storage vs CosmosDB

Comparing Azure Cosmos DB for Table and Azure Table Storage

Azure Cosmos DB for Table uses a reserved capacity model in order to ensure guaranteed performance but this means that one pays for the capacity as soon as the table is created, even if the capacity isn't being used. With Azure Table storage one only pays for capacity that's used.

https://learn.microsoft.com/en-us/azure/cosmos-db/table/faq

Select a candidate

https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-decision-tree


Cosmos DB is a superset of the Azure Table Storage functionality.

![](https://github.com/spawnmarvel/azure-functions/blob/main/images/table_vs_cosmos.jpg)

https://microsoft.github.io/AzureTipsAndTricks/blog/tip166.html

Appropriate Use for Table Storage

https://learn.microsoft.com/en-us/answers/questions/172775/appropriate-use-for-table-storage

## Create a key vault for our table connection

update 19.03.2024 for table

* add a secret in a key vault and retrive the secret for later use for the table connection.
* https://medium.com/@dssc2022yt/accessing-azure-key-vault-secrets-with-azure-functions-2e651980f292

* https://blog.nillsf.com/index.php/2020/09/16/connect-azure-functions-securely-to-key-vault-using-vnet-integration-and-private-link/

* Create a key vault allow public so we can test the code.
* When that works we can secure it with a private link.
* azure-keyvault for requiremenets.py
* Azure role-based access control (recommended) in key vault, add role Key Vault Secrets User for function app

publish the app and verify in function app Log Stream

```log
2024-03-19T15:35:28Z   [Information]   Azure Key vault get success
2024-03-19T15:35:28Z   [Information]   Azure Table storage, trying to connect to table
2024-03-19T15:35:28Z   [Information]   Azure Table storage, connection success


2024-03-19T15:46:56Z   [Information]   []
2024-03-19T15:46:56Z   [Information]   Listing Azure Table storage
2024-03-19T15:46:56Z   [Information]   SOLNOK:


```

## Work with tables, create new if not exist

Clients
Two different clients are provided to interact with the various components of the Table Service:

TableServiceClient -
* Get and set account setting
* Query, create, and delete tables within the account.
* Get a TableClient to access a specific table using the get_table_client method.

TableClient -
* Interacts with a specific table (which need not exist yet).
* Create, delete, query, and upsert entities within the specified table.
* Create or delete the specified table itself.


https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme?view=azure-python#creating-entities



Iterate over tables

```log
2024-03-19T16:19:54Z   [Information]   Azure Table storage, trying to create table
2024-03-19T16:19:54Z   [Information]   Response status: 200
[...]
2024-03-19T16:29:29Z   [Information]   cointable
2024-03-19T16:29:29Z   [Information]   cointable01
2024-03-19T16:29:29Z   [Information]   cointable01 already exists
2024-03-19T16:29:29Z   [Information]   SOLNOK:
2024-03-19T16:29:29Z   [Information]   {'Api version': '2.0', 'Status Code'
```


Insert entity

```log
2024-03-19T17:00:56Z   [Information]   Trying to insert to table
[...]
2024-03-19T17:00:56Z   [Information]   Success insert to table
```

## Create a key vault for our table connection private link TODO

* Create a key vault
* Test it with ps1
* Create a private link
* Test it with ps1

Update st_key_vault.py

## Debug in portal

https://follow-e-lo.com/2024/03/22/azure-function-python-step-7-debug/





