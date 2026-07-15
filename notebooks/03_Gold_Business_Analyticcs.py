# Databricks notebook source
sales = spark.table("gold.sales_analytics")
display(sales)

# COMMAND ----------

from pyspark.sql.functions import sum

top_products = (
    sales.groupBy("Product_Name")
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Total_Sales", ascending=False)
)

display(top_products)

# COMMAND ----------

territory_sales = (
    sales.groupBy("Territory_Name")
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Total_Sales", ascending=False)
)

display(territory_sales)

# COMMAND ----------

doctor_sales = (
    sales.groupBy("Doctor_Name")
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Total_Sales", ascending=False)
)

display(doctor_sales)

# COMMAND ----------

brand_sales = (
    sales.groupBy("Brand")
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Total_Sales", ascending=False)
)

display(brand_sales)

# COMMAND ----------

category_sales = (
    sales.groupBy("Category")
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Total_Sales", ascending=False)
)

display(category_sales)

# COMMAND ----------

from pyspark.sql.functions import month

monthly_sales = (
    sales.groupBy(month("Sale_Date").alias("Month"))
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Month")
)

display(monthly_sales)

# COMMAND ----------

rep_sales = (
    sales.groupBy("Rep_ID")
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Total_Sales", ascending=False)
)

display(rep_sales)

# COMMAND ----------

from pyspark.sql.functions import avg

avg_product_sales = (
    sales.groupBy("Product_Name")
    .agg(avg("Sales_Amount").alias("Average_Sales"))
    .orderBy("Average_Sales", ascending=False)
)

display(avg_product_sales)

# COMMAND ----------

quantity_sold = (
    sales.groupBy("Product_Name")
    .agg(sum("Quantity").alias("Total_Quantity"))
    .orderBy("Total_Quantity", ascending=False)
)

display(quantity_sold)

# COMMAND ----------

manufacturer_sales = (
    sales.groupBy("Manufacturer")
    .agg(sum("Sales_Amount").alias("Total_Sales"))
    .orderBy("Total_Sales", ascending=False)
)

display(manufacturer_sales)

# COMMAND ----------

# MAGIC %md
# MAGIC # Prescription Analytics

# COMMAND ----------

prescription = spark.table("silver.prescription")
product = spark.table("silver.product")
hcp = spark.table("silver.hcp")

# COMMAND ----------

from pyspark.sql.functions import col

prescription_final = (
    prescription.alias("p")
    .join(product.alias("pr"),
          col("p.Product_ID") == col("pr.Product_ID"), "left")
    .join(hcp.alias("h"),
          col("p.HCP_ID") == col("h.HCP_ID"), "left")
    .select(
        "p.*",
        "pr.Product_Name",
        "pr.Category",
        "pr.Brand",
        "h.Doctor_Name",
        "h.Specialization"
    )
)

display(prescription_final)

# COMMAND ----------

prescription_final.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("gold.prescription_analytics")

# COMMAND ----------

display(spark.table("gold.prescription_analytics"))

# COMMAND ----------

# MAGIC %md
# MAGIC # Claims Analytics
# MAGIC

# COMMAND ----------

claims = spark.table("silver.claims")
hospital = spark.table("silver.hospital")
product = spark.table("silver.product")

# COMMAND ----------

from pyspark.sql.functions import col

claims_final = (
    claims.alias("c")
    .join(hospital.alias("h"),
          col("c.Hospital_ID") == col("h.Hospital_ID"), "left")
    .join(product.alias("p"),
          col("c.Product_ID") == col("p.Product_ID"), "left")
    .select(
        "c.*",
        "h.Hospital_Name",
        "h.City",
        "h.State",
        "p.Product_Name",
        "p.Category",
        "p.Brand"
    )
)

display(claims_final)

# COMMAND ----------

claims_final.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("gold.claims_analytics")

# COMMAND ----------

display(spark.table("gold.claims_analytics"))

# COMMAND ----------

sales_df = spark.table("gold.sales_analytics")

display(sales_df)

# COMMAND ----------

prescription_df = spark.table("gold.prescription_analytics")

display(prescription_df)

# COMMAND ----------

claims_df = spark.table("gold.claims_analytics")

display(claims_df)