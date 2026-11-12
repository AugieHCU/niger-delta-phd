import xgboost as xgb
import pandas as pd

def train_mvi_classifier(X_train: pd.DataFrame, y_train: pd.Series) -> xgb.XGBClassifier:
    """Train the XGBoost classifier for Morphodynamic Vulnerability Index (MVI) prediction."""
    model = xgb.XGBClassifier(
        n_estimators=150,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric="logloss"
    )
    model.fit(X_train, y_train)
    return model
