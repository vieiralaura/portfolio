# Backtest Documentation  
This repository contains guidelines and best practices for conducting backtests in predictive modeling.
The document outlines when to perform backtests, key questions to ask before starting, data requirements, and an overview of key metrics used to
evaluate model performance.  

## Objective
This documentation was designed to help the pre-sales team understand the fundamentals of statistical model backtesting. Backtesting is a crucial tool for demonstrating the value of predictive models, providing tangible proof of their performance and reliability.

The document explains key concepts, metrics, and the methodology used to ensure accurate and impactful backtest results.

---

## Key concepts
### What is a statistical model?  
A predictive model uses statistical methods to analyze historical data and create a mathematical equation to reduce uncertainty in future data predictions.

The model is created from a historical base (training) with several variables that analyze the behavior of transactions, customer profiles, registration data, alerts, etc. Once we have this equation (which we call a model) ready, we can use new data to predict the probability of fraud or default, for example.

For the model to work, this new data must be similar to the data that was used to train the model.

We can have prebuilt models or customized models. 
- **Prebuilt Models:** Generic models created using industry or market data for broader applications.  
- **Customized Models:** Tailored models designed for specific clients or segments by adjusting variables or weights.
  
### What is a Backtest?  
A backtest processes historical data to simulate the expected performance of a model in a past timeframe. The goal is to estimate how the model would behave in production and demonstrate its value. 

### Differences Between Backtest and Production  
- **Backtest:** Evaluates model performance on historical data.  
- **Production:** Uses real-time data for decision-making.  
It is imoportant to know that the results from backtests are estimations and may vary from actual production performance.  

### When to perform a Backtest?  
Backtests are typically conducted when:  
- We need to demonstrate the value of an existing product or solution (models).  
- Historical data analysis is required for internal studies to change the current model.  

### When not to perform a Backtest?  
A backtest is not recommended when:  
- The client does not have or is unwilling to share historical data for analysis.  
- Transaction dates are not available.  
- The client’s dataset is not mature enough (e.g., for fraud analysis, the data should be at least 3 months old).
  
---

## Key questions to ask before starting a Backtest  
Some key questions that can guide you before requesting a study or backtest!

### General Questions  
1. What is the client’s product or service?  
2. How long has the operation been running?  
3. What problem is the client trying to solve?  
4. What is the client’s desired outcome (e.g., reducing fraud, increasing approval rates)?  
5. What data can the client provide?  

### Data-Specific Questions  
1. Does the client have a historical dataset to evaluate customer profiles?  
  - If not, consider presenting a case study to demonstrate the product’s value instead of backtesting.  
2. Are the provided datasets representative of the client’s operations?  

### Technical Questions  
1. Are the data fields used for input in the backtest the same as those collected during production?  
2. Does the client have labels for success/non-success transactions? (The target variable is available?)
3. What is the expected success metric?  
  - Examples: fraud reduction rate, approval rate increase, or performance comparison with existing solutions.  

---
## Data Requirements  
The data required to perform a backtest will depend on each model, but the general guidelines listed below are the same for all backtests.
It is important to ensure consistency and completeness in the dataset. Poor data quality directly affects model performance and results.

For the model to work well and provide reliable results, the quality of the client's database is essential. If we receive inconsistent or incomplete data, the model will not perform well and the results may be compromised, which directly reflects on the customer's perception of the value of our product.

## Sample
### Concepts
- **Universe or Population**: The total number of individuals we aim to study or characterize.
- **Sample**: A subset of individuals selected from the universe/population for study.
- **Representative Sample**: To ensure the model performs accurately, the sample must represent the real-world population of individuals. This means it must be randomly drawn from the dataset to include common cases, outliers, and fraud cases. If the sample is biased (e.g., contains only recent transactions, approved requests, or only fraudulent cases), the backtest might not reflect reality, leading to inaccurate results.
Thus, the client does not need to provide the entire dataset. A representative sample is sufficient, provided it includes a reasonable number of fraudulent cases.

