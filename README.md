# Diabetes Risk Prediction for SDG 3: Good Health and Well-Being

This project is part of the **PLP Academy Week 2 Assignment: AI for Sustainable Development**.

## Project Overview

- **SDG Focus**: SDG 3 – Good Health and Well-Being
- **Problem**: Many people at risk of diabetes remain undiagnosed. Early prediction can support screening and prevention.
- **Solution**: A supervised machine learning model that predicts the risk of diabetes using health-related features from the Pima Indians Diabetes dataset.

## Repository Contents

- `notebooks/diabetes_risk_prediction.ipynb`  
  Jupyter Notebook with the full ML workflow: data loading, preprocessing, model training, evaluation, and visualizations.

- `src/diabetes_model.py`  
  Python script version of the core ML pipeline (can be run from the command line).

- `article/diabetes_sdg3_report.md`  
  1-page style article explaining the SDG problem, ML method, results, and ethical reflection.

- `slides/pitch_deck_outline.md`  
  Outline of a 5-minute pitch deck you can turn into PowerPoint/Google Slides.

> **Note:** The dataset file itself is **not** included. Download the `diabetes.csv` file (Pima Indians Diabetes Database from Kaggle/other source) and place it into the `data/` folder.

## How to Run Locally

1. **Install Dependencies**

   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

2. **Project Structure** (expected)

   ```text
   Week 2/
   ├─ data/
   │  └─ diabetes.csv
   ├─ notebooks/
   │  └─ diabetes_risk_prediction.ipynb
   ├─ src/
   │  └─ diabetes_model.py
   ├─ article/
   │  └─ diabetes_sdg3_report.md
   └─ slides/
      └─ pitch_deck_outline.md
   ```

3. **Run the Notebook**

   - Open Jupyter Notebook (or VS Code with Jupyter support).
   - Open `notebooks/diabetes_risk_prediction.ipynb`.
   - Run the cells from top to bottom.

4. **Run the Script (Optional)**

   From the project root (where this README is), run:

   ```bash
   python src/diabetes_model.py
   ```

## Screenshots for Submission

Take screenshots after running the notebook, for example:

- Confusion matrix plot
- Classification report / accuracy printout
- Feature importance (coefficients) bar chart

Add them to your README or upload alongside your submission.

## Ethical & SDG Reflection (Short)

- The model supports **SDG 3** by helping detect potential diabetes cases earlier.
- Data comes from a specific population (Pima Indians), so predictions may not generalize to all groups.
- Such models should support doctors, not replace them, to avoid harmful misclassification.

You can modify all text to match your own style and learning reflections.
