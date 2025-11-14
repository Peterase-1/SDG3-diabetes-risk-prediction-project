# Pitch Deck Outline – Diabetes Risk Prediction for SDG 3

You can use this outline to create PowerPoint or Google Slides for a 5-minute presentation.

---

## Slide 1 – Title & Introduction

- **Title**: Diabetes Risk Prediction using Machine Learning
- **Subtitle**: Supporting SDG 3 – Good Health and Well-Being
- Your name, course (PLP Academy), date

---

## Slide 2 – The Problem (SDG Context)

- Diabetes is a growing global health challenge.
- Many people at risk remain undiagnosed until complications occur.
- Link to **SDG 3**: Ensure healthy lives and promote well-being for all.
- Brief statement: "How can AI help identify high-risk individuals earlier?"

---

## Slide 3 – Data and Approach

- Dataset: Pima Indians Diabetes dataset (open-source).
- Each row = one patient with features like:
  - Glucose, BloodPressure, BMI, Age, etc.
- Task: **Binary classification** – predict `Outcome` (0 = no diabetes, 1 = diabetes).
- ML method: **Logistic Regression** (supervised learning).

---

## Slide 4 – Model Workflow

- Simple pipeline diagram or bullet list:
  1. Load data from `diabetes.csv`.
  2. Split into train/test sets.
  3. Scale features with StandardScaler.
  4. Train Logistic Regression model.
  5. Evaluate using accuracy, precision, recall, F1-score.
- Mention tools: Python, pandas, scikit-learn, matplotlib/seaborn.

---

## Slide 5 – Results & Visuals

- Show:
  - Accuracy value (e.g., around 75–80%, update with your actual result).
  - Short table or screenshot of classification report.
  - Confusion matrix image (screenshot from notebook).
- Simple interpretation:
  - The model can correctly identify many patients with diabetes.
  - Discuss trade-off between false positives and false negatives.

---

## Slide 6 – Impact on SDG 3

- How this model contributes to SDG 3:
  - Supports **early detection** and preventive care.
  - Helps target screenings where they are most needed.
  - May reduce severe complications and healthcare costs.
- Emphasize that this is a **prototype** or proof-of-concept.

---

## Slide 7 – Ethics, Bias, and Limitations

- Data bias: dataset comes from one population – may not generalize globally.
- The model should **support** health professionals, not replace them.
- Risk of misclassification (false negatives and false positives).
- Need for:
  - More diverse datasets
  - Validation in real clinical environments

---

## Slide 8 – Future Work & Conclusion

- Possible improvements:
  - Try other models (Random Forest, XGBoost, etc.).
  - Hyperparameter tuning.
  - Use larger and more diverse datasets.
- Final message:
  - AI is a powerful **support tool** for preventive healthcare.
  - This project shows how basic ML techniques can contribute to **SDG 3 – Good Health and Well-Being**.
