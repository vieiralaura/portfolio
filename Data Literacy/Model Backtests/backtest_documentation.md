# Backtest Documentation  
This repository contains guidelines and best practices for conducting backtests in predictive modeling.
The document outlines when to perform backtests, key questions to ask before starting, data requirements, and an overview of key metrics used to
evaluate model performance.  

## What is a Model?  
A predictive model uses statistical methods to analyze historical data and create a mathematical equation to reduce uncertainty in future data predictions.  
- **Prebuilt Models:** Generic models created using industry or market data for broader applications.  
- **Customized Models:** Tailored models designed for specific clients or segments by adjusting variables or weights.  
---
## What is a Backtest?  
A backtest processes historical data to simulate the expected performance of a model in a past timeframe. The goal is to estimate how the model would behave in production and demonstrate its value.  
### Differences Between Backtest and Production  
- **Backtest:** Evaluates model performance on historical data.  
- **Production:** Uses real-time data for decision-making.  
Results from backtests are estimations and may vary from actual production performance.  

---
## When to perform a Backtest?  
Backtests are typically conducted when:  
- We need to demonstrate the value of an existing product or solution.  
- Historical data analysis is required for internal studies.  
---

## When Not to Perform a Backtest?  
A backtest is not recommended when:  
- The client does not have or is unwilling to share historical data for analysis.  
- Transaction dates are not available.  
- The client’s dataset is not mature enough (e.g., for fraud analysis, the data should be at least 3 months old).  
---

## Key Questions to Ask Before Starting a Backtest  
### General Questions  
1. What is the client’s product or service?  
2. How long has the operation been running?  
3. What problem is the client trying to solve?  
4. What is the client’s desired outcome (e.g., reducing fraud, increasing approval rates)?  
5. What data can the client provide?  

### Data-Specific Questions  
1. Does the client have a historical dataset to evaluate customer profiles?  
  - If not, consider presenting a case study to demonstrate the product’s value.  
2. Are the provided datasets representative of the client’s operations?  

### Technical Questions  
1. Are the data fields used in the backtest the same as those collected during production?  
2. Does the client have labels for fraud/non-fraud transactions?  
3. What is the expected success metric?  
  - Examples: fraud reduction rate, approval rate increase, or performance comparison with existing solutions.  
---

---
## Data Requirements  
### Essential Fields  
- **Customer Identifier:** Example: CPF (Brazilian Tax ID) or another unique identifier.  
- **Transaction Date:** Required for accurate simulation of past events.  
- **Response Variable:** Fraud/non-fraud labels (1 for fraud, 0 for non-fraud).  

### Sample Characteristics  
1. Must represent the client’s operations, including approved and rejected transactions.  
2. Minimum of 3,000 transactions and maximum of 100,000 transactions.  
3. Historical data covering at least 6 months with a minimum of 3 months before the current date.  

---
## Performance Metrics  
### Kolmogorov-Smirnov (KS)  
- Measures the model's ability to separate good transactions from fraudulent ones.  
- A higher KS indicates better separation between good and bad transactions.  
### Custom Index (Example: CSI)  
- Indicates the percentage of risky transactions flagged by the model in the highest scoring bands.  
---

## Data Format and Quality  
### File Format  
- **Preferred Format:** CSV (Comma-Separated Values).  
 - Faster processing and lower error rates compared to other formats.  
### Data Quality  
- Ensure consistency and completeness in the dataset. Poor data quality directly affects model performance and results.  
---