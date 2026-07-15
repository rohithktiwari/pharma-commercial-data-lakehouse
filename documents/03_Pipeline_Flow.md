# Pipeline Flow

The project follows the Medallion Architecture.

## Step 1

CSV datasets are collected from multiple pharmaceutical business domains.

↓

## Step 2

Files are stored in Azure Data Lake Storage Gen2.

↓

## Step 3

Azure Databricks ingests the raw data into the Bronze layer.

↓

## Step 4

PySpark transforms the raw data by removing duplicates, handling null values, validating records, and standardizing formats in the Silver layer.

↓

## Step 5

Business-ready fact and dimension tables are created in the Gold layer.

↓

## Step 6

Business KPIs are generated for commercial reporting.

↓

## Step 7

Azure Data Factory is used to orchestrate the pipeline.

↓

## Step 8

The curated Gold layer can be consumed by reporting tools such as Power BI.
