# Databricks notebook source
def mount(container_name, storage_account_name, configs):
    dbutils.fs.mount(
        source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_account_name}/{container_name}",
        extra_configs = configs
    )

# COMMAND ----------

# access information for our storage blob
storage_account_name = "formula1ay"
client_id = dbutils.secrets.get(scope="formula1-scope", key="databricks-app-client-id")
tenant_id = dbutils.secrets.get(scope="formula1-scope", key="databricks-app-tenant-id")
client_secret = dbutils.secrets.get(scope="formula1-scope", key="databricks-app-client-secret")

# COMMAND ----------

# ERROR: remember to spell 'oauth' correctly - not oath!!!
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": f"{client_id}",
    "fs.azure.account.oauth2.client.secret": f"{client_secret}",
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token",
}

# COMMAND ----------

mount("raw", storage_account_name, configs)

# COMMAND ----------

mount("processed", storage_account_name, configs)

# COMMAND ----------

# dbutils.fs.unmount("/mnt/formula1ay/processed")

# COMMAND ----------

# list mounted storage to check the operation has completed succesfully
dbutils.fs.mounts()

# COMMAND ----------


