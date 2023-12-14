# azure-functions
Testing and learning Azure functions

## Docs

https://learn.microsoft.com/en-us/azure/azure-functions/

## Python

## How to steps

* Create an rg and add an azure function
* Function name must be the same as the function you will create.
* Select linux, Python, code consumption (serverless) and create a storage account
* Application insight enable later
* Deployment disable, git will be enabled later, now we just push with ps1
* Identity, set the function app identity to be system assigned
* On the storage account IAM, add role assignment function app identity to Storage Queue Data Contributor (Allows for read, write, and delete access to Azure Storage queues and queue messages)

Note! Use correct security with auth-level, this is just an example.

##  Create function

https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=windows%2Cbash%2Cazure-cli&pivots=python-mode-decorators


```ps1
# This git repos was cloned in azure-functions
cd c:\giti2023\azure-functions

# Run the func init command as follows to create a functions project
func init CoinWorker

Use the up/down arrow keys to select a worker runtime:python
Found Python version 3.10.7 (py).

cd coinWorker

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

# Create function

func new --name GetCoinStatus --template "HTTP trigger" --authlevel "anonymous"

# Start the function locally
func start

# Visit URL
http://localhost:7071/api/GetCoinStatus

This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.

# Publish is
az login --tenant

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
* Add code inside function name
* Test it, you might need to az login if much dependencies
* Publish it

Edit _init_.py example

```py
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    workerInstance = Worker()
    # [...]
    li = [sol_status, dot_status, xrp_status, ada_status, coinmarket, length_of_queue]
    return func.HttpResponse(str(li), mimetype="text/json")

```

## Logging and log analytics

https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview

* Use logging.level as normal in the code
* Create a log analytics workspace
* Enable Applictions insight on the function app , select the loganalytics workspace


## Kusto

https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries

*

## Alerts and logic app



## Functions

CoinWorker->GetCoinStatus 
* Type httptrigger
* Get data from external API
* if limit, insert to queue

QueueWorker->GetQueueStatus http trigger
* Type httptrigger
* Get data from queue

Next workspace->FunctionName
* Type