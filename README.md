📦 Telecom Customer Churn Analytics & Prediction
An end-to-end data project using SQL Server, Python (XGBoost), and Power BI.

📘 Overview

This repository contains a complete Customer Churn Analytics & Prediction solution for telecom data.
It integrates:

Data Engineering (SQL Server ETL + analytical views)

Machine Learning (Python + XGBoost)

Business Intelligence (Power BI dashboard)

Semantic Modeling (DAX measures, calculated tables, and business logic)

The goal is to understand why customers churn, identify drivers and risk factors, and predict future churn.
The project reflects a real-world, enterprise-level data workflow designed for insights and decision-making.


📁 Repository Structure

📦 Telecom-Churn-Analytics
│
├── Data/
│   └── Original raw datasets.
│
├── MSSQL-ETL/
│   └── SQL Server scripts:
│       - Data exploration & cleaning
│       - ETL pipeline (staging → curated → analytical)
│       - Creation of views for direct Power BI connection
│
├── PBI_Measures_Tables&Columns/
│   └── Power BI semantic model:
│       - DAX measures
│       - Calculated tables
│       - Calculated columns
│       - Domain/business logic
│
├── churnpred/
│   ├── churnpred.py
│   │   Machine Learning pipeline:
│   │   - Binary churn model
│   │   - Multiclass churn category model
│   │   - Threshold optimization
│   │   - CSV output generation
│   ├── Readme_churnpred.md
│       Technical ML documentation.
│
├── Churn Analysis_DashBoard.pbix
│   └── Power BI dashboard (Summary + Predictions)
│
└── README.md



⚙️ Technology Stack

| Layer                | Technology                            | Description                                          |
| -------------------- | ------------------------------------- | ---------------------------------------------------- |
| **Data Engineering** | SQL Server                            | ETL, cleaning, feature preparation, analytical views |
| **Machine Learning** | Python, Pandas, Scikit-Learn, XGBoost | Predictive churn modeling                            |
| **Visualization**    | Power BI                              | Exploratory + predictive churn dashboards            |
| **Semantic Model**   | DAX, Data Modeling                    | Business metrics and logic                           |


🤖 Machine Learning – Churn Prediction Pipeline

The churnpred.py script performs the full ML workflow.

1. Churn Prediction (Binary Model)

Predicts whether a customer is likely to churn.

Techniques Used

ColumnTransformer for preprocessing

OneHotEncoding for categorical fields

XGBoostClassifier (300 trees, tuned hyperparameters)

Train/Test split with stratification

ROC-AUC evaluation

Precision–Recall analysis

F1-optimizing threshold (replaces the default 0.5)

2. Churn Category Prediction (Multiclass Model)

Predicts why a customer churned (for churned customers only), such as:

Competitor

Service issues

Price

Attitude

Other churn categories

3. Outputs

The script generates two enriched files:
churn_predictions_all_customers.csv
churn_predictions_new_joiners.csv

Each file includes:

Churn probability

Predicted churn label

Predicted churn category

All original customer fields


📊 Power BI – Churn Analytics Dashboard

The dashboard contains two major pages: Summary and Predictions.

📄 Page 1 — Churn Analysis: Summary
KPIs

Total Customers

New Joiners

Total Churn

Overall Churn Rate

Visual Insights

Churn Rate by State

Churn Rate by Internet Type

Churn by Gender

Customers & Churn Rate by Age Group

Churn Rate by Payment Method

Churn Rate by Contract Type

Customers & Churn Rate by Tenure Group

Churn by Category

Service adoption tables (Yes/No per service)

📄 Page 2 — Churn Analysis: Predictions
Predictive KPIs

Predicted Churn Customers

Predicted Churn Rate

Average Predicted Churn Probability

Predictive Visuals

Predicted Churn by Gender

Predicted Churn by Age Group

Predicted Churn Rate by State

Predicted Churn Rate by Internet Type

Predicted Churn Rate by Payment Method

Predicted Churn Rate by Contract

Predicted Churn Rate by Tenure Group

Predicted Churn by Category

Predicted Churn by Marital Status

Churn Probability vs Monthly Charge

These visuals combine outputs from SQL views, DAX modelling, and Python ML predictions.


🧩 High-Level Architecture

                 SQL Server (ETL + Analytical Views)
                               │
                               ├──────────► Power BI (Historical Analysis)
                               │
                               └──────────► Python ML Engine
                                               │
                                               ├── Predictions → Power BI
                                               └── Predictions for New Joiners



🎯 Project Objectives

Build a practical, business-oriented churn analytics pipeline

Understand historical churn patterns and customer behavior

Predict customers at high risk of leaving

Identify churn drivers and categories

Support customer retention strategies with ML + BI

Demonstrate advanced skills in:

SQL Server

Data modeling (DAX)

Python ML

Power BI storytelling


🚀 Future Improvements

SHAP explainability for model transparency

Deploy ML model as an API (FastAPI / Flask)

Automate daily predictions with Azure Data Factory / Prefect

Add new features (LTV, RFM scoring, NPS, service usage)

Integrate retention recommendations (Next Best Action Engine)


📥 How to Use This Repository
1. Load the dataset

Place your raw dataset inside the Data/ folder.

2. Run SQL ETL

Execute the scripts in MSSQL-ETL/ to build cleaned tables and analytical views.

3. Open Power BI

Load the dashboard file:
Churn Analysis_DashBoard.pbix

4. (Optional) Generate new ML predictions
python churnpred/churnpred.py

5. Refresh Power BI
Load the updated CSV predictions into the dashboard’s predictive page.


🏁 Final Notes

This repository showcases a realistic and fully integrated data solution combining:

ETL

Machine Learning

Semantic Modeling

Business Intelligence

Ideal for enterprise churn analytics and customer retention forecasting.
