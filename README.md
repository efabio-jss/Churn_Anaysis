# 📦 Telecom Customer Churn Analytics & Prediction

An end-to-end data project using **SQL Server**, **Python (XGBoost)**, and **Power BI**.

***

## 📘 Overview

This repository contains a complete **Customer Churn Analytics & Prediction** solution for telecom data. It integrates:

*   **Data Engineering**: SQL Server ETL + analytical views
*   **Machine Learning**: Python + XGBoost
*   **Business Intelligence**: Power BI dashboard
*   **Semantic Modeling**: DAX measures, calculated tables, and business logic

**Goal**: Understand why customers churn, identify drivers and risk factors, and predict future churn.  
This project reflects a real-world, enterprise-level data workflow designed for insights and decision-making.

***

## 📁 Repository Structure

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
    │
    │   ├── Readme_churnpred.md
    │       Technical ML documentation.
    │
    ├── Churn Analysis_DashBoard.pbix
    │   └── Power BI dashboard (Summary + Predictions)
    │
    └── README.md

***

## ⚙️ Technology Stack

| Layer            | Technology                            | Description                               |
| ---------------- | ------------------------------------- | ----------------------------------------- |
| Data Engineering | SQL Server                            | ETL, cleaning, feature preparation, views |
| Machine Learning | Python, Pandas, Scikit-Learn, XGBoost | Predictive churn modeling                 |
| Visualization    | Power BI                              | Exploratory + predictive dashboards       |
| Semantic Model   | DAX, Data Modeling                    | Business metrics and logic                |

***

## 🤖 Machine Learning – Churn Prediction Pipeline

The **churnpred.py** script performs the full ML workflow:

### **Binary Model**

Predicts whether a customer is likely to churn.

**Techniques Used**:

*   ColumnTransformer for preprocessing
*   OneHotEncoding for categorical fields
*   XGBoostClassifier (300 trees, tuned hyperparameters)
*   Train/Test split with stratification
*   ROC-AUC evaluation
*   Precision–Recall analysis
*   F1-optimizing threshold (replaces default 0.5)

### **Multiclass Model**

Predicts why a customer churned (for churned customers only):

*   Competitor
*   Service issues
*   Price
*   Attitude
*   Other categories

**Outputs**:

*   `churn_predictions_all_customers.csv`
*   `churn_predictions_new_joiners.csv`

Each file includes:

*   Churn probability
*   Predicted churn label
*   Predicted churn category
*   All original customer fields

***

## 📊 Power BI – Churn Analytics Dashboard

Two major pages:

### **Page 1 — Churn Analysis: Summary KPIs**

*   Total Customers
*   New Joiners
*   Total Churn
*   Overall Churn Rate

**Visual Insights**:

*   Churn Rate by State, Internet Type, Gender
*   Customers & Churn Rate by Age Group
*   Churn Rate by Payment Method, Contract Type
*   Service adoption tables

### **Page 2 — Churn Analysis: Predictions**

*   Predicted Churn Customers
*   Predicted Churn Rate
*   Average Predicted Churn Probability

**Predictive Visuals**:

*   Predicted Churn by Gender, Age Group, State
*   Churn Probability vs Monthly Charge

***

## 🧩 High-Level Architecture

    SQL Server (ETL + Analytical Views)
            │
            ├──► Power BI (Historical Analysis)
            │
            └──► Python ML Engine
                    │
                    ├── Predictions → Power BI
                    └── Predictions for New Joiners

***

## 🎯 Project Objectives

*   Build a practical, business-oriented churn analytics pipeline
*   Understand historical churn patterns
*   Predict customers at high risk of leaving
*   Identify churn drivers and categories
*   Support retention strategies with ML + BI

***

## 🚀 Future Improvements

*   SHAP explainability for model transparency
*   Deploy ML model as API (FastAPI / Flask)
*   Automate daily predictions with Azure Data Factory / Prefect
*   Add new features (LTV, RFM scoring, NPS)
*   Integrate retention recommendations (Next Best Action Engine)

***

## 📥 How to Use This Repository

1.  **Load the dataset** → Place raw data in `Data/`
2.  **Run SQL ETL** → Execute scripts in `MSSQL-ETL/`
3.  **Open Power BI** → Load `Churn Analysis_DashBoard.pbix`
4.  **(Optional) Generate ML predictions** → Run `python churnpred/churnpred.py`
5.  **Refresh Power BI** → Load updated CSV predictions

***

## 🏁 Final Notes

This repository showcases a realistic and fully integrated data solution combining:

*   ETL
*   Machine Learning
*   Semantic Modeling
*   Business Intelligence

Ideal for enterprise churn analytics and customer retention forecasting.

***
