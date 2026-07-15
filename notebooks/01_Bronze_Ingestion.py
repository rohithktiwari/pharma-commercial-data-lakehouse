# Databricks notebook source
spark

# COMMAND ----------

df = spark.read.format("csv") \
    .option("header", "true") \
    .load("abfss://bronze@stpharmalake.dfs.core.windows.net/sales/sales_enterprise.csv")

display(df)

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS bronze")

# COMMAND ----------

df.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("bronze.sales")

# COMMAND ----------

df.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("bronze.sales")

# COMMAND ----------

display(spark.table("bronze.sales"))

# COMMAND ----------

# MAGIC %md
# MAGIC # BRONZE LAYER - ALL DATASETS

# COMMAND ----------

prescription_df = spark.read.format("csv") \
.option("header","true") \
.load("abfss://bronze@stpharmalake.dfs.core.windows.net/prescription/prescription_enterprise.csv")

display(prescription_df)

# COMMAND ----------

prescription_df.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("bronze.prescription")

# COMMAND ----------

def load_to_bronze(folder_name, file_name, table_name):

    df = spark.read.format("csv") \
        .option("header", "true") \
        .load(f"abfss://bronze@stpharmalake.dfs.core.windows.net/{folder_name}/{file_name}")

    df.write \
        .mode("overwrite") \
        .format("delta") \
        .saveAsTable(f"bronze.{table_name}")

    print(f"✅ bronze.{table_name} loaded successfully")

# COMMAND ----------

load_to_bronze("claims", "claims_enterprise.csv", "claims")

# COMMAND ----------

display(spark.table("bronze.claims"))

# COMMAND ----------

load_to_bronze("hcp", "hcp_enterprise.csv", "hcp")
load_to_bronze("hospital", "hospital_enterprise.csv", "hospital")
load_to_bronze("product", "product_enterprise.csv", "product")
load_to_bronze("sales_rep", "sales_rep_enterprise.csv", "sales_rep")
load_to_bronze("territory", "territory_enterprise.csv", "territory")

# COMMAND ----------

display(spark.sql("SHOW TABLES IN bronze"))