# Customer Churn Analysis

## Project Overview

This project analyzes customer churn in a telecommunications dataset using Python. It explores customer retention, contract types, internet services, and customer tenure to identify patterns associated with customers leaving a service.

## Objectives

- Calculate the overall customer churn rate.
- Compare churn across contract types.
- Analyze churn by internet service.
- Identify churn patterns by customer tenure.
- Create visualizations and export summary reports.
- Recommend potential customer retention strategies.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Git and GitHub

## Key Results

| Metric | Result |
|---|---:|
| Customers analyzed | 7,032 |
| Customers churned | 1,869 |
| Customers retained | 5,163 |
| Churn rate | 26.58% |
| Average monthly charges | $64.80 |
| Average tenure | 32.4 months |

## Key Business Insights

### 1. Contract Type

Month-to-month customers had the highest churn rate at 42.71%. One-year contracts had an 11.28% churn rate, while two-year contracts had a 2.85% rate.

### 2. Internet Service

Customers with fiber optic service had a churn rate of 41.89%, compared with 19.00% for DSL customers and 7.43% for customers without internet service.

### 3. Customer Tenure

Customers with 12 months or less of tenure had a churn rate of 47.68%. Customers with 49–72 months of tenure had a churn rate of 9.51%.

### Recommendations

- Improve onboarding and support for new customers.
- Investigate service satisfaction among fiber optic customers.
- Evaluate retention offers for month-to-month customers.
- Monitor churn trends regularly to identify at-risk customer groups.

These results show associations in the dataset and do not prove causation.

## Visualizations and Reports

The analysis generates these files in the `charts/` directory:

- `churn_distribution.png`
- `churn_by_contract.png`
- `churn_by_tenure.png`
- `contract_churn_summary.csv`
- `internet_churn_summary.csv`
- `tenure_churn_summary.csv`

## Project Structure

```text
customer-churn-analysis/
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── charts/
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```powershell
git clone https://github.com/krishnakolli1/customer-churn-analysis.git
cd customer-churn-analysis
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Add the dataset

Place the CSV file in the `data/` folder with the filename:

`WA_Fn-UseC_-Telco-Customer-Churn.csv`

### 5. Run the analysis

```powershell
python analysis.py
```

## Dataset

The project uses the IBM Telco Customer Churn dataset for educational and portfolio purposes. Refer to the original dataset source for its licensing and redistribution terms.

Dataset source: [Kaggle — Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis
- Customer retention metrics
- Grouping and aggregation with Pandas
- Churn rate analysis
- Data visualization
- Business reporting and recommendations
