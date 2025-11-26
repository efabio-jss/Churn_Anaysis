

📘 Customer Churn Prediction Pipeline
*A documentation file for `churnpred.py`*


🔍 Overview
`churnpred.py` implements a complete **machine learning workflow** for analyzing customer churn.
The script:

- Predicts whether a customer is likely to churn  
- Identifies the **most probable churn reason** for customers predicted as churners  
- Generates enriched outputs for:
  - **Historical customers** ("Churn Data")
  - **New joiners** ("Join Data")

The pipeline integrates **XGBoost**, **scikit-learn**, and **pandas** inside a clean, modular architecture.


📂 Input Structure
The script reads an Excel file that must contain:

| Sheet Name       | Description                                   |
|------------------|-----------------------------------------------|
| **Churn Data**   | Historical dataset with churn labels          |
| **Join Data**    | New customers for churn risk scoring          |

Paths must be defined before running:

```python
excel_path = r"Your File Path"
output_folder = Path(r"Your Outputs File Path")
```

The output folder is created automatically if it does not exist.


🧽 1. Data Preparation

   Columns removed from the feature set:
- `Customer_ID`
- `Customer_Status`
- `Churn_Category`
- `Churn_Reason`

   Automatic Feature Handling
- **Numeric fields** → passed through unchanged  
- **Categorical fields** → One-Hot Encoding (`handle_unknown="ignore"`)

A `ColumnTransformer` prepares both types consistently.


🤖 2. Churn (Binary) Classifier

Target Definition
```python
Customer_Status == "Churned" → 1
Otherwise → 0
```

Model: XGBoostClassifier
Key hyperparameters:
- n_estimators=300
- max_depth=4
- learning_rate=0.05
- subsample=0.8
- colsample_bytree=0.8
- reg_lambda=1.0

Train/Test Split
- 75% training  
- 25% testing  
- Stratified to maintain churn proportion  


📊 3. Model Evaluation

The script computes the following:

- ROC-AUC  
- Precision–Recall Curve  
- F1-optimized probability threshold  
- Classification report with optimized threshold

The F1-optimized threshold replaces the default 0.5 threshold for better prediction balance.


🏷️ 4. Churn Reason Prediction (Multi-Class)

A second model predicts **churn reasons**, applied only to customers who truly churned.

Steps:
1. Filter churned customers  
2. Label-encode churn category  
3. Train a multi-class XGBoost model  
4. Generate classification report  

This model is reused to assign churn reason predictions to newly evaluated customers.


📤 5. Output Generation

A. `churn_predictions_all_customers.csv`
Contains predictions for all customers.  
Added columns:

| Column                | Meaning                                         |
|-----------------------|-------------------------------------------------|
| `Pred_Churn_Prob`     | Probability of churn                            |
| `Pred_Churn_Label`    | “Predicted_Churn” or “Predicted_Stay”           |
| `Pred_Churn_Category` | Predicted churn reason (if churn), else "No churn" |


B. `churn_predictions_new_joiners.csv`
Same structure as above but applied to **Join Data** for scoring new customers.


📁 Output Files
Saved automatically to your configured directory:

churn_predictions_all_customers.csv
churn_predictions_new_joiners.csv



⚙️ Dependencies

Install the required packages:

pip install pandas numpy scikit-learn xgboost openpyxl



🚀 Summary

This script provides a fully automated churn prediction solution:

- Loads and processes customer datasets  
- Trains two XGBoost models (binary + multi-class)  
- Optimizes prediction thresholds  
- Generates ready-to-use enriched CSV prediction files  
- Supports both historical and new customers  

A production-ready foundation for churn analytics and retention strategy development.
