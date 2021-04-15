# Azure
## 1. User account setup
### 1.1 Assigning roles

Go to the UI on this path:

* `Home -> Azure Active Directory -> Users -> (click a user) -> Assigned roles -> Add assignments`

### 1.2 Assigning a subscription
`Home -> Subscriptions -> (click a subscription) -> Access control (IAM) -> Add -> Add role assignment`
To add an admin user, choose `Add co-administrator` in the `Add` menu instead.
### 1.3 Assigning roles v2

## 2. Services
### 2.1. Synapse
#### 2.1.1 Setup
Follow the official [guide](https://docs.microsoft.com/en-us/azure/synapse-analytics/get-started-create-workspace) to create the workspace.
#### 2.2.2 Sources
##### a. Supermetrics
Supermetrics has a direct connector for Synapse ([link](https://supermetrics.com/blog/supermetrics-for-azure-synapse)).
See the `How to get started with Supermetrics for Azure Synapse` section for a guide. Note that you first have to create the destination schema in the Synapse database. You can easily do this from `Data -> Databases -> (your database) -> Schemas -> (right click) -> New SQL script -> New schema`
##### b. Salesforce
Use the [guide](https://docs.microsoft.com/en-us/azure/data-factory/connector-salesforce). Make sure to use the upsert option.

## TODO
- secrets
- prefect inside notebook?
- how to install python packages inside Synapse
- sharing stuff in Synapse
- link with GitHub
- continue prefect research - check out Saturn Cloud execution with autoscaling (check out https://github.com/saturncloud/prefect-saturn)