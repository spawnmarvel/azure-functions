# azure-functions
Testing and learning Azure functions

## Docs

https://learn.microsoft.com/en-us/azure/azure-functions/

## Python

## How to steps

* Create an rg and add an azure function
* Select linux, Python and create a storage account
* Identity, set the function app identity to be system assigned
* On the storage account IAM, add role assignment function app identity to Storage Queue Data Contributor

Note! Use correct security with auth-level, this is just an example.

# Create function

https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=windows%2Cbash%2Cazure-cli&pivots=python-mode-decorators


```ps1

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

# Now visit URL

```