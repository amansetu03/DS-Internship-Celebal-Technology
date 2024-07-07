## Week-8 Assignment: Loan Approval Prediction
<p>input dataset</p>

| Loan_ID   | Gender | Married | Dependents | Education     | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Property_Area | Loan_Status |
|-----------|--------|---------|------------|---------------|---------------|-----------------|-------------------|------------|------------------|----------------|---------------|-------------|
| LP001002  | Male   | No      | 0          | Graduate      | No            | 5849            | 0.0               | NaN        | 360.0            | 1.0            | Urban         | Y           |
| LP001003  | Male   | Yes     | 1          | Graduate      | No            | 4583            | 1508.0            | 128.0      | 360.0            | 1.0            | Rural         | N           |
| LP001005  | Male   | Yes     | 0          | Graduate      | Yes           | 3000            | 0.0               | 66.0       | 360.0            | 1.0            | Urban         | Y           |
| LP001006  | Male   | Yes     | 0          | Not Graduate  | No            | 2583            | 2358.0            | 120.0      | 360.0            | 1.0            | Urban         | Y           |
| LP001008  | Male   | No      | 0          | Graduate      | No            | 6000            | 0.0               | 141.0      | 360.0            | 1.0            | Urban         | Y           |

<p>Dataset after preprocess.</p>

| Loan_ID   | Gender | Married | Education     | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Loan_Status | Dependents_0 | Dependents_1 | Dependents_2 | Dependents_3+ | Property_Area_Rural | Property_Area_Semiurban | Property_Area_Urban |
|-----------|--------|---------|---------------|---------------|-----------------|-------------------|------------|------------------|----------------|-------------|--------------|--------------|--------------|---------------|---------------------|-------------------------|----------------------|
| LP001002  | 1      | 0       | 0             | 0             | 5849            | 0.0               | 128.0      | 360.0            | 1.0            | 1           | True         | False        | False        | False         | False               | False                   | True                 |
| LP001003  | 1      | 1       | 0             | 0             | 4583            | 1508.0            | 128.0      | 360.0            | 1.0            | 0           | False        | True         | False        | False         | True                | False                   | False                |
| LP001005  | 1      | 1       | 0             | 1             | 3000            | 0.0               | 66.0       | 360.0            | 1.0            | 1           | True         | False        | False        | False         | False               | False                   | True                 |
| LP001006  | 1      | 1       | 1             | 0             | 2583            | 2358.0            | 120.0      | 360.0            | 1.0            | 1           | True         | False        | False        | False         | False               | False                   | True                 |
| LP001008  | 1      | 0       | 0             | 0             | 6000            | 0.0               | 141.0      | 360.0            | 1.0            | 1           | True         | False        | False        | False         | False               | False                   | True                 |

### Use Logistic Regression
<p>model Accuracy and classification report: </p>
Accuracy: 0.79

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| 0 (Negative)| 0.95      | 0.42   | 0.58     | 43      |
| 1 (Positive)| 0.76      | 0.99   | 0.86     | 80      |

Macro Avg:
- Precision: 0.85
- Recall: 0.70
- F1-Score: 0.72

Weighted Avg:
- Precision: 0.83
- Recall: 0.79
- F1-Score: 0.76

### Confusion Matrix
|            | Predicted Negative | Predicted Positive |
|------------|--------------------|--------------------|
| Actual Negative | 18                 | 25                  |
| Actual Positive | 1                 | 79                 |
