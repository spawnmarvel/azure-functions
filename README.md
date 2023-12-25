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

## How to steps as an example with CoinWorker Http trigger (Queue operations) and Firi API

* API for data, https://developers.firi.com
* Create an rg and add an azure function
* Function name must be the same as the function you will create.
* Select linux, Python, code consumption (serverless) and create a storage account
* Application insight will be enable later
* Deployment disable, git will be enabled later, now we just push with ps1
* Queue:
* * Identity, set the function app identity to be system assigned
* * On the storage account IAM, add role assignment function app identity to Storage Queue Data Contributor (Allows for read, write, and delete access to Azure Storage queues and queue messages)
* pip install azure-storage-queue 
* pip install azure-identity
* Put all imports or libs in requirements.txt

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


## How to steps as an example with MapWorker Http trigger (Table operations) Geo Norge API


* API for data, https://ws.geonorge.no/kommuneinfo/v1/
* pip install azure-data-tables
* Put all imports or libs in requirements.txt

Table:

* Shared Key
* Connection String
* Shared Access Signature Token
* Managed identity? Should work

https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme?view=azure-python

How to hide API keys from git example:
* .gitignore = env.py
* Git push
* Add env.py to project
* code = API_CONNECTION = "TEST123"
* Import it in module = from GetMapStatus.env import API_CONNECTION
* Use ut = self.row =  API_CONNECTION

```ps1
azure-functions> func init MapWorker

Use the up/down arrow keys to select a worker runtime:python

cd .\MapWorker\

func new --name GetMapStatus --template "HTTP trigger" --authlevel "anonymous"


func start
```