#### Why a Representative Sample?
- **Lower Data Volume**: Easier to process.
- **Reduced Processing Costs**: Saves resources.
- **Faster Results**: Without compromising accuracy.

#### Guidelines for Extracting a Representative Dataset
- **Characteristics of the Sample**: It should reflect the client’s request population and the real scenario, including order volume, monthly approval rate, and fraud/cbk rate. No filters should be applied—both approved and rejected requests must be included.
- **Number of Requests and Time Frames**:
 - Minimum of 3,000 transactions and maximum of 100,000.
 - At least six cohorts, with a minimum gap of three months from the current date and a maximum gap of one year.  
   Example: For May 2024, ideal cohorts range from September 2023 to February 2024.
- **Response Variable**: Must be significant, with at least 100 fraudulent cases. Fraud cases should be marked as `1` and non-fraud cases as `0`.
  
### Essential Fields  
- **Customer Identifier:** Example: CPF (Brazilian Tax ID) or another unique identifier.  
- **Transaction Date:** Required for accurate simulation of past events.  
- **Response Variable:** Fraud/non-fraud labels (1 for fraud, 0 for non-fraud).  

### Data Format and Quality  
- **Preferred Format:** CSV (Comma-Separated Values).  
 - Faster processing and lower error rates compared to other formats.  
  
### Importance of the DATE Field
The date is crucial for backtesting. A historical date is required to simulate what the model would have done in the past. If the data contains only today’s date, the backtest will not represent historical performance, making the results misleading.
Without the correct date:
- The backtest cannot simulate past performance accurately.
- Results will be flawed as they’ll measure against today’s response variable.

### Why do we need the target variable?
The response variable (indicating whether a transaction was fraudulent) is essential to validate the model used in the backtest. Without it:
- We cannot measure performance or determine whether the model is making accurate decisions.
- The client might measure performance independently, potentially leading to inconsistent or incorrect conclusions due to lack of expertise.
This can harm the credibility of the backtest, as improper evaluations might lead to an incorrect assessment of the model’s effectiveness.

---

## Performance Measurement
To evaluate model performance on the test dataset during the backtest, we rely on key metrics. The main ones used today are **KS** and **CI**.
These metrics are critical to demonstrate the model's effectiveness, but they depend on high-quality data and the presence of the response variable (fraud or not). Performance measurement is impossible without this variable.
### KS - Kolmogorov-Smirnov
- **Definition**: Measures the model's ability to separate good orders (non-fraudulent) from bad ones (fraudulent).  
- The KS value represents the difference between the cumulative distribution of good and bad orders. A low KS indicates that the distributions are very similar, meaning the model struggles to differentiate between good and bad orders.
- **Visualization**: Think of two curves—one for good orders and one for bad orders. The KS is the maximum distance between these two curves.  
- This metric is widely recognized and used beyond our organization.
### CI - Custom Index
- **Definition**: A proprietary metric that represents the percentage of the riskiest population captured during analysis.  
- **Example**: CI20 indicates the percentage of bad orders within the top 20% of orders with the highest scores. If CI20 = 60%, it means that 60% of the fraud cases are within the top 20% highest-scoring orders. A rejection cut at this level would capture 60% of the fraud.
- This analysis can also be applied with other cutoffs, such as CI5, CI10, CI15.
  
### Result Big Table
The Result Big Table organizes the dataset to highlight the concentration of bad orders. The dataset is divided into 20 equal-sized segments, each containing 5% of the orders, sorted by score.  
- The first segments contain the concentration of good orders, while the last ones concentrate the bad orders.  
- For fraud detection, higher scores indicate higher risk, so bad orders should accumulate in the last segments.  
- For credit risk, the interpretation is reversed: delinquency should concentrate in the first segments.

---

## Key Points to Reassure Clients:
1. **Data Usage**: The client’s data is used exclusively for backtesting purposes.
2. **Transparent Results**: The backtest demonstrates how the model performs using their data, ensuring they know what to expect once the model is implemented in production.
3. **Shared Goals**: We are also motivated to achieve high model performance, as we are accountable for contractual indicators.
