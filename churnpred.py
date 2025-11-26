import pandas as pd
import numpy as np
from pathlib import Path


excel_path = r"Your File Path"
output_folder = Path(r"Your Outputs File Path")
output_folder.mkdir(parents=True, exist_ok=True)

sheet_churn = "Churn Data"
sheet_join = "Join Data"


df_churn = pd.read_excel(excel_path, sheet_name=sheet_churn)
df_join = pd.read_excel(excel_path, sheet_name=sheet_join)

print(df_churn.shape, df_join.shape)
print(df_churn["Customer_Status"].value_counts())


y = (df_churn["Customer_Status"] == "Churned").astype(int)

drop_cols = ["Customer_ID", "Customer_Status", "Churn_Category", "Churn_Reason"]
feature_cols = [c for c in df_churn.columns if c not in drop_cols]

X = df_churn[feature_cols]

num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = [c for c in X.columns if c not in num_cols]

print("Num cols:", num_cols)
print("Cat cols:", cat_cols)


from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    roc_auc_score,
    classification_report,
    precision_recall_curve,
)
from xgboost import XGBClassifier

preprocess = ColumnTransformer(
    transformers=[
        ("num", "passthrough", num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ]
)

xgb_churn = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_lambda=1.0,
    random_state=42,
    eval_metric="logloss",
    n_jobs=4,
)

clf_churn = Pipeline(
    steps=[
        ("preprocess", preprocess),
        ("model", xgb_churn),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

clf_churn.fit(X_train, y_train)


y_proba_test = clf_churn.predict_proba(X_test)[:, 1]

roc = roc_auc_score(y_test, y_proba_test)
print(f"ROC-AUC (test): {roc:.3f}")

prec, rec, th = precision_recall_curve(y_test, y_proba_test)
f1 = 2 * prec * rec / (prec + rec + 1e-9)
best_idx = np.argmax(f1)
best_thresh = th[best_idx]

print(f"Best threshold (F1): {best_thresh:.3f}")
print(f"Precision@best: {prec[best_idx]:.3f}")
print(f"Recall@best:    {rec[best_idx]:.3f}")
print(f"F1@best:        {f1[best_idx]:.3f}")

y_pred_best = (y_proba_test >= best_thresh).astype(int)
print("\nClassification report (threshold optimized):")
print(classification_report(y_test, y_pred_best, digits=3))


df_churners = df_churn[df_churn["Customer_Status"] == "Churned"].copy()
X_cat = df_churners[feature_cols]
y_cat = df_churners["Churn_Category"]

from sklearn.preprocessing import LabelEncoder

le_cat = LabelEncoder()
y_cat_enc = le_cat.fit_transform(y_cat)

X_cat_train, X_cat_test, y_cat_train, y_cat_test = train_test_split(
    X_cat, y_cat_enc, test_size=0.25, random_state=42, stratify=y_cat_enc
)

xgb_cat = XGBClassifier(
    n_estimators=400,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_lambda=1.0,
    random_state=42,
    eval_metric="mlogloss",
    n_jobs=4,
)

clf_cat = Pipeline(
    steps=[
        ("preprocess", preprocess),
        ("model", xgb_cat),
    ]
)

clf_cat.fit(X_cat_train, y_cat_train)

y_cat_pred = clf_cat.predict(X_cat_test)
print("\nChurn Category – Classification Report:")
print(classification_report(y_cat_test, y_cat_pred, digits=3))


p_churn_all = clf_churn.predict_proba(X)[:, 1]
pred_label_all = np.where(
    p_churn_all >= best_thresh, "Predicted_Churn", "Predicted_Stay"
)

cat_pred_all = le_cat.inverse_transform(clf_cat.predict(X))

df_scores_all = df_churn.copy()
df_scores_all["Pred_Churn_Prob"] = p_churn_all
df_scores_all["Pred_Churn_Label"] = pred_label_all
df_scores_all["Pred_Churn_Category"] = np.where(
    df_scores_all["Pred_Churn_Label"] == "Predicted_Churn",
    cat_pred_all,
    "No churn"
)

out_all = output_folder / "churn_predictions_all_customers.csv"
df_scores_all.to_csv(out_all, index=False, encoding="utf-8-sig")
print(f"\n[OK] Ficheiro gerado: {out_all}")


X_join = df_join[feature_cols]
p_churn_join = clf_churn.predict_proba(X_join)[:, 1]
pred_label_join = np.where(
    p_churn_join >= best_thresh, "Predicted_Churn", "Predicted_Stay"
)

cat_pred_join = le_cat.inverse_transform(clf_cat.predict(X_join))

df_join_scores = df_join.copy()
df_join_scores["Pred_Churn_Prob"] = p_churn_join
df_join_scores["Pred_Churn_Label"] = pred_label_join
df_join_scores["Pred_Churn_Category"] = np.where(
    df_join_scores["Pred_Churn_Label"] == "Predicted_Churn",
    cat_pred_join,
    "No churn"
)

out_join = output_folder / "churn_predictions_new_joiners.csv"
df_join_scores.to_csv(out_join, index=False, encoding="utf-8-sig")
print(f"[OK] Ficheiro gerado: {out_join}")
