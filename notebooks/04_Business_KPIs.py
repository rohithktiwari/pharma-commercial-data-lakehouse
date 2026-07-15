# Databricks notebook source
from pyspark.sql.functions import *

sales = spark.table("gold.sales_analytics")
prescription = spark.table("gold.prescription_analytics")
claims = spark.table("gold.claims_analytics")

# COMMAND ----------

# MAGIC %md
# MAGIC # Business KPIs
# MAGIC
# MAGIC This notebook contains business KPIs generated from the Gold Layer tables.
# MAGIC These KPIs help business users analyze sales performance, product performance,
# MAGIC doctor activity, territory performance, prescription trends and claims analysis.

# COMMAND ----------

from pyspark.sql.functions import *

sales = spark.table("gold.sales_analytics")
prescription = spark.table("gold.prescription_analytics")
claims = spark.table("gold.claims_analytics")

# COMMAND ----------

# MAGIC %md
# MAGIC # Section 1 - Sales Performance KPIs

# COMMAND ----------

# MAGIC %md
# MAGIC #1.Top 10 Products by Sales

# COMMAND ----------

top_products = (
    sales
    .groupBy("Product_Name")
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy(col("Total_Sales").desc())
)

display(top_products)

# COMMAND ----------

# MAGIC %md
# MAGIC #Top 10 Products by Quantity Sold

# COMMAND ----------

top_quantity = (
    sales
    .groupBy("Product_Name")
    .agg(
        sum("Quantity").alias("Total_Quantity")
    )
    .orderBy(col("Total_Quantity").desc())
)

display(top_quantity)

# COMMAND ----------

# MAGIC %md
# MAGIC #Sales by Territory

# COMMAND ----------

territory_sales = (
    sales
    .groupBy("Territory_Name")
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy(col("Total_Sales").desc())
)

display(territory_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC #Sales by Brand

# COMMAND ----------

brand_sales = (
    sales
    .groupBy("Brand")
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy(col("Total_Sales").desc())
)

display(brand_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC #Sales by Category

# COMMAND ----------

category_sales = (
    sales
    .groupBy("Category")
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy(col("Total_Sales").desc())
)

display(category_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC # Section 2 - Sales Trend & Sales Representative KPIs

# COMMAND ----------

# MAGIC %md
# MAGIC #Monthly Sales Trend

# COMMAND ----------

monthly_sales = (
    sales
    .groupBy(month("Sale_Date").alias("Month"))
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy("Month")
)

display(monthly_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC #Sales by State

# COMMAND ----------

state_sales = (
    sales
    .groupBy("State")
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy(col("Total_Sales").desc())
)

display(state_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC #Top Sales Representatives

# COMMAND ----------

rep_sales = (
    sales
    .groupBy("Rep_ID")
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy(col("Total_Sales").desc())
)

display(rep_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC #Revenue by Manufacturer

# COMMAND ----------

manufacturer_sales = (
    sales
    .groupBy("Manufacturer")
    .agg(
        sum("Sales_Amount").alias("Total_Sales")
    )
    .orderBy(col("Total_Sales").desc())
)

display(manufacturer_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC #Average Sales Per Product

# COMMAND ----------

avg_sales = (
    sales
    .groupBy("Product_Name")
    .agg(
        avg("Sales_Amount").alias("Average_Sales")
    )
    .orderBy(col("Average_Sales").desc())
)

display(avg_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC # Section 3 - Prescription KPIs

# COMMAND ----------

# MAGIC %md
# MAGIC ##Top Doctors by Prescription Count

# COMMAND ----------

top_doctors = (
    prescription
    .groupBy("Doctor_Name")
    .count()
    .withColumnRenamed("count", "Prescription_Count")
    .orderBy(col("Prescription_Count").desc())
)

display(top_doctors)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Top Prescribed Products

# COMMAND ----------

top_prescribed_products = (
    prescription
    .groupBy("Product_Name")
    .count()
    .withColumnRenamed("count", "Prescription_Count")
    .orderBy(col("Prescription_Count").desc())
)

display(top_prescribed_products)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Prescriptions by Specialization

# COMMAND ----------

specialization_prescriptions = (
    prescription
    .groupBy("Specialization")
    .count()
    .withColumnRenamed("count", "Prescription_Count")
    .orderBy(col("Prescription_Count").desc())
)

display(specialization_prescriptions)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Prescriptions by Brand

# COMMAND ----------

brand_prescriptions = (
    prescription
    .groupBy("Brand")
    .count()
    .withColumnRenamed("count", "Prescription_Count")
    .orderBy(col("Prescription_Count").desc())
)

display(brand_prescriptions)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Top Categories by Prescription

# COMMAND ----------

category_prescriptions = (
    prescription
    .groupBy("Category")
    .count()
    .withColumnRenamed("count", "Prescription_Count")
    .orderBy(col("Prescription_Count").desc())
)

display(category_prescriptions)

# COMMAND ----------

prescription.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC # Section 4 - Claims KPIs

# COMMAND ----------

# MAGIC %md
# MAGIC ##Claims by Status

# COMMAND ----------

claims_status = (
    claims
    .groupBy("Status")
    .count()
    .withColumnRenamed("count", "Total_Claims")
    .orderBy(col("Total_Claims").desc())
)

display(claims_status)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Top Hospitals by Claims

# COMMAND ----------

hospital_claims = (
    claims
    .groupBy("Hospital_Name")
    .count()
    .withColumnRenamed("count", "Total_Claims")
    .orderBy(col("Total_Claims").desc())
)

display(hospital_claims)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Claims by State

# COMMAND ----------

state_claims = (
    claims
    .groupBy("State")
    .count()
    .withColumnRenamed("count", "Total_Claims")
    .orderBy(col("Total_Claims").desc())
)

display(state_claims)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Claims by Product

# COMMAND ----------

product_claims = (
    claims
    .groupBy("Product_Name")
    .count()
    .withColumnRenamed("count", "Total_Claims")
    .orderBy(col("Total_Claims").desc())
)

display(product_claims)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Total Claim Amount by Product

# COMMAND ----------

claim_amount = (
    claims
    .groupBy("Product_Name")
    .agg(
        sum("Claim_Amount").alias("Total_Claim_Amount")
    )
    .orderBy(col("Total_Claim_Amount").desc())
)

display(claim_amount)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

