# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Transformation
# MAGIC

# COMMAND ----------

spark.sql("USE bronze")

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS silver")

# COMMAND ----------

spark.sql("SHOW SCHEMAS").display()

# COMMAND ----------

sales_df = spark.table("bronze.sales")

display(sales_df)

# COMMAND ----------

sales_df.printSchema()

# COMMAND ----------

sales_df.count()

# COMMAND ----------

from pyspark.sql.functions import col, to_date

sales_clean = (
    sales_df
    .dropDuplicates(["Sale_ID"])
    .withColumn("Sale_Date", to_date(col("Sale_Date"), "yyyy-MM-dd"))
    .filter(col("Sales_Amount").isNotNull())
)


# COMMAND ----------

display(sales_clean)

# COMMAND ----------

sales_clean.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("silver.sales")

# COMMAND ----------

display(spark.table("silver.sales"))

# COMMAND ----------

from pyspark.sql.functions import col, to_date

def load_to_silver(table_name, id_column, date_column=None):

    df = spark.table(f"bronze.{table_name}")

    df = df.dropDuplicates([id_column])

    if date_column:
        df = df.withColumn(date_column, to_date(col(date_column), "yyyy-MM-dd"))

    df.write \
      .mode("overwrite") \
      .format("delta") \
      .saveAsTable(f"silver.{table_name}")

    print(f"silver.{table_name} loaded successfully")

# COMMAND ----------

load_to_silver("claims", "Claim_ID", "Claim_Date")
load_to_silver("prescription", "Prescription_ID", "Prescription_Date")
load_to_silver("hcp", "HCP_ID")
load_to_silver("hospital", "Hospital_ID")
load_to_silver("product", "Product_ID")
load_to_silver("sales_rep", "Rep_ID")
load_to_silver("territory", "Territory_ID")

# COMMAND ----------

sales = spark.table("silver.sales")
product = spark.table("silver.product")
hcp = spark.table("silver.hcp")
territory = spark.table("silver.territory")

# COMMAND ----------

from pyspark.sql.functions import col

sales_final = (
    sales.alias("s")
    .join(product.alias("p"), col("s.Product_ID") == col("p.Product_ID"), "left")
    .join(hcp.alias("h"), col("s.HCP_ID") == col("h.HCP_ID"), "left")
    .join(territory.alias("t"), col("s.Territory_ID") == col("t.Territory_ID"), "left")
    .select(
        "s.*",

        "p.Product_Name",
        "p.Category",
        "p.Price",
        "p.Brand",
        "p.Manufacturer",

        "h.Doctor_Name",
        "h.Specialization",
        "h.Qualification",

        "t.Territory_Name",
        "t.Region",
        "t.State",
        "t.Zone"
    )
)

# COMMAND ----------

sales_final.columns

# COMMAND ----------

sales_final = sales_final.drop(territory["Active"])

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS gold")

# COMMAND ----------

sales_final.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("gold.sales_analytics")

# COMMAND ----------

spark.sql("SELECT current_catalog(), current_schema()").display()

# COMMAND ----------

display(spark.table("gold.sales_analytics"))

# COMMAND ----------



# COMMAND ----------

