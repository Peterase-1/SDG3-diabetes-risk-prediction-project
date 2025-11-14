# Diabetes Risk Prediction for SDG 3: Good Health and Well-Being

This repository contains a completed mini-project for **SDG 3 – Good Health and Well-Being**. The goal is to use machine learning to predict the likelihood of diabetes based on basic health indicators, demonstrating how AI can support early detection and preventive healthcare.

## Project Overview

- **SDG Focus**: SDG 3 – Good Health and Well-Being
- **Problem**: Many people at risk of diabetes remain undiagnosed until complications appear.
- **Solution**: A supervised machine learning model (Logistic Regression) trained on the Pima Indians Diabetes dataset to predict diabetes risk.

The model uses features such as pregnancies, glucose level, blood pressure, BMI, family history (diabetes pedigree), and age to predict whether a patient is likely to have diabetes (`Outcome`: 0 = no diabetes, 1 = diabetes).

## Repository Contents

- `notebooks/diabetes_risk_prediction.ipynb`
  Full ML workflow: data loading, exploration, preprocessing, model training, evaluation, and visualizations.

- `src/diabetes_model.py`
  Script version of the core ML pipeline that can be run from the command line.

- `article/diabetes_sdg3_report.md`
  Report explaining the SDG problem, ML approach, results, and ethical reflection.

- `slides/pitch_deck_outline.md`
  Outline for a 5-minute pitch deck presenting the project.

> **Note:** The dataset file itself is **not** included. Place `diabetes.csv` (Pima Indians Diabetes dataset) in the `data/` folder.

## Results (Model Performance)

On the held-out test set, the Logistic Regression model achieved:

- **Accuracy**: `0.71` (71%)
- **Class 0 (no diabetes)**: precision `0.76`, recall `0.82`, F1-score `0.79`, support `100`
- **Class 1 (diabetes)**: precision `0.61`, recall `0.52`, F1-score `0.56`, support `54`

The model is better at correctly identifying people **without** diabetes than those **with** diabetes. In a real healthcare context, false negatives (missed diabetes cases) are especially important, so this model should be treated as a **support tool** rather than a final decision-maker.

## How to Run

1. Install dependencies:

   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

2. Place the dataset at:

   ```text
   data/diabetes.csv
   ```

3. Run the notebook:

   - Open `notebooks/diabetes_risk_prediction.ipynb` in Jupyter / VS Code.
   - Run all cells.

4. Or run the script from the project root:

   ```bash
   python src/diabetes_model.py
   ```

## Ethical & SDG Reflection (Short)

- Supports **SDG 3** by illustrating how AI can assist in early identification of people at risk of diabetes.
- The dataset comes from a specific population (Pima Indians), so the model may not generalize to all groups without retraining and validation.
- Predictions should **support** healthcare professionals, not replace them; human oversight is essential to avoid harmful misclassification and unfair decisions.
