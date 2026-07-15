# Pharma Commercial Data Lakehouse

End-to-end Azure Data Engineering project that integrates pharmaceutical commercial data into a centralized Lakehouse 
using Azure Databricks, PySpark, Delta Lake, and the Medallion Architecture.

---

## Project Overview

This project combines Sales, Products, Claims, Prescriptions, Healthcare Professionals (HCP), Hospitals, Territories, and Sales Representatives into a single analytics platform.

The data is processed through Bronze, Silver, and Gold layers to create clean, business-ready datasets for reporting and analysis.

---

## Business Problem

Pharmaceutical commercial data is usually stored across multiple systems, making reporting slow and inconsistent.

This project solves that problem by building a centralized Lakehouse where data is cleaned, transformed, and prepared for business analytics.

---

## Solution Architecture

<img width="1672" height="941" alt="pharma_lakehouse_architecture png" src="https://github.com/user-attachments/assets/62295962-f8d8-4cad-a6a8-4075efac4b88" />




## Medallion Architecture

<img width="1536" height="1024" alt="Medallion architecture png" src="https://github.com/user-attachments/assets/a6380a5b-16e3-4305-8ba3-abebbf81ba62" />

```

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Cloud | Microsoft Azure |
| Storage | Azure Data Lake Storage Gen2 |
| Processing | Azure Databricks |
| Language | Python |
| Framework | PySpark |
| Storage Format | Delta Lake |
| Governance | Unity Catalog |
| Pipeline | Azure Data Factory |
| Query Language | SQL |
| Visualization | Power BI (Optional) |
| Version Control | Git & GitHub |

---

## Project Workflow

```text
CSV Files
    │
    ▼
Azure Data Lake Storage Gen2
    │
    ▼
Azure Databricks
    │
    ▼
Bronze Layer
    │
    ▼
Silver Layer
    │
    ▼
Gold Layer
    │
    ▼
Business KPIs
```

---

## Repository Structure

```text
pharma-commercial-data-lakehouse/
│
├── architecture/
├── datasets/
├── documents/
├── notebooks/
├── queries/
├── screenshots/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Project Layers

### Bronze Layer
- Loaded raw CSV files into Delta tables.
- Preserved original source data.

<img width="1532" height="725" alt="07 Bronze Ingestion Notebook" src="https://github.com/user-attachments/assets/2f2e1cb2-5740-4da7-b0fd-560e1542f52c" />


---

### Silver Layer
- Removed duplicates
- Handled missing values
- Standardized data
- Applied business transformations

<img width="1536" height="732" alt="08 Silver Transformation Notebook" src="https://github.com/user-attachments/assets/db485545-0b6c-400b-b982-1247e3234c28" />


---

### Gold Layer
- Built analytical tables
- Generated business-ready datasets
- Created KPIs for reporting

<img width="1532" height="727" alt="09 Gold Final Architecture Notebook" src="https://github.com/user-attachments/assets/9004c2b9-1ff7-4271-8650-7366bb73b613" />


## Business KPIs

Implemented analytical KPIs including:

- Total Sales
- Net Revenue
- Sales by Territory
- Sales by Product
- Top Products
- Monthly Sales Trend
- Claims Summary
- Claims Status
- Prescription Analysis
- Top Healthcare Professionals
- Product Performance
- Territory Performance
- Revenue by Brand
- Revenue by Manufacturer
- Active Sales Representatives
- Sales Distribution
- Product Category Analysis
- Hospital Performance
- Average Sales Value
- Sales Growth

<img width="1528" height="720" alt="10 Buisness Kpis" src="https://github.com/user-attachments/assets/e21130e6-547d-4ca5-a4a9-c44eef9a0d26" />

```

---

## Azure Data Factory

Azure Data Factory was configured to orchestrate the data pipeline and demonstrate pipeline automation.

<img width="1536" height="722" alt="14 Azure data factory Notebook" src="https://github.com/user-attachments/assets/1361c24b-6328-42ad-a6c8-839cdd75078b" />


```

---

## Documentation

The repository also includes:

- Project Overview
- Data Dictionary
- Pipeline Flow
- Business Rules
- SQL Query Reference
- PySpark Query Reference

---

## Skills Demonstrated

- Azure Databricks
- Azure Data Lake Storage Gen2
- Azure Data Factory
- PySpark
- SQL
- Delta Lake
- Unity Catalog
- ETL Development
- Data Transformation
- Data Modeling
- Business KPI Development
- Git & GitHub

---

## Future Improvements

- Incremental Data Loading
- Automated Pipeline Scheduling
- Data Quality Validation
- CI/CD Integration
- Monitoring & Alerting

---

## Author
**Rohit Kumar**

Aspiring Azure Data Engineer

**Rohit Kumar**

Aspiring Azure Data Engineer

<p align="center">

<img src="https://img.shields.io/badge/Azure-Cloud-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
<img src="https://img.shields.io/badge/Azure%20Databricks-Data%20Engineering-E36209?style=for-the-badge&logo=databricks&logoColor=white"/>
<img src="https://img.shields.io/badge/PySpark-Big%20Data-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white"/>
<img src="https://img.shields.io/badge/Delta%20Lake-Lakehouse-00ADD8?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/SQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/Unity%20Catalog-Data%20Governance-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Azure%20Data%20Factory-Orchestration-0062AD?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white"/>

</p>
