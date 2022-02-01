# Databricks notebook source
# MAGIC %fs 
# MAGIC ls

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

for fname in dbutils.fs.ls('/'):
    print(fname)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dir(dbutils.fs)

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------


