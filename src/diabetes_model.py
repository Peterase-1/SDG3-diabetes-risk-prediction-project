import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def load_data(csv_path: str) -> pd.DataFrame:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(
            f"Data file not found at '{csv_path}'. Please download the Pima Indians Diabetes "
            f"dataset (diabetes.csv) and place it in the 'data' folder."
        )
    data = pd.read_csv(csv_path)
    return data


def preprocess_and_split(data: pd.DataFrame):
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns


def train_and_evaluate(X_train, X_test, y_train, y_test, feature_names):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")

    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.show()

    # Feature importance (coefficients)
    coefficients = model.coef_[0]
    coef_df = pd.DataFrame({
        "feature": feature_names,
        "coefficient": coefficients,
    }).sort_values(by="coefficient", key=np.abs, ascending=False)

    print("\nLogistic Regression Coefficients (sorted by absolute value):")
    print(coef_df)

    plt.figure(figsize=(8, 5))
    sns.barplot(data=coef_df, x="coefficient", y="feature")
    plt.title("Feature Importance (Logistic Regression Coefficients)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Adjust this path if your folder structure is different
    csv_path = os.path.join("data", "diabetes.csv")

    print("Loading data from:", csv_path)
    data = load_data(csv_path)

    print("Data shape:", data.shape)
    print(data.head())

    X_train_scaled, X_test_scaled, y_train, y_test, feature_names = preprocess_and_split(data)

    train_and_evaluate(X_train_scaled, X_test_scaled, y_train, y_test, feature_names)
