# Data-A
# Customer Churn Analysis: Python & PostgreSQL

## Project Overview

Customer churn occurs when customers stop using a company's products or services. Understanding churn helps businesses identify at-risk customer segments and develop data-informed retention strategies.

This project analyzes customer churn using PostgreSQL and Python to uncover patterns associated with contract type, internet service, payment method, customer tenure, and monthly charges.

The goal is to transform raw customer data into actionable business insights.

## Business Problem

The business needs to understand:

- What proportion of customers leave the company?
- Which contract types have the highest churn rates?
- How does churn vary by internet service and payment method?
- Which combinations of customer tenure and monthly charges are associated with higher churn?
- Which customer segments should the business prioritize for retention efforts?

## Tools and Technologies

- **PostgreSQL:** SQL queries, aggregation, grouping, filtering, and churn-rate calculations.
- **Python:** Data analysis and integration with SQL results.
- **Pandas:** Data manipulation and presentation.
- **Matplotlib:** Data visualization.
- **Jupyter Notebook:** Interactive analysis and documentation.
- **VS Code:** Development environment.
- **Git and GitHub:** Version control and project sharing.

## Dataset

The analysis uses a customer churn dataset containing 7,032 customer records.

- Total customers: 7,032
- Customers who churned: 1,869
- Customers retained: 5,163
- Overall churn rate: 26.58%

The dataset includes customer churn status, contract type, internet service, payment method, tenure, and monthly charges.

## Methodology

### 1. Data and database preparation

Loaded the customer dataset into PostgreSQL and verified that the database contained 7,032 customer records.

### 2. SQL analysis

Used SQL to calculate customer counts, churned customer counts, and churn rates across different customer categories.

### 3. Exploratory data analysis

Investigated churn patterns across contract types, internet services, payment methods, tenure groups, and monthly charge groups.

### 4. Data visualization

Created horizontal bar charts to compare churn rates and customer losses, alongside a box plot and a heatmap to explore relationships between customer characteristics and churn.

### 5. Business recommendations

Translated the observed patterns into potential customer retention strategies.

## Key Findings

### 1. Overall customer churn

The overall churn rate was **26.58%**, meaning approximately one in four customers in the dataset had churned.

### 2. Contract type

| Contract type | Churn rate |
|---|---:|
| Month-to-month | 42.71% |
| One year | 11.27% |
| Two year | 2.83% |

Month-to-month customers had a substantially higher observed churn rate than customers on longer-term contracts.

### 3. Internet service

| Internet service | Churn rate |
|---|---:|
| Fiber optic | 41.89% |
| DSL | 18.96% |
| No internet service | 7.40% |

Fiber-optic customers had the highest observed churn rate among the three groups.

### 4. Payment method

| Payment method | Churn rate |
|---|---:|
| Electronic check | 45.29% |
| Mailed check | 19.11% |
| Bank transfer (automatic) | 16.71% |
| Credit card (automatic) | 15.24% |

Customers using electronic checks had the highest observed churn rate.

### 5. Combined customer segments

The segment combining month-to-month contracts, fiber-optic internet, and electronic-check payments had:

- Total customers: 1,307
- Churned customers: 789
- Churn rate: 60.37%

This segment is a strong candidate for further investigation and targeted retention experiments.

### 6. Customer tenure and monthly charges

Among customers with 0–12 months of tenure, the high-monthly-charge group (70 or more in the dataset's currency units) had a churn rate of 68.07%.

This suggests that newer customers with higher monthly charges may warrant closer attention.

## Business Recommendations

1. **Improve early customer retention:** Investigate onboarding experiences and provide timely support during customers' first year.
2. **Evaluate contract incentives:** Test whether suitable longer-term contract offers improve retention.
3. **Investigate fiber-optic churn:** Examine pricing, reliability, customer satisfaction, and service complaints.
4. **Review the electronic-check segment:** Investigate billing experiences and other customer characteristics before selecting interventions.
5. **Target high-risk segments:** Use customer-level evidence to design and evaluate retention campaigns.
6. **Measure outcomes:** Track retention, churn rates, campaign costs, and customer satisfaction to evaluate the effectiveness of interventions.

## Limitations

This analysis identifies associations in the available dataset. It does not establish that contract type, internet service, payment method, tenure, or monthly charges independently cause churn.

The findings should be validated with further analysis and, where practical, controlled retention experiments before major business decisions are made.

## Project Structure

```text
customer-churn-analysis/
├── README.md
├── churn_analysis.ipynb
└── .gitignore
```

Additional files, such as charts, a requirements file, or SQL scripts, can be added as the project is organized for publication.

## Skills Demonstrated

- SQL querying and aggregation
- PostgreSQL database analysis
- Python data analysis with pandas
- Exploratory data analysis
- Data visualization
- Business insight generation
- Translating analytical findings into recommendations

## Conclusion

This project demonstrates how SQL and Python can work together to investigate customer churn, identify important customer segments, and support data-informed retention decisions.

The analysis provides a foundation for further work, including churn prediction, customer segmentation, and retention campaign evaluation.

