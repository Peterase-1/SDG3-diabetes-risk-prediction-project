# Diabetes Risk Prediction and SDG 3: Good Health and Well-Being

## 1. SDG Problem Addressed

This project focuses on **SDG 3 – Good Health and Well-Being**, with a specific emphasis on the growing burden of diabetes.

Diabetes is a chronic disease that can lead to serious complications such as heart disease, kidney failure, blindness, and amputations. Many people at risk of diabetes are not diagnosed early, especially in low-resource settings. Early identification of individuals who are likely to have diabetes can support:

- Earlier screening and lifestyle interventions
- Better allocation of limited health resources
- Prevention of severe complications and healthcare costs

By using data-driven risk prediction, this project aims to demonstrate how **AI can support preventive healthcare** as part of SDG 3.

## 2. Machine Learning Approach

The project uses a classic **supervised learning** setup with the **Pima Indians Diabetes dataset**. Each row in the dataset represents one patient, with features such as:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction (family history)
- Age

The target variable is **`Outcome`**:

- `0` → no diabetes
- `1` → diabetes

### Model Pipeline

1. Load the dataset from `diabetes.csv` using `pandas`.
2. Explore the data: shape, missing values, distribution of the `Outcome` variable.
3. Split data into **features (`X`)** and **target (`y`)**.
4. Split into **training** and **test** sets using `train_test_split`.
5. **Standardize** the features using `StandardScaler`.
6. Train a **Logistic Regression** classifier.
7. Evaluate the model using:
   - Accuracy
   - Precision, Recall, F1-score
   - Confusion matrix and basic visualizations

This is summarized as: **"Logistic Regression for Diabetes Risk Prediction"**.

## 3. Results and Interpretation

Based on the final run of the Logistic Regression model, the performance on the held-out test set is:

- **Accuracy**: `0.71` (71%) on the test set.
- **Class 0 (no diabetes)**: precision `0.76`, recall `0.82`, F1-score `0.79`, support `100`.
- **Class 1 (diabetes)**: precision `0.61`, recall `0.52`, F1-score `0.56`, support `54`.

This means the model is better at correctly identifying people **without** diabetes than those **with** diabetes. In healthcare, **false negatives** (missed diabetes cases) are particularly important, because they represent people who need care but are not flagged. False positives (people incorrectly predicted to have diabetes) can also cause stress and extra tests, but they are generally safer than missing a real case.

Overall, the results suggest that this model can be useful as a **support tool** for early risk screening, but it should not be used as the only basis for clinical decisions.

## 4. Ethical and Social Considerations

### 4.1 Bias and Representativeness

The Pima Indians Diabetes dataset comes from a specific population group. A model trained solely on this data may not generalize well to populations with:

- Different genetic backgrounds
- Different diets and lifestyles
- Different access to healthcare

Using this model directly in another country or community without proper validation could introduce **bias** and unfair predictions.

### 4.2 Fairness and Responsibility

- The model should not be used to deny care or insurance.
- It should instead be used to **support** healthcare workers in identifying high-risk individuals for further tests.
- Transparent communication with patients is important so they understand that predictions are probabilistic, not perfect.

### 4.3 Sustainability and SDG Impact

- By promoting **early detection**, AI models like this can reduce the long-term complications of diabetes.
- This can lower healthcare costs, improve quality of life, and help health systems use their resources more efficiently.
- In combination with public health campaigns and education, AI tools can contribute to more sustainable, preventive healthcare systems.

## 5. Conclusion

This project shows how a relatively simple **Logistic Regression** model, applied to an open diabetes dataset, can:

- Highlight key risk factors such as glucose levels, BMI, and age
- Predict the likelihood of diabetes for individuals based on health indicators
- Support **SDG 3 – Good Health and Well-Being** by enabling preventive and data-driven healthcare

However, it also emphasizes the need to treat AI as a **support tool**, carefully consider data bias, and ensure ethical use in real-world health settings.
