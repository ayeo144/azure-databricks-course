# Databricks notebook source
# access information for our storage blob
storage_account_name = "formula1ay"
client_id = ""
tenant_id = ""
client_secret = ""

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

def mount(container_name, storage_account_name, configs):
    dbutils.fs.mount(
        source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_account_name}/{container_name}",
        extra_configs = configs
    )

# COMMAND ----------

mount("raw", storage_account_name, configs)

# COMMAND ----------

mount("processed", storage_account_name, configs)

# COMMAND ----------

# MAGIC %fs
# MAGIC 
# MAGIC ls mnt/formula1ay/

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1ay/raw")

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------


