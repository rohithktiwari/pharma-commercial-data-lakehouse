# Project Overview

## Business Problem

Pharmaceutical organizations often manage commercial data across multiple disconnected systems. Sales transactions, prescription records, insurance claims, product information, healthcare professional (HCP) data, hospitals, and territory details are typically stored separately, making it difficult to generate consistent business insights.

The absence of a centralized platform results in duplicate records, inconsistent reporting, and slow analytical processes.

---

## Project Objective

The objective of this project is to build a scalable Azure-based Data Lakehouse that consolidates multiple pharmaceutical datasets into a single analytics platform.

The solution follows the Medallion Architecture (Bronze, Silver, and Gold) to transform raw operational data into business-ready datasets for reporting and decision-making.

---

## Solution

The project ingests multiple CSV datasets into Azure Data Lake Storage Gen2 and processes them using Azure Databricks with PySpark.

Data is transformed through three layers:

- Bronze Layer – Raw data ingestion
- Silver Layer – Data cleansing and standardization
- Gold Layer – Business-ready analytical tables

The final Gold layer supports business KPIs and reporting.

---

## Technologies Used

- Azure Data Lake Storage Gen2
- Azure Databricks Connector 
- Azure Databricks
- PySpark
- Delta Lake
- Unity Catalog
- Azure Data Factory
- SQL
- GitHub

---

## Project Outcome

The solution creates a centralized analytics platform capable of delivering reliable commercial insights, reducing data redundancy, and improving reporting efficiency across sales, claims, prescriptions, products, territories, hospitals, and healthcare professionals.
